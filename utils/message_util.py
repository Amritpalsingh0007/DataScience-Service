import re

class MessageUtil:
    def __ini__(self):
        words_to_card = ['spent', 'card', 'bank']
        self.pattern = r'\b(?:'+ "|".join(re.escape(word) for word in words_to_card) + r')\b'
    def isBankSms(self, message:str):
        return bool(re.search(self.pattern, message, flags=re.IGNORECASE))