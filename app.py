import streamlit as st
import cv2
import numpy as np
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="StegaVision DWT", page_icon="🔒", layout="wide")

st.title("Tugas Steganografi dengan DWT")
st.markdown(""" 
    [*Muhamad Yustika Selamet*](https://github.com/Zeustika) , 
    [*Acep Tio*](https://github.com/aceptio) ,     
    [*Alariq Ariq Mustafa*](https://github.com/Alariqqq) ,
    [*Ikhsan Miftah Fauzan*](https://github.com/ikhsanmiftahhhh) ,
    [*Rizky Afrianti*](https://github.com/apiwss)         
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stMarkdown a {
        color: #ffffff;
        text-decoration: none;
    }
    .stDownloadButton button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    .stTextArea textarea {
        min-height: 150px;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Menu", ["Encode", "Decode"], index=0)

def encode_data(image, data):
    data = data + "$" 
    data_bin = ''.join(format(ord(char), '08b') for char in data)

    pixels = list(image.getdata())
    encoded_pixels = []

    index = 0
    for pixel in pixels:
        if index < len(data_bin):
            red_pixel = pixel[0]
            new_pixel = (red_pixel & 254) | int(data_bin[index])
            encoded_pixels.append((new_pixel, pixel[1], pixel[2]))
            index += 1
        else:
            encoded_pixels.append(pixel)

    return encoded_pixels

def decode_data(image):
    pixels = list(image.getdata())

    data_bin = ""
    for pixel in pixels:
        data_bin += bin(pixel[0])[-1]

    data = ""
    for i in range(0, len(data_bin), 8):
        byte = data_bin[i:i + 8]
        data += chr(int(byte, 2))
        if data[-1] == "$":
            break

    return data[:-1]

if menu == "Encode":
    st.header("🔐 Encode Pesan")
    st.markdown("Sisipkan pesan rahasia ke dalam gambar")

    col1, col2 = st.columns(2)
    with col1:
        uploaded_img = st.file_uploader(
            "Pilih gambar cover (PNG/JPG)", 
            type=["png", "jpg", "jpeg"],
            key="enc_upload"
        )
        if uploaded_img:
            try:
                img = Image.open(uploaded_img).convert("RGB")
                st.image(img, caption="Gambar Asli", use_container_width=True)
            except Exception:
                st.error("Gagal membuka gambar. Pastikan format gambar valid.")

    with col2:
        message = st.text_area(
            "Masukkan pesan rahasia", 
            placeholder="Tulis pesan yang akan disembunyikan...",
            height=150
        )
        password = st.text_input(
            "Password (opsional)", 
            type="password",
            help="Untuk ekstra layer keamanan"
        )

        if st.button("🚀 Encode Pesan", use_container_width=True):
            if uploaded_img and message.strip():
                try:
                    img_array = np.array(Image.open(uploaded_img).convert('RGB'))
                    img_pil = Image.open(uploaded_img).convert('RGB')
                    
                    with st.spinner("Menyisipkan pesan..."):
                        encoded_pixels = encode_data(img_pil, message.strip())
                        encoded_img = Image.new(img_pil.mode, img_pil.size)
                        encoded_img.putdata(encoded_pixels)
                        stego_img = np.array(encoded_img)

                    st.success("Pesan berhasil disisipkan!")

                    col_before, col_after = st.columns(2)
                    with col_before:
                        st.image(img_array, caption="Sebelum", use_container_width=True)
                    with col_after:
                        st.image(stego_img, caption="Sesudah", use_container_width=True)

                    buffered = BytesIO()
                    encoded_img.save(buffered, format="PNG")
                    img_bytes = buffered.getvalue()
                    
                    st.download_button(
                        label="💾 Download Gambar Stego",
                        data=img_bytes,
                        file_name="secret_image.png",
                        mime="image/png",
                        use_container_width=True
                    )

                    st.info(f"""
                        - Ukuran asli: {len(img_bytes) / 1024:.2f} KB  
                        - Ukuran stego: {len(img_bytes) / 1024:.2f} KB  
                        - Panjang pesan: {len(message)} karakter
                    """)
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
            else:
                st.warning("Harap upload gambar dan masukkan pesan!")

elif menu == "Decode":
    st.header("🔍 Decode Pesan")
    st.markdown("Ekstrak pesan rahasia dari gambar stego")

    uploaded_stego = st.file_uploader(
        "Pilih gambar stego", 
        type=["png", "jpg", "jpeg"],
        key="dec_upload"
    )

    if uploaded_stego:
        col1, col2 = st.columns(2)
        with col1:
            try:
                st.image(uploaded_stego, caption="Gambar Stego", use_container_width=True)
            except:
                st.error("Gagal memuat gambar stego")

        with col2:
            password = st.text_input(
                "Password (jika ada)", 
                type="password",
                key="dec_password"
            )
            if st.button("🕵️‍♂️ Ekstrak Pesan", use_container_width=True):
                try:
                    img_pil = Image.open(uploaded_stego).convert("RGB")
                    with st.spinner("Memproses gambar..."):
                        extracted = decode_data(img_pil)

                    if extracted:
                        st.success("Pesan berhasil diekstrak!")
                        st.text_area(
                            "Pesan rahasia", 
                            value=extracted,
                            height=150,
                            key="extracted_msg"
                        )
                    else:
                        st.warning("Tidak ditemukan pesan atau gambar rusak")
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")

st.markdown("---")
st.markdown("**Tugas KI 2025**")
