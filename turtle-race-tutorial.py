import time
import turtle
import random

# --- SABİTLER (CONSTANTS) ---
WIDTH, HEIGHT = 800, 600
# 'pink' rengi iki kez yazılmıştı, biri 'cyan' olarak değiştirildi
COLORS = ["red", "blue", "green", "yellow", "orange", "brown", "pink", "black", "cyan", "purple"]


def get_number_of_racers():
    """Kullanıcıdan geçerli bir yarışçı sayısı (2-10) alır."""
    while True:
        racers = input("Enter the number of racers (2-10): ").strip()
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("⚠️ Please enter a number between 2 and 10.")
        else:
            print("❌ Input is not valid. Please enter a number.")


def create_turtles(colors):
    """Belirtilen renklere göre kaplumbağaları oluşturup başlangıç çizgisine dizer."""
    turtles = []
    # Ekran genişliğini kaplumbağa sayısına bölerek eşit aralıklar hesaplıyoruz
    spacingx = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)  # Yukarıya (Kuzey'e) bakmalarını sağla

        # Çizgi çizmemeleri için kalemi kaldır, yerine geç, kalemi indir
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()

        turtles.append(racer)

    return turtles  # EKSİK OLAN KRİTİK SATIR EKLENDİ!


def race(turtles):
    """Kaplumbağaları rastgele hızlarda hareket ettirir, ilk bitirenin rengini döndürür."""
    while True:
        for racer in turtles:
            # 1 ile 20 piksel arası rastgele ileri git
            distance = random.randrange(1, 20)
            racer.forward(distance)

            # racer.ycor() metodu, nesnenin dikey (Y) eksenindeki tam konumunu verir
            if racer.ycor() >= HEIGHT // 2 - 10:
                # Kazanan kaplumbağanın rengini doğrudan döndürüyoruz
                return racer.pencolor()


def init_turtle():
    """Oyun ekranını başlatır ve ayarlar."""
    window = turtle.Screen()
    window.setup(WIDTH, HEIGHT)
    window.title("🐢 Python Turtle Racing Championship 🐢")
    return window


# ==========================================
# ANA UYGULAMA DÖNGÜSÜ
# ==========================================
def main():
    print("🏁 Welcome to Turtle Racing! 🏁\n")

    racers = get_number_of_racers()
    window = init_turtle()

    # random.sample(), bir listeden benzersiz rastgele elemanlar seçer
    selected_colors = random.sample(COLORS, racers)

    # Kaplumbağaları sahaya diz
    turtles = create_turtles(selected_colors)

    # Yarış öncesi heyecanlı geri sayım (Terminalde)
    print("\nGet ready...")
    time.sleep(1)
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("GO! 🚀\n")

    # Yarışı başlat ve kazananı al
    winner = race(turtles)

    print("-" * 30)
    print(f"🏆 The winner is the {winner.upper()} turtle! 🏆")
    print("-" * 30)

    # Yarış bitince ekranın hemen kapanmasını engeller, tıklayana kadar bekler
    window.exitonclick()


if __name__ == "__main__":
    main()