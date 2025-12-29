import codecs

encoded_text = b'Hello, world!'
decoded_text = codecs.decode(encoded_text, 'ascii')

print("Teks setelah decoding dari ASCII:", decoded_text)
# Fungsi: Mendekode string dari format ASCII kembali ke string biasa.
# Kondisi: Ketika Anda menerima teks ASCII dan perlu mengkonversinya kembali.
