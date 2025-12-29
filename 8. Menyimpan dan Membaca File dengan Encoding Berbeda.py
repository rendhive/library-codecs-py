import codecs

# Menyimpan file dengan encoding Latin-1
with codecs.open('latin_example.txt', 'w', 'latin-1') as f:
    f.write("Café")

# Membaca file dengan encoding Latin-1
with codecs.open('latin_example.txt', 'r', 'latin-1') as f:
    content = f.read()

print("Isi file dengan encoding Latin-1:", content)
# Fungsi: Menyimpan dan membaca file dengan encoding tertentu.
# Kondisi: Ketika Anda bekerja dengan file yang memerlukan encoding khusus.
