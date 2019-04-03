from dictstack import DictStack


def test_basic_dict():
    sd = DictStack()
    sd['a'] = 1
    sd[10] = 20

    assert sd['a'] == 1
    assert sd[10] == 20

def test_push_and_read():
    sd = DictStack()
    sd.push()
    sd['a'] = 1

    assert sd['a'] == 1

def test_write_push_write():
    sd = DictStack()
    sd['a'] = 1
    sd.push()
    sd['a'] = 2

    assert sd['a'] == 2

def test_write_push_write_pop_read():
    sd = DictStack()
    sd['a'] = 1
    sd.push()
    sd['a'] = 2
    sd.pop()

    assert sd['a'] == 1

def test_keys():
    sd = DictStack()

    sd['a'] = 1
    sd['b'] = 2

    assert sd.keys() == set(('a', 'b'))

    sd.push()

    sd['a'] = 3

    assert sd.keys() == set(('a', 'b'))

    sd['c'] = 4

    assert sd.keys() == set(('a', 'b', 'c'))

    sd.pop()

    assert sd.keys() == set(('a', 'b'))


def test_len():
    sd = DictStack()

    sd['a'] = 1
    sd['b'] = 2

    assert len(sd) == 2

    sd.push()

    sd['a'] = 3

    assert len(sd) == 2

    sd['c'] = 4

    assert len(sd) == 3

    sd.pop()

    assert len(sd) == 2
