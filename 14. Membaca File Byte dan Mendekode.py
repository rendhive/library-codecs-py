import codecs

# Menulis data biner ke file
with open('binary_data.bin', 'wb') as f:
    f.write(b'\x50\x79\x74\x68\x6f\x6e')

# Membaca data biner dari file dan mendekode
with codecs.open('binary_data.bin', 'rb') as f:
    binary_content = f.read()
    decoded_binary = codecs.decode(binary_content, 'utf-8', errors='ignore')

print("Decoded binary content:", decoded_binary)
# Fungsi: Membaca file biner dan mendekode konten.
# Kondisi: Ketika Anda bekerja dengan file yang menyimpan data biner.
