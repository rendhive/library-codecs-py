import codecs

text = "Hello, world!"
encoded_utf8 = codecs.encode(text, 'utf-8')
encoded_ascii = codecs.encode(encoded_utf8, 'ascii', errors='ignore')

print("Encoded ASCII:", encoded_ascii)
# Fungsi: Encode dua kali dengan encoding berbeda.
# Kondisi: Ketika Anda perlu mengubah format encoding secara bertahap.
