import os

file_name = "story.txt"

# 1. Dosyanın var olup olmadığını kontrol eden güvenli bir yapı ekledik
if not os.path.exists(file_name):
    print(f"Error: The file '{file_name}' was not found.")
    exit()

with open(file_name, "r", encoding="utf-8") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# 2. Kelimeleri bulma döngüsü
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

print("\n" + "="*30)
print("🎩 WELCOME TO MAD LIBS! 🎩")
print("="*30 + "\n")

# 3. Kullanıcıdan veri alırken ekranda < > işaretlerini gizleyip daha şık gösteriyoruz
for word in words:
    # .strip("<>") metodu baştaki ve sondaki okları siler (sadece ekranda güzel görünmesi için)
    clean_word = word.strip("<>")
    answer = input(f"Enter a/an {clean_word}: ")
    answers[word] = answer

# 4. .items() kullanarak sözlükteki (dictionary) anahtar ve değerleri aynı anda çekiyoruz
for word, user_answer in answers.items():
    story = story.replace(word, user_answer)

print("\n" + "="*30)
print("📖 HERE IS YOUR STORY 📖")
print("="*30 + "\n")
print(story)
print("\n" + "="*30)