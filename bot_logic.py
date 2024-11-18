from input_handler import hold_key  # Tuş işlemleri için import

def bot_action():
    """
    Botun ana döngüsü.
    - Belirli tuşlara sırasıyla basar ve bırakır.
    - Kullanıcı Ctrl+C ile döngüyü durdurabilir.
    """
    try:
        while True:  # Sonsuz döngü
            print("W tuşuna basılıyor...")
            hold_key(0x11, 3)  # 'W' tuşuna 3 saniye basılı tut
            print("W tuşu bırakıldı.")

            print("A tuşuna basılıyor...")
            hold_key(0x1E, 2)  # 'A' tuşuna 2 saniye basılı tut
            print("A tuşu bırakıldı.")

    except KeyboardInterrupt:
        # Kullanıcı Ctrl+C tuşuna bastığında döngü durur
        print("Bot manuel olarak durduruldu.")
