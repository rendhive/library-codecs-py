import codecs

original_text = "Hello, world!"
encoded_text = codecs.encode(original_text, 'ascii')

print("Teks setelah encoding ke ASCII:", encoded_text)
# Fungsi: Mengencoding string menjadi format ASCII.
# Kondisi: Ketika Anda perlu memastikan teks hanya menggunakan karakter ASCII.
