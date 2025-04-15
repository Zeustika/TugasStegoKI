import streamlit as st
import cv2
import numpy as np
from stegano_dwt import embed_message, extract_message
from PIL import Image
import io

st.set_page_config(page_title="StegaVision DWT", page_icon="🔒", layout="wide")

st.title("Tugas Steganografi dengan DWT")
st.markdown(""" 
    [*Muhamad Yustika Selamet*](https://github.com/Zeustika) , 
    [*Acep Tio*](https://www.linkedin.com/in/acep-tio-283006333/?originalSubdomain=id) ,     
    [*Alariq Ariq Mustafa*](https://simak.unsil.ac.id/us-unsil/foto/2023/237006166.jpg) ,
    [*Ikhsan Miftah Fauzan*](https://simak.unsil.ac.id/us-unsil/foto/2023/237006148.jpg) ,
    [*Rizky Afrianti*](https://www.linkedin.com/in/rizky-afrianti-a50048286/)         
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stMarkdown a {
        color: #ffffff;  /* Change to your desired color */
        text-decoration: none;  /* Optional: to remove the underline */
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

if menu == "Encode":
    st.header("🔐 Encode Pesan")
    st.markdown("Sisipkan pesan rahasia ke dalam gambar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_img = st.file_uploader("Pilih gambar cover (PNG/JPG)", 
                                      type=["png", "jpg", "jpeg"],
                                      accept_multiple_files=False,
                                      key="enc_upload")
        
        if uploaded_img:
            img = Image.open(uploaded_img)
            st.image(img, caption="Gambar Asli", use_container_width=True)
    
    with col2:
        message = st.text_area("Masukkan pesan rahasia", 
                             placeholder="Tulis pesan yang akan disembunyikan...",
                             height=150)
        
        password = st.text_input("Password (opsional)", 
                               type="password",
                               help="Untuk ekstra layer keamanan")
        
        if st.button("🚀 Encode Pesan", use_container_width=True):
            if uploaded_img and message:
                try:
                    img_array = np.array(Image.open(uploaded_img).convert('RGB'))
                    
                    with st.spinner("Menyisipkan pesan..."):
                        stego_img = embed_message(img_array.copy(), message)
                    
                    st.success("Pesan berhasil disisipkan!")
                    
                    # Display before/after comparison
                    col_before, col_after = st.columns(2)
                    with col_before:
                        st.image(img_array, caption="Sebelum", use_container_width=True)
                    with col_after:
                        st.image(stego_img, caption="Sesudah", use_container_width=True)
                    
                    # Save to bytes
                    img_bytes = cv2.imencode('.png', stego_img, 
                                           [cv2.IMWRITE_PNG_COMPRESSION, 0])[1].tobytes()
                    
                    # Download button
                    st.download_button(
                        label="💾 Download Gambar Stego",
                        data=img_bytes,
                        file_name="secret_image.png",
                        mime="image/png",
                        use_container_width=True
                    )
                    
                    # Show stats
                    st.info(f"""
                        - Ukuran asli: {uploaded_img.size / 1024:.2f} KB
                        - Ukuran stego: {len(img_bytes) / 1024:.2f} KB
                        - Panjang pesan: {len(message)} karakter
                        """)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            else:
                st.warning("Harap upload gambar dan masukkan pesan!")

elif menu == "Decode":
    st.header("🔍 Decode Pesan")
    st.markdown("Ekstrak pesan rahasia dari gambar stego")
    
    uploaded_stego = st.file_uploader("Pilih gambar stego", 
                                    type=["png", "jpg", "jpeg"],
                                    key="dec_upload")
    
    if uploaded_stego:
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(uploaded_stego, caption="Gambar Stego", use_container_width=True)
        
        with col2:
            password = st.text_input("Password (jika ada)", 
                                   type="password",
                                   key="dec_password")
            
            if st.button("🕵️‍♂️ Ekstrak Pesan", use_container_width=True):
                try:
                    img_array = np.array(Image.open(uploaded_stego).convert('RGB'))
                    
                    with st.spinner("Memproses gambar..."):
                        extracted = extract_message(img_array)
                    
                    if extracted:
                        st.success("Pesan berhasil diekstrak!")
                        st.text_area("Pesan rahasia", 
                                    value=extracted,
                                    height=150,
                                    key="extracted_msg")
                    else:
                        st.warning("Tidak ditemukan pesan atau gambar rusak")
                        
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(""" **Tugas KI 2025** """)
