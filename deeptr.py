from my_trans_pack import mod3, NAME, AUTHOR

print("="*40)
print(f"Демонстрація пакету (mod3 - deep_translator): {NAME}")
print(f"Розробник: {AUTHOR}")
print("="*40)

print("\n1. Тестування функції TransLate:")
print(f"Переклад 'Штучний інтелект' (uk -> en): {mod3.TransLate('Штучний інтелект', 'uk', 'en')}")

print("\n2. Тестування функції LangDetect:")
print(f"Визначення мови слова 'Hello': {mod3.LangDetect('Hello', 'all')}")

print("\n3. Тестування функції CodeLang:")
print(f"Код для 'english': {mod3.CodeLang('english')}")
print(f"Назва для 'pl': {mod3.CodeLang('pl')}")

print("\n4. Тестування функції LanguageList (вивід в файл):")
print("Результат роботи функції: ", mod3.LanguageList("file", "Робота працює"))
print("Перевірте створений файл language_list_mod3.txt");
