import argparse
import sys
from doc_reader import doc_reader
from doc_parser import doc_parser

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d_one', '--document_one', type = str,
        help = 'Path to the document in doc format.', required = True)
    parser.add_argument('-d_two', '--document_two', type = str,
        help = 'Path to the document in doc format.', default = None)
    parser = parser.parse_args()
    path_to_docs = (parser.document_one, parser.document_two)
    return path_to_docs

def exec_commands(command, pars = None, document = None, target_act = None):
    results = None
    if (command == 'find'):
        results = pars.find_word(' '.join(target_act))
    elif (command == 'sub'):
        results = pars.replace_word(target_act[0], ' '.join(target_act[1:]))
    elif (command == 'emplace_after'):
        results = pars.emplace_after(target_act[0], ' '.join(target_act[1:]))
    elif (command == 'print'):
        results = document.print_doc()
    elif (command == 'save'):
        results = document.save_file()
    elif (command == 'help'):
        print('Commands: \nfind words - searches for a words in a file \n' \
            'sub words replacement - replaces the words in the file \n' \
            'emplace_after words insert - insert the words in the file \n' \
            'print - print file')
    elif (command == 'exit'):
        sys.exit()
    return results

def choose_curr_doc(commands):
    if (len(commands) > 1 and commands[1] == 'doc1'):
        curr_doc = 0
        pos = 2
    elif (len(commands) > 1 and commands[1] == 'doc2'):
        curr_doc = 1
        pos = 2
    else:
        curr_doc = 0
        pos = 1
    return (curr_doc, pos)

def main():
    path_to_docs = build_parser()
    documents = (doc_reader(path_to_docs[0]), doc_reader(path_to_docs[1]))
    parser = (doc_parser(documents[0].get_doc()),
        doc_parser(documents[1].get_doc()))

    while (True):
        commands = input('enter command$').split(' ')
        curr_doc, pos = choose_curr_doc(commands)
        try:
            sub_command = commands.index('<')
        except:
            sub_command = -1
        if (sub_command != -1):
            sub_commands = commands[sub_command + 1:]
            sub_doc, sub_pos = choose_curr_doc(sub_commands)
            act = exec_commands(sub_commands[0], pars=parser[sub_doc],
            document=documents[sub_doc], target_act=sub_commands[sub_pos:])
            if (commands[0] != 'find'):
                act.insert(0, commands[pos])
        else:
            act = commands[pos:]
        results = exec_commands(commands[0], pars=parser[curr_doc],
            document=documents[curr_doc], target_act=act)
        if (type(results) == str):
            print(results)
        else:
            for line in results:
                print(line)



if __name__ == '__main__':
    sys.exit(main() or 0)