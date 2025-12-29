import codecs

original_text = "Hello, world!"
encoded_text = codecs.encode(original_text, 'utf-8')

print("Teks setelah encoding ke UTF-8:", encoded_text)
# Fungsi: Mengencoding string menjadi format UTF-8.
# Kondisi: Ketika Anda perlu menyimpan atau mengirim teks dalam format UTF-8.
