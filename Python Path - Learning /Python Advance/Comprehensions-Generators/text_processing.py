text = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet"

words = text.split()
length_of_words = [len(word.strip(".,—")) for word in words if word.lower() != "the"]
print(length_of_words)