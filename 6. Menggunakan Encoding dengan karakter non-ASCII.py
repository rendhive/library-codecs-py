import codecs

original_text = "Café"
encoded_text = codecs.encode(original_text, 'utf-8')
print("Teks setelah encoding ke UTF-8:", encoded_text)

# Mendekode kembali
decoded_text = codecs.decode(encoded_text, 'utf-8')
print("Teks setelah decoding dari UTF-8:", decoded_text)
# Fungsi: Menangani karakter non-ASCII dengan encoding dan decoding.
# Kondisi: Ketika Anda perlu bekerja dengan karakter beraksen atau simbol khusus.
