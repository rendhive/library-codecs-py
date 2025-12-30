import codecs

# Mengencoding karakter yang tidak terdefinisi dengan penanganan kesalahan
try:
    bad_data = b'\x80'
    decoded_data = codecs.decode(bad_data, 'utf-8')
except UnicodeDecodeError:
    print("Karakter tidak dapat didekode.")
# Fungsi: Menangani kesalahan saat mendekode data yang tidak valid.
# Kondisi: Ketika Anda berurusan dengan data yang mungkin rusak atau tidak valid.
