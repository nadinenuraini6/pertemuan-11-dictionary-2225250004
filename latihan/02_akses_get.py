data = {"nama": "Ayu", "nilai": 85} 
# Latihan 2: Akses Aman dengan get()
# Pertemuan 11 - Algoritma dan Pemrograman

data = {"nama": "Ayu", "nilai": 85}

# Mengakses value key yang tersedia
print(data.get("nama"))

# Mengakses key yang tidak tersedia (mengembalikan None secara default)
print(data.get("kelas"))

# Mengakses key yang tidak tersedia dengan nilai default kustom
print(data.get("kelas", "Belum ada"))