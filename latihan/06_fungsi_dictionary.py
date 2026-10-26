# Latihan 6: Fungsi Pencarian dalam Dictionary
# Pertemuan 11 - Algoritma dan Pemrograman

def cari(data, nim):
    """Fungsi untuk mencari data berdasarkan NIM secara aman menggunakan get()."""
    return data.get(nim, "Data tidak ditemukan")

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}

# Uji pencarian data yang tersedia dan tidak tersedia
print(cari(mahasiswa, "A002"))
print(cari(mahasiswa, "A003"))