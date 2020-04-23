# Generated from DLV_Input_Parser/Antlr_Files/DLV_In.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DLV_InParser import DLV_InParser
else:
    from DLV_InParser import DLV_InParser

# This class defines a complete listener for a parse tree produced by DLV_InParser.
class DLV_InListener(ParseTreeListener):

    # Enter a parse tree produced by DLV_InParser#dlv_file.
    def enterDlv_file(self, ctx:DLV_InParser.Dlv_fileContext):
        pass

    # Exit a parse tree produced by DLV_InParser#dlv_file.
    def exitDlv_file(self, ctx:DLV_InParser.Dlv_fileContext):
        pass


    # Enter a parse tree produced by DLV_InParser#dlv_rule.
    def enterDlv_rule(self, ctx:DLV_InParser.Dlv_ruleContext):
        pass

    # Exit a parse tree produced by DLV_InParser#dlv_rule.
    def exitDlv_rule(self, ctx:DLV_InParser.Dlv_ruleContext):
        pass


    # Enter a parse tree produced by DLV_InParser#fact.
    def enterFact(self, ctx:DLV_InParser.FactContext):
        pass

    # Exit a parse tree produced by DLV_InParser#fact.
    def exitFact(self, ctx:DLV_InParser.FactContext):
        pass


    # Enter a parse tree produced by DLV_InParser#head_tail_rule.
    def enterHead_tail_rule(self, ctx:DLV_InParser.Head_tail_ruleContext):
        pass

    # Exit a parse tree produced by DLV_InParser#head_tail_rule.
    def exitHead_tail_rule(self, ctx:DLV_InParser.Head_tail_ruleContext):
        pass


    # Enter a parse tree produced by DLV_InParser#ic.
    def enterIc(self, ctx:DLV_InParser.IcContext):
        pass

    # Exit a parse tree produced by DLV_InParser#ic.
    def exitIc(self, ctx:DLV_InParser.IcContext):
        pass


    # Enter a parse tree produced by DLV_InParser#head.
    def enterHead(self, ctx:DLV_InParser.HeadContext):
        pass

    # Exit a parse tree produced by DLV_InParser#head.
    def exitHead(self, ctx:DLV_InParser.HeadContext):
        pass


    # Enter a parse tree produced by DLV_InParser#tail.
    def enterTail(self, ctx:DLV_InParser.TailContext):
        pass

    # Exit a parse tree produced by DLV_InParser#tail.
    def exitTail(self, ctx:DLV_InParser.TailContext):
        pass


    # Enter a parse tree produced by DLV_InParser#positive_atom.
    def enterPositive_atom(self, ctx:DLV_InParser.Positive_atomContext):
        pass

    # Exit a parse tree produced by DLV_InParser#positive_atom.
    def exitPositive_atom(self, ctx:DLV_InParser.Positive_atomContext):
        pass


    # Enter a parse tree produced by DLV_InParser#negative_atom.
    def enterNegative_atom(self, ctx:DLV_InParser.Negative_atomContext):
        pass

    # Exit a parse tree produced by DLV_InParser#negative_atom.
    def exitNegative_atom(self, ctx:DLV_InParser.Negative_atomContext):
        pass


    # Enter a parse tree produced by DLV_InParser#atom.
    def enterAtom(self, ctx:DLV_InParser.AtomContext):
        pass

    # Exit a parse tree produced by DLV_InParser#atom.
    def exitAtom(self, ctx:DLV_InParser.AtomContext):
        pass


    # Enter a parse tree produced by DLV_InParser#atom_content.
    def enterAtom_content(self, ctx:DLV_InParser.Atom_contentContext):
        pass

    # Exit a parse tree produced by DLV_InParser#atom_content.
    def exitAtom_content(self, ctx:DLV_InParser.Atom_contentContext):
        pass


    # Enter a parse tree produced by DLV_InParser#atom_text.
    def enterAtom_text(self, ctx:DLV_InParser.Atom_textContext):
        pass

    # Exit a parse tree produced by DLV_InParser#atom_text.
    def exitAtom_text(self, ctx:DLV_InParser.Atom_textContext):
        pass


