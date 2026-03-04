import json
import os
import re
from my_trans_pack import mod1, mod2, mod3

def main():
    # 1. Читання конфігураційного файлу
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Помилка читання config.json: {e}")
        return

    filename = config.get("filename")
    target_lang = config.get("target_lang")
    module_name = config.get("module")
    output_dest = config.get("output", "screen")
    max_chars = config.get("max_chars", float('inf'))
    max_words = config.get("max_words", float('inf'))
    max_sentences = config.get("max_sentences", float('inf'))

    # Перевірка наявності файлу з текстом
    if not os.path.exists(filename):
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return

    try:
        # I. Отримання інформації про файл
        file_size = os.path.getsize(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            full_text = f.read()

        char_count = len(full_text)
        words = full_text.split()
        word_count = len(words)
        # Простий поділ на речення (по крапці, знаку оклику чи питання)
        sentences = [s.strip() for s in re.split(r'[.!?]+', full_text) if s.strip()]
        sentence_count = len(sentences)

        # Вибір потрібного модуля динамічно
        active_mod = {'mod1': mod1, 'mod2': mod2, 'mod3': mod3}.get(module_name)
        if not active_mod:
            print("Помилка: Невідомий модуль у конфігурації (має бути mod1, mod2 або mod3).")
            return

        # Визначення мови (беремо перші 500 символів для швидкості)
        detected_lang_code = active_mod.LangDetect(full_text[:500], "lang")
        detected_lang_name = active_mod.CodeLang(detected_lang_code)

        print(f"Назва файлу: {filename}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість слів: {word_count}")
        print(f"Кількість речень: {sentence_count}")
        print(f"Мова тексту: {detected_lang_name} ({detected_lang_code})")
        print("-" * 40)

        # II. Зчитування тексту з урахуванням лімітів
        text_to_translate = ""
        cur_chars, cur_words, cur_sentences = 0, 0, 0

        for sentence in sentences:
            # Відновлюємо крапку, бо split її видалив (спрощено)
            sentence_with_punct = sentence + ". "
            s_words = len(sentence.split())
            s_chars = len(sentence_with_punct)

            if (cur_chars + s_chars > max_chars) or \
               (cur_words + s_words > max_words) or \
               (cur_sentences + 1 > max_sentences):
                break

            text_to_translate += sentence_with_punct
            cur_chars += s_chars
            cur_words += s_words
            cur_sentences += 1

        text_to_translate = text_to_translate.strip()
        
        if not text_to_translate:
            print("Помилка: Текст для перекладу порожній. Перевірте ліміти у конфігурації.")
            return

        # III. Переклад тексту
        translated_text = active_mod.TransLate(text_to_translate, detected_lang_code, target_lang)

        if translated_text.startswith("Error"):
            print(f"Помилка перекладу: {translated_text}")
            return

        # Визначаємо назву мови, на яку переклали (для виводу на екран)
        target_lang_name = active_mod.CodeLang(target_lang)
        if target_lang_name.startswith("Error"):
            target_lang_name = target_lang # Якщо це вже була назва

        # IV. Вивід на екран
        if output_dest == "screen":
            print(f"Мова перекладу: {target_lang_name}")
            print(f"Використаний модуль: {module_name}")
            print(f"\nПерекладений текст:\n{translated_text}")

        # V. Вивід у файл
        elif output_dest == "file":
            # Формуємо назву нового файлу
            target_code = target_lang
            if len(target_code) > 3: # Якщо передали назву ('english'), шукаємо код ('en')
                target_code = active_mod.CodeLang(target_lang)

            base_name, ext = os.path.splitext(filename)
            new_filename = f"{base_name}_{target_code}{ext}"
            
            with open(new_filename, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print("Ok")

        else:
            print("Помилка: Параметр 'output' у конфігурації має бути 'screen' або 'file'.")

    except Exception as e:
        print(f"Сталася критична помилка під час виконання програми: {e}")

if __name__ == "__main__":
    main()