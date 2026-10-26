# Program Sistem Data Mahasiswa menggunakan Dictionary
# Pertemuan 11 - Algoritma dan Pemrograman

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM secara aman menggunakan get()."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai dari seluruh mahasiswa dalam dictionary."""
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# 1. Inisialisasi dictionary data mahasiswa dengan NIM sebagai key utama
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== DATA AWAL MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Info: {info}")
print("-" * 40)

# 2. Uji Pencarian Mahasiswa (Test Case: Tersedia dan Tidak Tersedia)
print("=== UJI PENCARIAN ===")
nim_cari_1 = "A003"
hasil_1 = cari_mahasiswa(data_mahasiswa, nim_cari_1)
if hasil_1 is not None:
    print(f"Pencarian {nim_cari_1}: Data {hasil_1['nama']} ditemukan -> {hasil_1}")
else:
    print(f"Pencarian {nim_cari_1}: Data tidak ditemukan")

nim_cari_2 = "A999"
hasil_2 = cari_mahasiswa(data_mahasiswa, nim_cari_2)
if hasil_2 is not None:
    print(f"Pencarian {nim_cari_2}: {hasil_2}")
else:
    print(f"Pencarian {nim_cari_2}: Data tidak ditemukan")
print("-" * 40)

# 3. Penambahan Mahasiswa Baru (A006)
print("=== MENAMBAH MAHASISWA BARU (A006) ===")
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print(f"Key A006 berhasil ditambahkan: {data_mahasiswa['A006']}")
print("-" * 40)

# 4. Pembaruan Nilai Mahasiswa (A002 diubah menjadi 82)
print("=== MEMPERBARUI NILAI MAHASISWA ===")
if "A002" in data_mahasiswa:
    data_mahasiswa["A002"]["nilai"] = 82
    print(f"Nilai A002 (Budi) diperbarui menjadi: {data_mahasiswa['A002']['nilai']}")
print("-" * 40)

# 5. Menampilkan Seluruh Data Menggunakan items() (Rekap)
print("=== REKAP SELURUH DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(f"NIM {nim} -> Nama: {info['nama']}, Kelas: {info['kelas']}, Nilai: {info['nilai']}")
print("-" * 40)

# 6. Menghitung dan Menampilkan Rata-rata Nilai Seluruh Mahasiswa
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai kelas = {rata_rata:.2f}")