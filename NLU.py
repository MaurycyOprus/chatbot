import jsgf
from os import listdir
from os.path import isfile, join


def load_grammar():
    gram_dir = './gramatyka/'
    grammar_files = [file for file in listdir(gram_dir) if isfile(join(gram_dir, file))]

    grammars = []

    print(grammar_files)
    for grammarFile in grammar_files:
        print(grammarFile)
        grammar = jsgf.parse_grammar_file(gram_dir + grammarFile)
        grammars.append(grammar)

    return grammars


grammars = load_grammar()


def get_slots(expansion, slots):
    if expansion.tag != '':
        slots.append((expansion.tag, expansion.current_match))
        return

    for child in expansion.children:
        get_slots(child, slots)

    if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
        get_slots(expansion.referenced_rule.expansion, slots)


def get_dialog_act(rule):
    slots = []
    get_slots(rule.expansion, slots)
    return {'act': rule.grammar.name, 'slots': slots}


def nlu(utterance):
    matched = None
    for _grammar in grammars:
        matched = _grammar.find_matching_rules(utterance)
        if matched:
            break

    if matched:
        return get_dialog_act(matched[0])
    else:
        return {'act': 'null', 'slots': []}
