class Auto:
    def __init__(self):
        self.autovar = "autovar"

    def getautoname(self):
        return "Aeroplane from Auto"

if __name__ == "__main__":
    at = Auto()
    print(at.getautoname())