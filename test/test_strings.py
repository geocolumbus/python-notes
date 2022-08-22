from importlib.machinery import SourceFileLoader

strings = SourceFileLoader("strings", "src/python_strings.py").load_module()


def test_strings():
    assert strings.basics() == "George"
