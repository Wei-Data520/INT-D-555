class AdvancedTextCleaner:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        import string
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))

    def lowercase(self):
        self.text = self.text.lower()

    def remove_whitespace(self):
        self.text = ' '.join(self.text.split())

    def clean(self):
        self.remove_punctuation()
        self.lowercase()
        self.remove_whitespace()
        return self.text

# Example usage:
# cleaner = AdvancedTextCleaner("Hello, World! This is a test.")
# cleaned_text = cleaner.clean()
# print(cleaned_text)  # Output: "hello world this is a test"