import codecs

# Menulis data biner ke file
binary_data = b'This is binary data.\x00\x01\x02'
with open('binary_file.bin', 'wb') as f:
    f.write(binary_data)

# Membaca data biner
with open('binary_file.bin', 'rb') as f:
    read_data = f.read()

print("Data biner dibaca:", read_data)
# Fungsi: Menangani file biner dengan penulisan dan pembacaan.
# Kondisi: Ketika Anda ingin menyimpan dan memuat data dalam format biner.
