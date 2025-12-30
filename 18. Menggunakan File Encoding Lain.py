import codecs

# Menulis data dengan encoding UTF-16
with codecs.open('utf16_example.txt', 'w', 'utf-16') as f:
    f.write("Hello, world!")

# Membaca kembali dari file
with codecs.open('utf16_example.txt', 'r', 'utf-16') as f:
    content = f.read()
    
print("Isi file dengan UTF-16:", content)
# Fungsi: Menyimpan dan membaca file dengan encoding yang berbeda.
# Kondisi: Ketika Anda ingin menjaga kesetiaan data dalam format tertentu.
