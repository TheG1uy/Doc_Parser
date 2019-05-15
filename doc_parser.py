import re

class doc_parser:
    def __init__(self, _doc):
        self.doc = _doc

    def find_word(self, pattern):
        all_results = []
        for curr_line in range(len(self.doc.paragraphs)):
            result = re.findall(pattern, self.doc.paragraphs[curr_line].text)
            if (len(result) > 0):
                all_results.append(self.doc.paragraphs[curr_line].text)
        return all_results

    def replace_word(self, pattern, repl):
        all_results = []
        for curr_line in range(len(self.doc.paragraphs)):
            find = re.findall(pattern, self.doc.paragraphs[curr_line].text)
            if (len(find) > 0):
                result = re.sub(pattern, repl, self.doc.paragraphs[curr_line].text)
                self.doc.paragraphs[curr_line].text = result
                all_results.append(result)
        return all_results

    def emplace_after(self, pattern, sentence):
        all_results = []
        r = re.compile(pattern)
        for curr_line in range(len(self.doc.paragraphs)):
            find = [m.span() for m in r.finditer(self.doc.paragraphs[curr_line].text)]
            for res in find:
                self.doc.paragraphs[curr_line].text = ( \
                    self.doc.paragraphs[curr_line].text[:res[1]] + \
                    ' ' + sentence + self.doc.paragraphs[curr_line].text[res[1]:])
                all_results.append(self.doc.paragraphs[curr_line].text)
        return all_results
