import codecs

data = b'\x00\xff\xfe\xfd'
decoded_data = codecs.decode(data, 'utf-8', errors='ignore')  # Mengabaikan kesalahan

print("Decoded binary data:", decoded_data)
# Fungsi: Menggunakan codecs untuk mendekode data biner.
# Kondisi: Ketika Anda ingin membuang karakter yang tidak valid dari data biner.
