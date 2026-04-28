class Komputer:
    def __init__(self):
        self.procesor = None
        self.ram = None
        self.grafika = None
        self.dysk = None

    def __str__(self):
        return f"Specyfikacja: [CPU: {self.procesor}, RAM: {self.ram}, GPU: {self.grafika}, Dysk: {self.dysk}]"

class KomputerBuilder:
    def build_procesor(self): pass
    def build_ram(self): pass
    def build_grafika(self): pass
    def build_dysk(self): pass
    def get_result(self): pass


class KomputerGamingowyBuilder(KomputerBuilder):
    def __init__(self):
        self.komputer = Komputer()

    def build_procesor(self):
        self.komputer.procesor = "AMD Ryzen 7535HS"

    def build_ram(self):
        self.komputer.ram = "32GB"

    def build_grafika(self):
        self.komputer.grafika = "RTX 4050"

    def build_dysk(self):
        self.komputer.dysk = "1.5TB"

    def get_result(self):
        return self.komputer


if __name__ == "__main__":
    builder = KomputerGamingowyBuilder()

    builder.build_procesor()
    builder.build_ram()
    builder.build_grafika()
    builder.build_dysk()

    moj_komputer = builder.get_result()

    print("Złożono nowy zestaw:")
    print(moj_komputer)