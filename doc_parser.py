import re

class doc_parser:
    def __init__(self, _file):
        self.file = _file

    def find_word(self, pattern):
        for curr_line in range(len(self.file)):
            result = re.findall(pattern, self.file[curr_line])
            if (len(result) > 0):
                print(self.file[curr_line])

    def replace_word(self, pattern, repl):
        for curr_line in range(len(self.file)):
            find = re.findall(pattern, self.file[curr_line])
            if (len(find) > 0):
                result = re.sub(pattern, repl, self.file[curr_line])
                self.file[curr_line] = result
                print(result)

    def emplace_after(self, pattern, sentence):
        r = re.compile(pattern)
        for curr_line in range(len(self.file)):
            find = [m.span() for m in r.finditer(self.file[curr_line])]
            for res in find:
                self.file[curr_line] = (self.file[curr_line][:res[1]] + \
                    ' ' + sentence + self.file[curr_line][res[1]:])
                print(self.file[curr_line])
