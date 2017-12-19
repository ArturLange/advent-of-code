import unittest

from day9 import StreamProcess


class TestDay9(unittest.TestCase):
    def test_parse_input(self):
        test_data = (
            ('{}', 1),
            ('{{{}}}', 6),
            ('{{},{}}', 5),
            ('{{{},{},{{}}}}', 16),
            ('{<a>,<a>,<a>,<a>}', 1),
            ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
            ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
            ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
            ('{<>!>}', 1),
        )

        for case in test_data:
            stream_process = StreamProcess(case[0])
            print(stream_process.count_scores(), stream_process.stream, case)
            assert stream_process.count_scores() == case[1]

    def test_apply_ignores(self):
        stream_process = StreamProcess('{<!>,<<!!,!!!>!o!!>,{<e}eo>}}}')
        stream_process.apply_ignores()
        assert stream_process.stream == '{<,<<,>,{<e}eo>}}}'


if __name__ == '__main__':
    unittest.main()
