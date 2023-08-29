import deepl

class DeepLTranslate():
    def __init__(self):
        self.auth_key = "ここにご自身の認証キーを入力してください"
        self.translator = deepl.Translator(self.auth_key)
    def translate(self, text, language):
        result = self.translator.translate_text(text, target_lang=language)
        return result.text