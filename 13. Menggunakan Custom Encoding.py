import codecs

def custom_encoder(data):
    return data[::-1]  # Membalikkan string sebagai contoh encoding kustom

codecs.register_error('custom_encoder', lambda e: (custom_encoder(e.object), e.end))

text = "Hello"
encoded_text = codecs.encode(text, 'custom_encoder')

print("Teks setelah custom encoding:", encoded_text)
# Fungsi: Menggunakan encoding kustom untuk memodifikasi string.
# Kondisi: Ketika Anda ingin melakukan modifikasi unik pada string.
