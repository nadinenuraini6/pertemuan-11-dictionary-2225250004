# Pertemuan 11 Dictionary/Map

Nama: Nadine Nur'Aini
NIM: 2225250004
Kelas: 3B

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value[cite: 12].

## Struktur Data
Jelaskan key utama dan value yang digunakan[cite: 12].
*(Contoh: Menggunakan NIM sebagai key utama, dengan value berupa dictionary bersarang yang memuat atribut nama, kelas, dan nilai).*

## Cara Menjalankan
```bash
python3 praktik/data_mahasiswa.py
```[cite: 12]

## Test Case
Catat input/aksi, hasil yang diharapkan, hasil aktual, dan status[cite: 12].
* **Pencarian tersedia (A003):** Data Citra ditampilkan | Status: Berhasil[cite: 11, 12]
* **Pencarian tidak tersedia (A999):** Pesan 'Data tidak ditemukan' | Status: Berhasil[cite: 11, 12]
* **Pembaruan nilai (A002):** Nilai A002 berubah menjadi 82 | Status: Berhasil[cite: 11, 12]
* **Penambahan data (A006):** Key A006 tersedia setelah ditambahkan | Status: Berhasil[cite: 11, 12]
* **Rekap (`items()`):** Semua NIM dan data tampil | Status: Berhasil[cite: 11, 12]

## Refleksi
Jelaskan satu kesalahan akses key yang ditemukan dan cara memperbaikinya[cite: 12].
*(Contoh: Sempat terjadi kesalahan saat mengakses key yang tidak ada menggunakan kurung siku `[]` yang memunculkan `KeyError`, lalu berhasil diperbaiki dengan menggunakan method `.get()` atau operator `in`).*