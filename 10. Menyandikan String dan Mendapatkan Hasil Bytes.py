import codecs

original_text = "Hello!"
encoded_bytes = codecs.encode(original_text, 'utf-8')

print("Bytes setelah di-encode:", list(encoded_bytes))
# Fungsi: Mendapatkan byte hasil dari string setelah encoding.
# Kondisi: Ketika Anda ingin memeriksa representasi byte dari string.
