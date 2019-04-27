import argparse
import sys
from doc_reader import doc_reader
from doc_parser import doc_parser

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--document', type = str,
        help = 'Path to the document in txt/doc format.', required = True)
    return parser.parse_args().document


def main():
    path_to_doc = build_parser()
    document = doc_reader(path_to_doc)
    parser = doc_parser(document.get_text())

    while (True):
        commands = input('enter command$').split(' ')
        if (commands[0] == 'find'):
            parser.find_word(' '.join(commands[1:]))
        elif (commands[0] == 'sub'):
            parser.replace_word(commands[1], ' '.join(commands[2:]))
        elif (commands[0] == 'emplace_after'):
            parser.emplace_after(commands[1], ' '.join(commands[2:]))
        elif (commands[0] == 'print'):
            document.print_text()
        elif (commands[0] == 'exit'):
            break


if __name__ == '__main__':
    sys.exit(main() or 0)