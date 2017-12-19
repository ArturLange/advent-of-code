import re


class StreamProcess:

    def __init__(self, stream: str):
        self.stream = stream
        self.ignore_re = re.compile(r'!.')
        self.garbage_re = re.compile(r'<.*?>')

    def apply_ignores(self):
        ignores = reversed(list(self.ignore_re.finditer(self.stream)))
        stream_list = list(self.stream)
        for ignore in ignores:
            span = ignore.span()
            stream_list[span[0]:] = stream_list[span[1]:]
        self.stream = ''.join(stream_list)

    def delete_garbage(self):
        garbages = reversed(list(self.garbage_re.finditer(self.stream)))
        stream_list = list(self.stream)
        for garbage in garbages:
            span = garbage.span()
            stream_list[span[0]:] = stream_list[span[1]:]
        self.stream = ''.join(stream_list)

    def count_scores(self):
        self.apply_ignores()
        self.delete_garbage()
        score = 0
        group_nesting_level = 0
        for char in self.stream:
            if char == '{':
                group_nesting_level += 1
            elif char == '}':
                score += group_nesting_level
                group_nesting_level -= 1
        return score


if __name__ == '__main__':
    with open('inputs/day9', 'r') as input_file:
        stream = input_file.readline()
        stream_process = StreamProcess(stream)
        print(stream_process.count_scores())
        print(stream_process.stream)
