"""
Тестувальник класу для роботи з часом

Запускати за допомогою nose:
```
# Всі тести
nosetests .

# Конкретний тест
nosetests test_time.TestTime:test_should_normalize
```
"""

from mytime import Time


class TestTime:

    def test_should_be_creatable(self):
        time = Time(24, 12, 12)
        assert time.hours == 24
        assert time.minutes == 12
        assert time.seconds == 12

    def test_should_normalize(self):
        a = Time(24, 12, 70)
        assert a == Time(24, 13, 10)
        b = Time(24, 70, 0)
        assert b == Time(25, 10, 0)
        c = Time(24, 70, 70)
        assert c == Time(25, 11, 10)

    def test_should_be_comparable(self):
        a = Time(12, 0, 0)
        b = Time(12, 1, 0)
        assert a < b
        assert not a > b
        assert a != b

        c = Time(12, 0, 0)
        assert a == c

    def test_should_be_addable(self):
        a = Time(12, 1, 1)
        b = Time(12, 50, 2)
        assert a + b == Time(24, 51, 3)

        a = Time(12, 50, 1)
        b = Time(12, 50, 2)
        assert a + b == Time(25, 40, 3)

    def test_should_be_convertible_to_seconds(self):
        a = Time(0, 0, 60)
        b = Time(1, 1, 1)
        assert a.convert_to_seconds() == 60
        assert b.convert_to_seconds() == 1 + 1*60 + 1*3600
