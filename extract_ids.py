import json
import os

FILE_PATHS = ['comments.json', 'channel.json']

# Список головних підозрюваних (Адмін, Боти та Штатні Хейтери/Піарники)
TARGET_SUSPECTS = [
    "Пластична хірургія Україна| Реальні відгуки",
    "Юлі Я🍒",
    "Kate Chyzhova",
    "Oksana Savienkova",
    "Darinochka",
    "𝓨𝓾𝓵𝓲𝔂𝓪",
    "Alina Khantil",
    "Sunny",
    "Tetiana 💛💙",
    "Hanna Omelyanchuk",
    "KB",
    "Kseniia Udovichenko",
    "Наталія Корнієнко",
    "Анна",
    "Elena",
    "Н",
    "Svitlana Bondarenko"
]

def main():
    print("🔍 ЗАПУСК ПРОТОКОЛУ ДЕАНОНІМІЗАЦІЇ: ВИТЯГ УНІКАЛЬНИХ ТЕЛЕГРАМ ID...")
    
    suspect_ids = {}

    for file_path in FILE_PATHS:
        if not os.path.exists(file_path):
            continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Помилка читання {file_path}: {e}")
            continue

        for msg in data.get('messages', []):
            if msg.get('type') != 'message': continue
            
            raw_user = msg.get('from', '')
            user_id = msg.get('from_id', '')
            
            if raw_user in TARGET_SUSPECTS and user_id:
                # Телеграм часто записує ID у форматі 'user123456789'. Прибираємо префікс для чистого ID
                clean_id = str(user_id).replace('user', '').replace('channel', '').strip()
                if clean_id not in [uid for _, uid in suspect_ids.items()]:
                    suspect_ids[raw_user] = clean_id

    print("\n" + "="*70)
    print(" 📂 СПРАВА №190: ЦИФРОВІ ІДЕНТИФІКАТОРИ ФІГУРАНТІВ (TELEGRAM ID)")
    print("="*70)
    
    if not suspect_ids:
        print("❌ Жодного ID не знайдено. Перевірте наявність файлів.")
    else:
        for i, (name, uid) in enumerate(suspect_ids.items()):
            print(f" [{i+1}] Нікнейм: {name}")
            print(f"     ➔ Унікальний ID: {uid}")
            # Це системне посилання дозволяє перейти на профіль людини навіть якщо вона змінила нік
            print(f"     ➔ Deep Link для пробиву: tg://user?id={uid}")
            print("-" * 70)
            
    print("\n🚨 ІНСТРУКЦІЯ ДЛЯ ОПЕРАТИВНИКІВ:")
    print("1. Отримані числові ID є незмінними.")
    print("2. Передайте ці ID у відділ кіберрозвідки для звірки з базами даних (LeakOSINT).")
    print("3. Порівняйте отримані номери телефонів з номерами адміністраторів клінік та PR-агентств.")

if __name__ == "__main__":
    main()