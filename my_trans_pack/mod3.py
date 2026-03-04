from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs
import deep_translator.constants as dt_const

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        # deep_translator використовує 'auto' за замовчуванням
        source_lang = 'auto' if scr == 'auto' else scr
        translated = GoogleTranslator(source=source_lang, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        # detect_langs повертає список об'єктів з мовою та ймовірністю
        langs = detect_langs(text)
        best_match = langs[0] # Беремо найбільш ймовірний варіант
        
        if set == "lang":
            return best_match.lang
        elif set == "confidence":
            return str(round(best_match.prob, 2))
        else:
            return f"Language: {best_match.lang}, Confidence: {round(best_match.prob, 2)}"
    except Exception as e:
        return f"Error: {str(e)}"

def CodeLang(lang: str) -> str:
    try:
        langs = dt_const.GOOGLE_LANGUAGES_TO_CODES
        lang = lang.lower()
        
        # Якщо передали назву
        if lang in langs:
            return langs[lang]
            
        # Якщо передали код
        for name, code in langs.items():
            if code == lang:
                return name.capitalize()
                
        return "Error: Language not found."
    except Exception as e:
        return f"Error: {str(e)}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        langs = dt_const.GOOGLE_LANGUAGES_TO_CODES
        
        header = f"{'N':<4} {'Language':<15} {'ISO-639 code':<15} {'Text' if text else ''}"
        separator = "-" * len(header)
        table_lines = [header, separator]
        
        n = 1
        for name, code in langs.items():
            translated_text = ""
            if text:
                try:
                    translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                except:
                    translated_text = "Error"
                    
            line = f"{n:<4} {name.capitalize():<15} {code:<15} {translated_text}"
            table_lines.append(line.strip())
            n += 1
            
        result_text = "\n".join(table_lines) + "\nOk"
        
        if out == "screen":
            print(result_text)
        elif out == "file":
            with open("language_list_mod3.txt", "w", encoding="utf-8") as f:
                f.write(result_text)
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
