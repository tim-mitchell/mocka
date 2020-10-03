# mocka
mock library than understands annotations

A drop-in replacement for the builtin python mock module where annotations on spec objects are used to spec mocked attributes and methods.

In addition to the standard `unittest.mock` functionality, a new `from_protocol` function
is added.

```python
from_protocol(C)
``` 
is an alias for 
```python
create_autospec(C, spec_set=True, instance=True)
```

When you have type-hinted code like this
```python
class A(object):
    b: str

    def __init__(self, b: str):
        self.b = b

    def foo(self, bar: int) -> list:
        return ['x']*bar


class C(object):
    a: int

    def __init__(self, a: int):
        self.a = a

    def bar(self, foo: str) -> A:
        return A(foo)
```
Then mocking them with mocka will use the type hints as specs for child mocks.
```python
m = mocka.from_protocol(C)
a = m.bar('hello')

# the following are all True
isinstance(a, A)
isinstance(a.b, str)
isinstance(m.a, int)
isinstance(a.foo(4), list)
```

`mocka` also understands common `typing` types such as `Dict` and `Tuple` and `Optional`

```python
import typing

class D(object):
    a: typing.Optional[int]
    d: typing.Dict[str, int]
    e: typing.Optional[typing.AnyStr]
    t: typing.Tuple[int, float]

    def __init__(self, a: int):
        self.a = a

    def bar(self, foo: str) -> typing.Optional[A]:
        return A(foo)

m = mocka.from_protocol(D)
a = m.bar('hello')

# the following are all True
isinstance(m, D)
isinstance(a, A)
isinstance(m.a, int)
isinstance(m.d, dict)
isinstance(m.e, str)
isinstance(m.t, tuple)
```
