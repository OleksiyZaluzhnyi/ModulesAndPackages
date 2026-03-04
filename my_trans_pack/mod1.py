import googletrans

def TransLate(text: str, scr: str, dest: str) -> str:
    """Переклад тексту."""
    try:
        translator = googletrans.Translator()
        # Якщо передано 'auto', googletrans зрозуміє це як автоматичне визначення
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначення мови та коефіцієнта довіри."""
    try:
        translator = googletrans.Translator()
        result = translator.detect(text)
        
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return str(result.confidence)
        else: # "all"
            return f"Language: {result.lang}, Confidence: {result.confidence}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    """Повертає код за назвою або назву за кодом."""
    try:
        langs = googletrans.LANGUAGES
        lang = lang.lower()
        
        # Якщо передали код (наприклад 'uk')
        if lang in langs:
            return langs[lang].capitalize()
        
        # Якщо передали назву (наприклад 'ukrainian')
        for code, name in langs.items():
            if name.lower() == lang:
                return code
                
        return "Error: Language not found."
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Вивід таблиці підтримуваних мов."""
    try:
        langs = googletrans.LANGUAGES
        translator = googletrans.Translator()
        
        # Формування заголовка таблиці
        header = f"{'N':<4} {'Language':<15} {'ISO-639 code':<15} {'Text' if text else ''}"
        separator = "-" * len(header)
        table_lines = [header, separator]
        
        n = 1
        for code, name in langs.items():
            translated_text = ""
            if text:
                try:
                    translated_text = translator.translate(text, dest=code).text
                except:
                    translated_text = "Error translating"
            
            line = f"{n:<4} {name.capitalize():<15} {code:<15} {translated_text}"
            table_lines.append(line.strip())
            n += 1
            
        result_text = "\n".join(table_lines) + "\nOk"
        
        if out == "screen":
            print(result_text)
        elif out == "file":
            with open("language_list_mod1.txt", "w", encoding="utf-8") as f:
                f.write(result_text)
        else:
            return "Error: Invalid 'out' parameter."
            
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"