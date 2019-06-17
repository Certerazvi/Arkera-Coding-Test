import unittest


def increment_dictionary_values(d, i):
    result = {}
    for k, v in d.items():
        result[k] = v + i
    return d


class TestIncrementDictionaryValues(unittest.TestCase):

    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)
