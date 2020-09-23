import mocka
import unittest
import typing

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


class D(object):
    a: typing.Optional[int]
    d: typing.Dict[str, int]
    e: typing.Optional[typing.AnyStr]
    f: typing.Any
    t: typing.Tuple[int, float]

    def __init__(self, a: int):
        self.a = a

    def bar(self, foo: str) -> typing.Optional[A]:
        return A(foo)


class TestMocka(unittest.TestCase):
    def test_create_autospec(self):
        m = mocka.create_autospec(C, spec_set=True, instance=True)
        self.assertIsInstance(m, C)
        a = m.bar('hello')
        self.assertIsInstance(a, A)
        self.assertIsInstance(a.b, str)
#        self.assertIsInstance(a.foo(4), list)
        self.assertIsInstance(m.a, int)

    def test_unspecced_mock(self):
        m = mocka.MagicMock()
        a = m.bar('hello')
        self.assertNotIsInstance(a, A)

    def test_create_autospec_typing_types(self):
        m = mocka.create_autospec(D, spec_set=True, instance=True)
        a = m.bar('hello')
        self.assertIsInstance(a, A)
        self.assertIsInstance(m.a, int)
        self.assertIsInstance(m.d, dict)
        self.assertIsInstance(m.e, str)
        self.assertIsInstance(m.t, tuple)
        self.assertIsNone(m.f.__dict__['_spec_class'])
