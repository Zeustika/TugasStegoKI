# StegaVision DWT - Steganography Using Discrete Wavelet Transform

## Description
**StegaVision DWT** is a steganography application that uses the **Discrete Wavelet Transform (DWT)** method to embed and extract secret messages within images. This app allows users to encode a message into an image and decode it using a DWT-based algorithm. Steganography is a technique for hiding information in a way that is not easily detectable by third parties.

### Key Features:
- **Message Encoding:** Embed secret messages into PNG/JPG images using DWT.
- **Message Decoding:** Extract hidden messages from stego images.
- **Security:** Users can optionally add a password for extra security during encoding and decoding.
- **User Interface:** Easy-to-use UI built with Streamlit for a smooth interactive experience.

## Requirements
This app requires several Python packages to function properly for both steganography and user interface:

- `streamlit`: For the web-based user interface.
- `numpy`: For numerical computations.
- `opencv-python`: For image processing.
- `Pillow`: For image reading and writing.
- `stegano-dwt`: Module for DWT-based steganography implementation.

## How to Use

### Encoding a Message:
1. Select a cover image (PNG/JPG) where you want to hide the message.
2. Enter the secret message you want to embed.
3. Optionally, set a password for additional security.
4. Click the "🚀 Encode Message" button to embed the message.
5. The resulting image with the hidden message (stego image) will be displayed, and you can download it.

### Decoding a Message:
1. Select the stego image that contains the hidden message.
2. Enter the password if one was set.
3. Click the "🕵️‍♂️ Extract Message" button to reveal the hidden message.
4. The extracted message will be displayed in the app.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Zeustika/StegaVision-DWT.git
   ```

2. Navigate to the project directory:
   ```bash
   cd StegaVision-DWT
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

The app will open in your default browser.

## Project Structure
```
StegaVision-DWT/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # List of Python dependencies
├── .gitignore          # Ignore unnecessary files in Git
└── README.md           # This file
```

## Contribution
If you'd like to contribute to this project, feel free to **fork** the repository, make your changes, and create a **pull request**. We’ll review and consider your contribution.
