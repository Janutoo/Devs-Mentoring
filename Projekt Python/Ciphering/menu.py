# from abc import ABC, abstractmethod
from encrypton import Rot13Cipher
from encrypton import Rot47Cipher
#from FileHandler import FileHanlder

class Menu:
    def __init__(self):
        self.encrypted_texts = []
        self.ciphers = {'ROT13': Rot13Cipher(), 'ROT47': Rot47Cipher()}

    def run(self):
        while True:
            print("\nWybierz opcję:")
            print("1. Szyfruj tekst")
            print("2. Zapisz zaszyfrowany tekst do pliku")
            print("3. Deszyfruj tekst z pliku")
            print("4. Wyświetl zaszyfrowane teksty w pamięci")
            print("5. Wyjdź")

            choice = input("Twój wybór: ")
            if choice == '1':
                self.encrypt_text()
            elif choice == '2':
                self.save_to_file()
            elif choice == '3':
                self.decrypt_from_file()
            elif choice == '4':
                self.print_encrypted_texts()
            elif choice == '5':
                break
            else:
                print("Nieprawidłowy wybór.")
    def chosen_method_to_enryped_text():
        text = input("Podaj tekst do zaszyfrowania: ")
        algorithm = input("Podaj algorytm (ROT13/ROT47): ")
        return algorithm

    # def encrypt_text(self):
    #     text = input("Podaj tekst do zaszyfrowania: ")
    #     algorithm = input("Podaj algorytm (ROT13/ROT47): ")
    #     metohd = chosen_method_to_enryped_text
    #     if algorithm in self.ciphers:
    #         encrypted_text = self.ciphers[algorithm].encrypt(text)
    #         self.encrypted_texts.append(encrypted_text)
    #         print("Zaszyfrowany tekst:", encrypted_text)
    #     else:
    #         print("Nieznany algorytm.")

    # def save_to_file(self):
    #     filename = input("Podaj nazwę pliku: ")
    #     text = input("Podaj tekst do zapisania: ")
    #     self._save_to_file(filename, text)
    #     print("Zapisano do pliku.")

    # def decrypt_from_file(self):
    #     filename = input("Podaj nazwę pliku: ")
    #     algorithm = input("Podaj algorytm (ROT13/ROT47): ")
    #     encrypted_text = self._read_from_file(filename)
    #     if encrypted_text:
    #         if algorithm in self.ciphers:
    #             decrypted_text = self.ciphers[algorithm].decrypt(encrypted_text)
    #             print("Odszyfrowany tekst:", decrypted_text)
    #         else:
    #             print("Nieznany algorytm.")
    #     else:
    #         print("Nie znaleziono pliku.")

    # def print_encrypted_texts(self):
    #     for text in self.encrypted_texts:
    #         print(text)

    # def _save_to_file(self, filename, text):
    #     with open(filename, 'w') as f:
    #         f.write(text)

    # def _read_from_file(self, filename):
    #     try:
    #         with open(filename, 'r') as f:
    #             return f.read()
    #     except FileNotFoundError:
    #         return None

if __name__ == "__main__":
    menu = Menu()
    menu.run()


