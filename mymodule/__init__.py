class Foo:
    def __eq__(self, other):
        if not isinstance(other, Foo):
            raise TypeError('Foo objects cannot be compared to non-Foo objects')

foo = Foo()