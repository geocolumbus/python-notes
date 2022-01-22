from importlib.machinery import SourceFileLoader

strings = SourceFileLoader("strings", "src/strings.py").load_module()


def test_strings():
    assert strings.basics() == "George"
