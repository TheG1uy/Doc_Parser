from docx import Document

class doc_reader:
    def __init__(self, _path_to_doc):
        self.path_to_doc = _path_to_doc
        self.file = []
        if (_path_to_doc.find('.txt') != -1):
            with open(_path_to_doc, 'w') as doc:
                for line in doc:
                    for sentence in line.text.split('.'):
                        self.file.append(sentence)
        else:
            doc = Document('test.docx')
            for line in doc.paragraphs:
                for sentence in line.text.split('.'):
                    self.file.append(sentence)

    def print_text(self):
        for line in self.file:
            print(line)

    def get_text(self):
        return self.file

    def save_file(self, file_name):
        pass