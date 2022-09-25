import math


class SeriRLC:

    def enduktifReaktans(f,L):
        return 2 * 3.14 * f * L * 10 ** (-3)

    def kapasitifReaktans(f,C):
        return 10**(6)/(2*3.14*f*C)
