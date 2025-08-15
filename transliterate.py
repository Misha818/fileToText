# transliterate.py
# Simple Arabic to Latin transliteration

# This is a basic map, you can extend it or use a library like `arabic-reshaper` + `python-bidi`
TRANSLIT_MAP = {
    "ا": "a", "ب": "b", "ت": "t", "ث": "th", "ج": "j", "ح": "h",
    "خ": "kh", "د": "d", "ذ": "dh", "ر": "r", "ز": "z", "س": "s",
    "ش": "sh", "ص": "s", "ض": "d", "ط": "t", "ظ": "z", "ع": "a",
    "غ": "gh", "ف": "f", "ق": "q", "ك": "k", "ل": "l", "م": "m",
    "ن": "n", "ه": "h", "و": "w", "ي": "y", "ء": "'", "ى": "a",
}

def transliterate_text(arabic_text):
    latin_text = ""
    for char in arabic_text:
        latin_text += TRANSLIT_MAP.get(char, char)
    return latin_text

