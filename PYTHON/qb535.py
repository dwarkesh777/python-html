class WordPlay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        return [w for w in self.words if len(w) == length]

    def starts_with(self, char1):
        return [w for w in self.words if w.startswith(char1)]

    def ends_with(self, char2):
        return [w for w in self.words if w.endswith(char2)]

    def palindromes(self):
        return [w for w in self.words if w == w[::-1]]

    def only(self, str1):
        return [w for w in self.words if all(c in str1 for c in w)]

    def avoids(self, str2):
        return [w for w in self.words if not any(c in str2 for c in w)]

# Example usage
if __name__ == "__main__":
    words = ['apple', 'banana', 'find', 'dictionary', 'set', 'tuple', 'list', 'malayalam', 'nayan', 'grind', 'apricot']
    wp = WordPlay(words)

    print("Words with length 5:", wp.words_with_length(5))
    print("Words starting with 'a':", wp.starts_with('a'))
    print("Words ending with 'd':", wp.ends_with('d'))
    print("Palindromes:", wp.palindromes())
    print("Words only with letters in 'bna':", wp.only('bna'))
    print("Words avoiding letters in 'amkd':", wp.avoids('amkd'))
