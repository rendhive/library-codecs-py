import codecs

special_chars = "© 2023"
encoded = codecs.encode(special_chars, 'utf-8')

print("Encoded special characters:", encoded)
# Fungsi: Mengencoding karakter khusus.
# Kondisi: Ketika Anda perlu memastikan karakter khusus dapat disimpan dengan benar.
