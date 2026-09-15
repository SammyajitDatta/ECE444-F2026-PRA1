class utils:

    def reversed(self, number):
        if number < 0:
            return -int(str(abs(number))[::-1])
        return int(str(number)[::-1])

    def formatter(self, number):
        return bin(number), oct(number)