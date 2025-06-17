class OldPrinter:
    def old_print(self, text):
        print(f"Old Printer: {text}")

class NewPrinterInterface:
    def print(self, text):
        pass

class PrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        self.old_printer.old_print(text)

old = OldPrinter()
adapter = PrinterAdapter(old)
adapter.print("Adapted printing!")
