import codecs

# Menulis ke file dengan encoding UTF-8
with codecs.open('example.txt', 'w', 'utf-8') as f:
    f.write("Hello, world!")

# Membaca kembali dari file
with codecs.open('example.txt', 'r', 'utf-8') as f:
    content = f.read()

print("Isi file:", content)
# Fungsi: Membaca dan menulis file dengan encoding tertentu.
# Kondisi: Ketika Anda ingin memastikan file teks menggunakan encoding yang benar.
