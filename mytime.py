import string
import io
import sys

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds = self.seconds % 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes = self.minutes % 60

    def __str__(self):
        return "Time is {} hrs, {} mins and {} secs".format(self.hours, self.minutes, self.seconds)

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
            elif self.minutes > other.minutes:
                return False
            elif self.minutes == other.minutes:
                if self.seconds < other.seconds:
                    return True
                else:
                    return False
    def __add__(self, other):
        return Time(self.hours + other.hours,
                    self.minutes + other.minutes,
                    self.seconds + other.seconds)

    def convert_to_seconds(self):
        return (int(self.hours*3600+self.minutes*60+self.seconds))
    def __ne__(self, other):
        if (self.hours != other.hours) or (self.minutes != other.minutes) or (self.seconds != other.seconds):
            return True
        else:
            return False




t1 = Time(24, 120, 140)
t2 = Time(24, 120, 140)
print ("t1:", t1)
print("t2:", t2)
print(t1 < t2)
summ = t1+t2
print("Sum:", summ)
print(t1.convert_to_seconds())
print("!=", (t1 != t2))

