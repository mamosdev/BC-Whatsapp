# BC-Whatsapp
# WA Sender PPDB - Panduan Instalasi

Script ini digunakan untuk mengirim pesan WhatsApp secara otomatis kepada peserta PPDB berdasarkan data dari file Excel.

Script dibuat menggunakan **Python + Selenium** untuk mengontrol WhatsApp Web.

---

# 1. Persiapan Software

Pastikan komputer sudah memiliki software berikut:

### 1️⃣ Install Python

Download dan install Python dari:

https://www.python.org/downloads/

Saat instalasi **WAJIB centang**

```
Add Python to PATH
```

Setelah selesai, cek di terminal:

```
python --version
```

Jika muncul versi Python berarti instalasi berhasil.

---

# 2. Download Project

Letakkan semua file berikut dalam satu folder:

```
wa_sender_ppdb/
│
├── kirim_whatsapp.py
├── data.xlsx
└── README.md
```

---

# 3. Install Library Python

Buka **Command Prompt / Terminal**, lalu jalankan:

```
pip install pandas selenium tqdm openpyxl
```

Library yang akan terinstall:

* pandas → membaca file Excel
* selenium → otomatisasi browser
* tqdm → progress bar di terminal
* openpyxl → membaca file Excel format .xlsx

---

# 4. Siapkan File Excel

File harus bernama:

```
data.xlsx
```

Contoh format:

| Nama Lengkap | Telepon     | Status      |
| ------------ | ----------- | ----------- |
| Ahmad Fauzan | 08123456789 | Lulus       |
| Budi Santoso | 08129876543 | Tidak Lulus |

Catatan penting:

* Nomor boleh format `08xxxx` atau `628xxxx`
* Hanya data dengan **Status = Lulus** yang akan dikirim pesan

---

# 5. Menjalankan Script

Masuk ke folder project melalui terminal.

Contoh:

```
cd D:\PPDB\wa_sender
```

Kemudian jalankan:

```
python kirim_whatsapp.py
```

---

# 6. Login WhatsApp Web

Saat script berjalan akan muncul pesan:

```
Scan QR lalu tekan ENTER...
```

Langkah:

1. Scan QR menggunakan WhatsApp di HP
2. Tunggu sampai WhatsApp Web terbuka
3. Kembali ke terminal
4. Tekan **ENTER**

Script akan mulai mengirim pesan otomatis.

---

# 7. Progress Pengiriman

Terminal akan menampilkan progress seperti ini:

```
Total target: 86

 45%|██████████████      | 39/86
```

Contoh log:

```
✓ Terkirim: Ahmad Fauzan
✓ Terkirim: Rafi Pratama
✗ Gagal: 62812345678
```

---

# 8. Hasil Log

Setelah selesai, script akan membuat file:

```
sukses.xlsx
gagal.xlsx
```

### sukses.xlsx

Berisi daftar nomor yang berhasil dikirim.

### gagal.xlsx

Berisi nomor yang gagal dikirim.

---

# 9. Tips Penggunaan Aman

Agar akun WhatsApp tidak diblokir:

* gunakan delay minimal **6 detik**
* maksimal kirim **300 pesan per jam**
* gunakan akun WhatsApp yang aktif

---

# 10. Troubleshooting

### Error: No module named 'pandas'

Jalankan:

```
pip install pandas
```

---

### Error: No module named 'tqdm'

Jalankan:

```
pip install tqdm
```

---

### Pesan tidak terkirim otomatis

Pastikan:

* WhatsApp Web sudah terbuka
* sudah menekan **ENTER setelah scan QR**

---

# 11. Catatan

Script ini hanya membantu proses pengiriman pesan kepada peserta PPDB dan tetap harus digunakan secara bijak.
