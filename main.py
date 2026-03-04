import random

# --- (CONSTANTS) ---
MAX_LINES = 3
MIN_DEPOSIT = 5
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Sembollerin torbada bulunma oranları
SYMBOL_COUNT = {
    "A": 2,  # En nadir (En değerli)
    "B": 4,
    "C": 6,
    "D": 8  # En yaygın (En az değerli)
}

# Sembollerin kazanç çarpanları
SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Oynanan satırlardaki (lines) sembollerin aynı olup olmadığını kontrol eder.
    Kazancı ve kazandıran satırları döndürür.
    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        # Bütün sütunlardaki ilgili satıra (line) bakarız
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  # Eğer 'break' hiç çalışmazsa (yani hepsi aynıysa) bu blok çalışır
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Belirtilen sembol oranlarına göre rastgele bir slot matrisi oluşturur.
    """
    all_symbols = []

    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = []
        # all_symbols listesinin bir kopyasını ([:]) alıyoruz ki orijinali bozulmasın
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Sütun tabanlı matrisi yatay satırlar halinde ekrana yazdırır.
    """
    print("\n" + "=" * 13)
    # len(columns[0]) bize satır sayısını verir
    for row in range(len(columns[0])):
        # Python'un list comprehension yeteneği ile o satırdaki tüm elemanları çekiyoruz
        row_items = [column[row] for column in columns]
        # Elemanların arasına " | " koyarak string olarak birleştiriyoruz
        print(" | ".join(row_items))
    print("=" * 13 + "\n")


def deposit():
    while True:
        # Kullanıcıya minimum tutarı da input içinde belirtiyoruz
        amount = input(f"How much do you want to deposit? (Min ${MIN_DEPOSIT}): $").strip()

        if amount.isdigit():
            amount = int(amount)
            #MIN_DEPOSIT'ten büyük veya eşit mi
            if amount >= MIN_DEPOSIT:
                break
            else:
                print(f"⚠️ Amount must be at least ${MIN_DEPOSIT}.")
        else:
            print("❌ Please enter a valid number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ").strip()
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a valid number of lines (1-{MAX_LINES}).")
        else:
            print("Please enter a valid number.")
    return lines


def get_bets():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET} - ${MAX_BET}): ").strip()
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}!")
        else:
            print("Please enter a valid number.")
    return amount


def spin(balance):

    # Bakiye kontrolü için mantığı tek bir while döngüsü
    while True:
        lines = get_number_of_lines()
        bet = get_bets()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"❌ You don't have enough money! Your current balance is ${balance}.")
            print("Please lower your bet or number of lines.\n")
        else:
            break

    print(f"\n💸 You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)

    if winnings > 0:
        print(f"🎉 YOU WON ${winnings}!")
        # *winning_lines ile listeyi [1, 2] yerine temiz bir şekilde 1 2 diye yazdırıyoruz
        print(f"🎯 You won on line(s):", *winning_lines)
    else:
        print("😢 You didn't win anything this time.")

    # Net kazancı/kayıp
    return winnings - total_bet


# ==========================================
# ANA UYGULAMA DÖNGÜSÜ
# ==========================================

def main():
    print("🎰 WELCOME TO THE PYTHON CASINO 🎰\n")
    balance = deposit()

    while True:
        print("-" * 30)
        print(f"💰 Current balance: ${balance}")

        # Eğer para bittiyse oyunu otomatik bitir
        if balance <= 0:
            print("💸 You are out of money! Game over.")
            break

        answer = input("Press ENTER to spin (or 'q' to quit): ").strip().lower()
        if answer == "q":
            break

        balance += spin(balance)

    print("-" * 30)
    print(f"🚶 You left the casino with ${balance}.")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()