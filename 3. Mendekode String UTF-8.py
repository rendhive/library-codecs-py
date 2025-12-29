import codecs

encoded_text = b'Hello, world!'
decoded_text = codecs.decode(encoded_text, 'utf-8')

print("Teks setelah decoding dari UTF-8:", decoded_text)
# Fungsi: Mendekode string dari format UTF-8 kembali ke string biasa.
# Kondisi: Ketika Anda menerima teks dalam format biner dan perlu mengkonversinya kembali.
