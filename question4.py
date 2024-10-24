class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._attributes = [('length', self.length), ('width', self.width)]
        self._index = 0

    def __iter__(self):
        self._index = 0  # Reset index for new iteration
        return self

    def __next__(self):
        if self._index < len(self._attributes):
            attribute = self._attributes[self._index]
            self._index += 1
            return {attribute[0]: attribute[1]}
        else:
            raise StopIteration

# Example usage
rectangle = Rectangle(10, 20)
for attribute in rectangle:
    print(attribute)
