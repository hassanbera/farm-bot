from bot_logic import bot_action  # Botun ana döngüsünü içe aktarır

if __name__ == "__main__":
    """
    Ana program giriş noktası.
    Botu başlatır ve sonsuz döngüyü çalıştırır.
    """
    print("Bot çalışıyor... Ctrl+C ile durdurabilirsiniz.")  # Kullanıcıya bilgi ver
    bot_action()  # Botun ana döngüsünü çalıştır
