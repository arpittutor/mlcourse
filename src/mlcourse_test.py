from . import mlcourse

def test_mlcourse():
    assert mlcourse.apply("Jane") == "hello Jane"
