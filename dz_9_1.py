import colorama
from colorama import Back
import time

colorama.init()


class TraficLight:
    __color = [Back.RED, Back.YELLOW, Back.GREEN]

    def runing(self):
        print(TraficLight.__color[0])
        time.sleep(7)
        print(TraficLight.__color[1])
        time.sleep(2)
        print(TraficLight.__color[2])
        time.sleep(5)


a = TraficLight()
a.runing()
