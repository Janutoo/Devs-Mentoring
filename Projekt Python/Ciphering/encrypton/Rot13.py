from Rot import RotCipher

class Rot13Cipher(RotCipher):
    def encrypt(self, text):
        result = ''
        for char in text:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                result += char
        return result

    def decrypt(self, text):
        return self.encrypt(text)
