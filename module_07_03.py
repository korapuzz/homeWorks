class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        removed_symbols = (',', '.', '=', '!', '?', ';', ':', ' - ')

        for file in self.file_names:
            with open(file, 'r', encoding = "utf-8") as f:
                text = f.read().lower()

                for char in removed_symbols:
                    text = text.replace(char, "")

                all_words[f] = text.split()

    def find(self, word):
        word = word.lower()
        word_positions = {}

        for name, words in self.get_all_words().items():
            if word in words:
                word_positions[name] = words.find(word) + 1

        return word_positions

    def count(self, word):
        word = word.lower()

        word_count = {}

        for name, words in self.get_all_words().items():
            word_count[name] = words.count(word)

        return word_count


d = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
d.get_all_words()
