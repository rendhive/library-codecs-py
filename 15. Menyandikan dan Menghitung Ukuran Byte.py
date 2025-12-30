import codecs

text = "Hello, 世界"
encoded_text = codecs.encode(text, 'utf-8')

print("Ukuran byte dari encoded text:", len(encoded_text))
# Fungsi: Menghitung ukuran byte setelah encoding.
# Kondisi: Ketika Anda ingin mengecek ukuran teks setelah di-encode.
