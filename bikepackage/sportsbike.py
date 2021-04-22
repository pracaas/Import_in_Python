from auto import Auto
from suvpackage.xlesuv import Xlesuv


class Sportsbike:
    def __init__(self):
        self.var = "Testvar"

    def getname(self):
        return self.var
    def getbikename(self):
        return "R15"

    def getderiveautoname(self):
        at = Auto()
        return at.getautoname()
    def getxle(self):
        xl = Xlesuv()
        return xl.getxlesuvname()


if __name__ == "__main__":
    ss = Sportsbike()
    print(ss.getname())
    print(ss.getbikename())
    print(ss.getderiveautoname())
    print(ss.getxle())
