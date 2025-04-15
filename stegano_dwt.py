import pywt
import numpy as np
import cv2

def normalize_image(image):
    """Normalize image to 0-255 range preserving float precision"""
    image = image - np.min(image)
    image = image / np.max(image)
    return image * 255

def embed_message(img, message):
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '11111110'  # EOF marker
    
    # Convert to grayscale and float32
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    
    # Apply DWT
    coeffs = pywt.dwt2(gray, 'haar')
    cA, (cH, cV, cD) = coeffs
    
    # Flatten cD coefficients
    flat_cD = cD.flatten()
    
    # Embed message
    for i in range(min(len(binary_message), len(flat_cD))):
        flat_cD[i] = int(flat_cD[i]) & ~1 | int(binary_message[i])
    
    # Reshape and inverse DWT
    cD_new = flat_cD.reshape(cD.shape)
    coeffs_new = (cA, (cH, cV, cD_new))
    img_stego = pywt.idwt2(coeffs_new, 'haar')
    
    # Normalize preserving data
    img_stego = normalize_image(img_stego)
    
    # Convert to uint8 without losing LSB data
    img_stego = np.round(img_stego).astype(np.uint8)
    
    return img_stego

def extract_message(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    
    # Apply DWT
    coeffs = pywt.dwt2(gray, 'haar')
    cA, (cH, cV, cD) = coeffs
    
    # Extract LSBs
    flat_cD = cD.flatten().astype(int)
    bits = [str(val & 1) for val in flat_cD[:8000]]  # Limit extraction
    
    # Find EOF marker
    binary_str = ''.join(bits)
    eof_index = binary_str.find('11111110')
    
    if eof_index == -1:
        return "No message found or corrupted"
    
    # Convert to text
    message = []
    for i in range(0, eof_index, 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            message.append(chr(int(byte, 2)))
    
    return ''.join(message)