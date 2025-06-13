class TextManager:
    def __init__(self):
        self.text = ""

    def add_key(self, key):
        if key == "<":
            self.text = self.text[:-1]
        elif key == "_":
            self.text += " "
        else:
            self.text += key
        self.save_to_file()

    def get_text(self):
        return self.text

    def save_to_file(self):
        with open("Chip/outut.txt", "w", encoding="utf-8") as f:
            f.write(self.text)
