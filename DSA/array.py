class DynamicArray:
    def __init__(self, factor=2):
        self.array = []
        self.size = 0
        self.factor = factor

    def __len__(self):
        return self.size

    def __bool__(self):
        return self.size > 0

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __iter__(self):
        return iter(self.array[:self.size])

    def __str__(self):
        return str(self.array[:self.size])

    def _resize(self):
        new_capacity = self.factor * len(self.array)
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, element):
        assert index >= 0 and index <= self.size
        if self.size == len(self.array):
            self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def delete(self, index):
        assert index >= 0 and index < self.size
        del self.array[index]
        self.size -= 1
        if self.size and self.size == len(self.array) // self.factor:
            self._resize()

    def rotate(self, k):
        assert k >= 0 and k < self.size
        steps = k % self.size
        if steps == 0:
            return
        self.array[-steps:] = self.array[:steps]

    def reverse(self):
        self.array[:self.size] = reversed(self.array[:self.size])

    def append(self, element):
        if self.size == len(self.array):
            self._resize()
        self.array[self.size] = element
        self.size += 1

    def prepend(self, element):
        if self.size == len(self.array):
            self._resize()
        for i in range(self.size, 0, -1):
            self.array[i] = self.array[i - 1]
        self.array[0] = element
        self.size += 1

    def merge(self, other):
        if not other:
            return
        if self.size + len(other) >= len(self.array):
            self._resize()
        self.array[self.size:self.size+len(other)] = other.array[:other.size]
        self.size += other.size
        other.clear()

    def interleave(self, other):
        if not other:
            return
        if self.size + len(other) >= len(self.array):
            self._resize()
       