class Printer:

    def print_document(self, document):
        print(f"Drukowanie dokumentu: {document}")


class Scanner:
    
    def scan_document(self, document):
        print(f"Skanowanie dokumentu: {document}")


class MultifunctionalDevice(Printer, Scanner):
    pass


device = MultifunctionalDevice()

device.print_document("Dokument do wydrukowania")
device.scan_document("Dokument do zeskanowania")