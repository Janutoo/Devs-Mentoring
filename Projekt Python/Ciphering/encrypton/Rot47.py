from Rot import RotCipher

class Rot47Cipher(RotCipher):
    def encrypt(self, text):
        result = ''
        for char in text:
            if 33 <= ord(char) <= 126:
                result += chr((ord(char) - 33 + 47) % 94 + 33)
            else:
                result += char
        return result

    def decrypt(self, text):
        return self.encrypt(text)