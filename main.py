import requests
import random
import time
import os

LETTER_SET = "xzyvnraoelk"
MIN_LEN = 3
MAX_LEN = 4
TOTAL_TRIES = 200
DELAY = 0.6

CHECKED_FILE = "checked.txt"
OUTPUT_FILE = "rare_available.txt"

# Daha önce kontrol edilenleri yükle
checked = set()
if os.path.exists(CHECKED_FILE):
    with open(CHECKED_FILE, "r", encoding="utf-8") as f:
        checked = set(line.strip() for line in f if line.strip())

def generate_name():
    while True:
        length = random.randint(MIN_LEN, MAX_LEN)
        name = "".join(random.choice(LETTER_SET) for _ in range(length)).capitalize()
        if name not in checked:
            return name

def check_name(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    r = requests.get(url, timeout=10)
    if r.status_code == 204:
        return "AVAILABLE"
    elif r.status_code == 200:
        return "TAKEN"
    else:
        return "ERROR"

available = []

print(f"{len(checked)} isim daha önce kontrol edilmiş.")
print(f"{TOTAL_TRIES} yeni isim üretilecek...\n")

for _ in range(TOTAL_TRIES):
    name = generate_name()
    status = check_name(name)

    checked.add(name)
    with open(CHECKED_FILE, "a", encoding="utf-8") as f:
        f.write(name + "\n")

    if status == "AVAILABLE":
        print(f"[✓] {name} → BOŞ")
        available.append(name)
    elif status == "TAKEN":
        print(f"[✗] {name} → dolu")
    else:
        print(f"[!] {name} → hata")

    time.sleep(DELAY)

# Boş olanları kaydet
with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    for n in available:
        f.write(n + "\n")

print("\nBitti!")
print(f"Toplam boş bulunan: {len(available)}")
print("Kontrol edilen isimler bir daha ASLA kontrol edilmeyecek.")
