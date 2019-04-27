import re

class doc_parser:
    def __init__(self, _file):
        self.file = _file

    def find_word(self, pattern):
        for line in self.file:
            result = re.findall(pattern, line)
            if (len(result) > 0):
                print(line)

    def replace_word(self, pattern, repl):
        for line in self.file:
            find = re.findall(pattern, line)
            if (len(find) > 0):
                result = re.sub(pattern, repl, line)
                print(result)

    def emplace_after(self, pattern, sentence):
        r = re.compile(pattern)
        for line in self.file:
            find = [m.span() for m in r.finditer(line)]
            for res in find:
                line = line[:res[1]] ' ' + sentence + line[res[1]:]
                print(line)
