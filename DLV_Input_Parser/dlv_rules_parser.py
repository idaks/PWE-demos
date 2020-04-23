from antlr4 import *
from antlr4.tree.Trees import Trees

from .Antlr_Files.DLV_InLexer import DLV_InLexer
from .Antlr_Files.DLV_InParser import DLV_InParser
from .Antlr_Files.DLV_InListener import DLV_InListener


DLV_COMMENT_SYMBOL = '%'
DLV_RULE_END_SYMBOL = '.'


class RuleAtom:

    def __init__(self):
        self.rel_name = None
        self.rel_arity = None
        self.type = None
        self.vars = []

    def __str__(self):
        return str(self.__dict__)


class AntlrDLVRulesListener(DLV_InListener):

    POSITIVE_ATOM = '+'
    NEGATIVE_ATOM = '-'

    def __init__(self):

        self.facts = []
        self.rules = []
        self.ics = []

        self.curr_head = None
        self.curr_tail = None

        self.curr_atom_set = []
        self.curr_atom = None
        self.curr_atom_depth = 0
        self.curr_atom_data = None

        self.atom_type = None

    def enterPositive_atom(self, ctx:DLV_InParser.Positive_atomContext):
        self.atom_type = AntlrDLVRulesListener.POSITIVE_ATOM

    def enterNegative_atom(self, ctx:DLV_InParser.Negative_atomContext):
        self.atom_type = AntlrDLVRulesListener.NEGATIVE_ATOM

    def enterAtom(self, ctx:DLV_InParser.AtomContext):
        self.curr_atom_depth += 1
        rel_name = ctx.TEXT().getText()
        if self.curr_atom_depth == 1:
            self.curr_atom = RuleAtom()
            self.curr_atom.rel_name = rel_name
            # Set defaults in case this is a 0-arity relation
            self.curr_atom_data = []
        else:
            tmp_ptr = self.curr_atom_data
            for _ in range(self.curr_atom_depth - 2):
                tmp_ptr = tmp_ptr[-1]
            tmp_ptr.append([rel_name])

    def enterAtom_text(self, ctx:DLV_InParser.Atom_textContext):
        tmp_ptr = self.curr_atom_data
        for _ in range(self.curr_atom_depth - 1):
            tmp_ptr = tmp_ptr[-1]
        tmp_ptr.append(ctx.TEXT().getText())

    def exitAtom(self, ctx:DLV_InParser.AtomContext):
        if self.curr_atom_depth == 1:
            self.curr_atom.rel_arity = len(self.curr_atom_data)
            self.curr_atom.type = self.atom_type
            self.curr_atom.vars = self.curr_atom_data
            self.curr_atom_set.append(self.curr_atom)

        self.curr_atom_depth -= 1

    def exitHead(self, ctx:DLV_InParser.HeadContext):
        self.curr_head = self.curr_atom_set
        self.curr_atom_set = []

    def exitTail(self, ctx:DLV_InParser.TailContext):
        self.curr_tail = self.curr_atom_set
        self.curr_atom_set = []

    def exitFact(self, ctx:DLV_InParser.FactContext):
        self.facts.extend(self.curr_atom_set)
        self.curr_atom_set = []

    def exitHead_tail_rule(self, ctx:DLV_InParser.Head_tail_ruleContext):
        self.rules.append((self.curr_head, self.curr_tail))
        self.curr_head = None
        self.curr_tail = None

    def exitIc(self, ctx:DLV_InParser.IcContext):
        self.ics.append(self.curr_tail)
        self.curr_tail = None

    def exitDlv_rule(self, ctx:DLV_InParser.Dlv_ruleContext):
        self.curr_atom_set = []
        self.curr_head = None
        self.curr_tail = None


def __parse_dlv_rules__(input_stream, silent=False, print_parse_tree=False):
    lexer = DLV_InLexer(input_stream)

    # use this line to take input from the cmd line
    # lexer = PWE_ASP_Meta_DataLexer(StdinStream())

    ct_stream = CommonTokenStream(lexer)
    parser = DLV_InParser(ct_stream)
    tree = parser.dlv_file()
    if print_parse_tree:
        print(Trees.toStringTree(tree, None, parser))
    asp_meta_data_listener = AntlrDLVRulesListener()
    asp_meta_data_listener.silent = silent
    walker = ParseTreeWalker()
    walker.walk(asp_meta_data_listener, tree)

    return asp_meta_data_listener


def preprocess(lines):

    def is_not_a_comment(line):
        return line[0] != DLV_COMMENT_SYMBOL

    def remove_comments(line):
        first_comment_symbol_loc = line.find(DLV_COMMENT_SYMBOL)
        if first_comment_symbol_loc != -1:
            line = line[:first_comment_symbol_loc]
            line = line.strip()
        return line

    lines = map(str.strip, lines)
    lines = filter(lambda x: len(x) > 0, lines)
    lines = filter(is_not_a_comment, lines)
    lines = map(remove_comments, lines)

    return list(lines)


def __parse_dlv_rules_from_file__(fname, silent=False, print_parse_tree=False):
    input_stream = FileStream(fname)
    return __parse_dlv_rules__(input_stream, silent, print_parse_tree)


def __parse_dlv_rules_from_string__(asp_input_string, silent=False, print_parse_tree=False):
    input_stream = InputStream(asp_input_string)
    return __parse_dlv_rules__(input_stream, silent, print_parse_tree)


def parse_dlv_rules(dlv_lines, silent=False, print_parse_tree=False):
    if isinstance(dlv_lines, str):
        dlv_lines = dlv_lines.splitlines()
    rule_lines = preprocess(dlv_lines)
    rule_lines_str = "\n".join(rule_lines)
    return __parse_dlv_rules_from_string__(rule_lines_str, silent=silent, print_parse_tree=print_parse_tree)


def parse_dlv_rules_from_file(fname, silent=False, print_parse_tree=False):
    with open(fname, 'r') as f:
        dlv_rules = f.read()
    return parse_dlv_rules(dlv_rules, silent=silent, print_parse_tree=print_parse_tree)

