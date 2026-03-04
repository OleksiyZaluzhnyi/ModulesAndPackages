from my_trans_pack import mod2, NAME, AUTHOR

print("="*40)
print(f"Демонстрація пакету (mod2 - googletrans 3.1.0a0): {NAME}")
print(f"Розробник: {AUTHOR}")
print("="*40)

print("\n1. Тестування функції TransLate:")
print(f"Переклад 'Привіт, світе' (uk -> de): {mod2.TransLate('Привіт, світе', 'uk', 'de')}")

print("\n2. Тестування функції LangDetect:")
print(f"Визначення мови слова 'Guten Tag': {mod2.LangDetect('Guten Tag', 'all')}")

print("\n3. Тестування функції CodeLang:")
print(f"Код для 'german': {mod2.CodeLang('german')}")
print(f"Назва для 'es': {mod2.CodeLang('es')}")

print("\n4. Тестування функції LanguageList (вивід на екран):")
mod2.LanguageList("screen", "Тестування")
