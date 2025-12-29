import codecs

original_text = "Hello, world!"
encoded_text = codecs.encode(original_text, 'utf-16')

print("Teks setelah encoding ke UTF-16:", encoded_text)

decoded_text = codecs.decode(encoded_text, 'utf-16')
print("Teks setelah decoding dari UTF-16:", decoded_text)
# Fungsi: Mengencoding dan mendekode string UTF-16.
# Kondisi: Ketika Anda ingin menyimpan data dalam format UTF-16.
