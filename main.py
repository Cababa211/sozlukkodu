sozluk = {
            "Esef": "Olmaması, yapılmaması gereken veya yapılamayan bir şey için duyurulan üzüntü",
            "Emin": "Güvenilir, Doğru",
            }
print(*sozluk)

kullanici_istek = input("Hangi Kelimenin Anlamını Öğrenmek İstiyorsunuz?")
    
if kullanici_istek in sozluk.keys():
    print(sozluk[kullanici_istek])
else:
    print("Bu kelime sözlükte bulunmuyor")
