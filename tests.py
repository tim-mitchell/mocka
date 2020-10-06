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
    aa: A

    def __init__(self, a: int):
        self.a = a
        self.aa = A('bb')

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
    def test_from_protocol(self):
        m = mocka.from_protocol(C)
        self.assertIsInstance(m, C)
        a = m.bar('hello')
        aa = m.aa
        self.assertIsInstance(m.a, int)
        self.assertIsInstance(a, A)
        self.assertIsInstance(a.b, str)
        self.assertIsInstance(a.foo(5), list)
        self.assertIsInstance(aa, A)
        self.assertIsInstance(aa.b, str)
        self.assertIsInstance(aa.foo(4), list)

    def test_recursive_autospec(self):
        m = mocka.from_protocol(C)
        a = m.bar('hello')
        self.assertIsInstance(a.foo(4), list)

    def test_untyped_mock(self):
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
