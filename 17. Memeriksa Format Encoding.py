import codecs

text = "Sample text."
encoded_text = codecs.encode(text, 'utf-8')
decoded_text = codecs.decode(encoded_text, 'utf-8')

if text == decoded_text:
    print("Encoding dan decoding berhasil, teks cocok.")
else:
    print("Teks tidak cocok!")
# Fungsi: Memeriksa apakah encoding dan decoding berhasil.
# Kondisi: Ketika Anda perlu memverifikasi integritas data setelah proses encoding/decoding.
