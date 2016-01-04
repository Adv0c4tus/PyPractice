import string
import math
import random

class Instrument:
    def __init__(self, name):
        self.name = name
    def play(self):
        return "Playing on {}".format(self.name)
    def __str__(self):
        return 'Instrument: {}'.format(self.name)
class Guitar(Instrument):
    def _init_(self, name, strings):
        self.name = name
        self.strings = strings
        return "{}".format(self.name)
    def play(self):
        if self.strings > 0:
            if random.random() <= 0.01:
                self.strings -= 1
            return "Playing on {}".format(self.name)
        else:
            return "Can not play, no strings :("
class Ukulele(Guitar):
    def _init_(self, name):
        super().__init__(name,strings=4)