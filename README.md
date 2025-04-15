# StegaVision DWT - Steganografi dengan Discrete Wavelet Transform

## Deskripsi
**StegaVision DWT** adalah aplikasi steganografi yang menggunakan metode **Discrete Wavelet Transform (DWT)** untuk menyisipkan dan mengekstrak pesan rahasia di dalam gambar. Aplikasi ini memungkinkan pengguna untuk meng-encode pesan ke dalam gambar dan mendekode pesan tersebut menggunakan algoritma berbasis DWT. Steganografi adalah teknik untuk menyembunyikan informasi dalam bentuk yang tidak mudah terdeteksi oleh pihak ketiga.

### Fitur Utama:
- **Encode Pesan:** Sisipkan pesan rahasia ke dalam gambar PNG/JPG menggunakan DWT.
- **Decode Pesan:** Ekstrak pesan yang tersembunyi dari gambar stego.
- **Keamanan:** Pengguna dapat menambahkan password opsional untuk keamanan ekstra dalam proses encoding dan decoding.
- **Antarmuka Pengguna:** Antarmuka yang mudah digunakan dengan Streamlit untuk pengalaman interaktif yang baik.

## Prasyarat
Aplikasi ini membutuhkan beberapa paket Python untuk menjalankan fungsionalitas steganografi dan antarmuka pengguna:

- `streamlit`: Untuk antarmuka pengguna web.
- `numpy`: Untuk komputasi numerik.
- `opencv-python`: Untuk manipulasi gambar.
- `Pillow`: Untuk pembacaan dan penulisan gambar.
- `stegano-dwt`: Modul untuk implementasi steganografi berbasis DWT.

## Cara Menggunakan

### Encode Pesan:
1. Pilih gambar cover (PNG/JPG) yang ingin Anda gunakan untuk menyisipkan pesan.
2. Masukkan pesan rahasia yang ingin Anda sembunyikan.
3. Pilih opsi untuk menambahkan password (opsional) untuk lapisan keamanan tambahan.
4. Klik tombol "🚀 Encode Pesan" untuk menyisipkan pesan.
5. Gambar hasil dengan pesan tersembunyi (stego image) akan ditampilkan. Anda dapat mengunduh gambar tersebut.

### Decode Pesan:
1. Pilih gambar stego yang berisi pesan rahasia.
2. Masukkan password jika ada.
3. Klik tombol "🕵️‍♂️ Ekstrak Pesan" untuk mengekstrak pesan rahasia dari gambar stego.
4. Pesan yang berhasil diekstrak akan ditampilkan di aplikasi.

## Instalasi

1. Clone repositori ini ke dalam komputer Anda:
   ```bash
   git clone https://github.com/Zeustika/StegaVision-DWT.git


1. Clone repositori ini ke dalam komputer Anda:
   ```bash
   git clone https://github.com/Zeustika/StegaVision-DWT.git
   ```
   
2. Masuk ke direktori proyek:
   ```bash
   cd StegaVision-DWT
   ```
   
3. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```

Aplikasi akan terbuka di browser Anda.

## Struktur Proyek
```
StegaVision-DWT/
│
├── app.py              # Aplikasi utama Streamlit
├── requirements.txt    # Daftar dependensi Python
├── .gitignore          # File untuk mengabaikan file yang tidak perlu di Git
└── README.md           # File ini
```

## Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buat **fork** repositori ini, lakukan perubahan, dan buat **pull request**. Kami akan meninjau dan mempertimbangkan kontribusi Anda.
