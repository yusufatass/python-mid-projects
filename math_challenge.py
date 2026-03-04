import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    # String birleştirme yerine f-string kullanmak çok daha okunabilirdir
    expression = f"{left} {operator} {right}"
    answer = eval(expression)
    return expression, answer


wrong = 0
input("Press enter to START...")
print("-----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()

    guess = input(f"Problem #{i + 1}: {expression} = ")

    if guess == str(answer):
        print("✅ Doğru!\n")
    else:
        # Hem yanlış olduğunu söylüyoruz hem de doğru cevabı gösteriyoruz
        print(f"❌ Yanlış! Doğru cevap {answer} olacaktı.\n")
        wrong += 1  # Yanlış sayacını 1 artırıyoruz

end_time = time.time()
total_time = round(end_time - start_time, 2)

# Toplam sorudan yanlışları çıkararak doğru sayısını buluyoruz
correct_answers = TOTAL_PROBLEMS - wrong

print("-----------------------")
print("Oyun Bitti!")
print(f"Skor: {TOTAL_PROBLEMS} soruda {correct_answers} doğru, {wrong} yanlış.")
print(f"Süre: {total_time} saniye sürdü.")