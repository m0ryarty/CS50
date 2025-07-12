class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        print('a', self.size)
        cookies = f'{int(self.size) * '🍪'}'
        return f'{cookies}'

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError
        self.size = self.size + n
        return self.size

    def withdraw(self, n):
        size = self.size - n
        if self.size - n < 0:
            raise ValueError
        self.size = self.size - n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError

        self._size = size


def main():
    jar = Jar()
    jar1 = jar.deposit(3)
    jar2 = jar.deposit(4)

    print('z', jar1, jar2)


main()
