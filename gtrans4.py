from my_trans_pack import mod1, NAME, AUTHOR

print("="*40)
print(f"Демонстрація пакету: {NAME}")
print(f"Розробник: {AUTHOR}")
print("="*40)

print("\n1. Тестування функції TransLate:")
print(f"Переклад 'Добрий день' (uk -> en): {mod1.TransLate('Добрий день', 'uk', 'en')}")

print("\n2. Тестування функції LangDetect:")
print(f"Визначення мови слова 'Bonjour': {mod1.LangDetect('Bonjour', 'all')}")
print(f"Тільки код мови: {mod1.LangDetect('Bonjour', 'lang')}")

print("\n3. Тестування функції CodeLang:")
print(f"Код для 'ukrainian': {mod1.CodeLang('ukrainian')}")
print(f"Назва для 'fr': {mod1.CodeLang('fr')}")

print("\n4. Тестування функції LanguageList (вивід на екран):")
mod1.LanguageList("screen", "Слава Україні!")
