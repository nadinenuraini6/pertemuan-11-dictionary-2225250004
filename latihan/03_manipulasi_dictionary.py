# Latihan 3: Manipulasi Dictionary
# Pertemuan 11 - Algoritma dan Pemrograman

data = {"nama": "Ayu", "nilai": 85}

# Menambah pasangan key-value baru
data["kelas"] = "A"

# Mengubah value dari key yang sudah ada
data["nilai"] = 90

print("Setelah ditambah dan diubah:", data)

# Menghapus pasangan key menggunakan pop() dan mengambil valuenya
kelas = data.pop("kelas")
print("Value kelas yang dihapus:", kelas)
print("Setelah pop:", data)