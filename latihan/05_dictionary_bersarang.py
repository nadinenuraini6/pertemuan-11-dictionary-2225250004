# Latihan 5: Dictionary Bersarang (Nested Dictionary)
# Pertemuan 11 - Algoritma dan Pemrograman

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

# Mengakses data bersarang menggunakan urutan key yang benar
print(mahasiswa["A001"]["nama"])
print(mahasiswa["A002"]["nilai"])