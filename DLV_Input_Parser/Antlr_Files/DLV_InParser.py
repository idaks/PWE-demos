# Generated from DLV_Input_Parser/Antlr_Files/DLV_In.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\7\2")
        buf.write("\34\n\2\f\2\16\2\37\13\2\3\3\3\3\3\3\5\3$\n\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\7\7\62\n\7\f")
        buf.write("\7\16\7\65\13\7\3\7\3\7\3\b\3\b\3\b\5\b<\n\b\3\b\3\b\7")
        buf.write("\b@\n\b\f\b\16\bC\13\b\3\b\3\b\5\bG\n\b\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\5\13S\n\13\3\f\3\f\5\f")
        buf.write("W\n\f\3\f\3\f\7\f[\n\f\f\f\16\f^\13\f\3\f\3\f\5\fb\n\f")
        buf.write("\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2")
        buf.write("\2d\2\35\3\2\2\2\4#\3\2\2\2\6\'\3\2\2\2\b)\3\2\2\2\n,")
        buf.write("\3\2\2\2\f\63\3\2\2\2\168\3\2\2\2\20H\3\2\2\2\22J\3\2")
        buf.write("\2\2\24M\3\2\2\2\26\\\3\2\2\2\30c\3\2\2\2\32\34\5\4\3")
        buf.write("\2\33\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2")
        buf.write("\2\2\36\3\3\2\2\2\37\35\3\2\2\2 $\5\6\4\2!$\5\b\5\2\"")
        buf.write("$\5\n\6\2# \3\2\2\2#!\3\2\2\2#\"\3\2\2\2$%\3\2\2\2%&\7")
        buf.write("\3\2\2&\5\3\2\2\2\'(\5\20\t\2(\7\3\2\2\2)*\5\f\7\2*+\5")
        buf.write("\16\b\2+\t\3\2\2\2,-\5\16\b\2-\13\3\2\2\2./\5\20\t\2/")
        buf.write("\60\7\4\2\2\60\62\3\2\2\2\61.\3\2\2\2\62\65\3\2\2\2\63")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2")
        buf.write("\66\67\5\20\t\2\67\r\3\2\2\28A\7\5\2\29<\5\20\t\2:<\5")
        buf.write("\22\n\2;9\3\2\2\2;:\3\2\2\2<=\3\2\2\2=>\7\6\2\2>@\3\2")
        buf.write("\2\2?;\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BF\3\2\2\2")
        buf.write("CA\3\2\2\2DG\5\20\t\2EG\5\22\n\2FD\3\2\2\2FE\3\2\2\2G")
        buf.write("\17\3\2\2\2HI\5\24\13\2I\21\3\2\2\2JK\7\7\2\2KL\5\24\13")
        buf.write("\2L\23\3\2\2\2MR\7\n\2\2NO\7\b\2\2OP\5\26\f\2PQ\7\t\2")
        buf.write("\2QS\3\2\2\2RN\3\2\2\2RS\3\2\2\2S\25\3\2\2\2TW\5\30\r")
        buf.write("\2UW\5\24\13\2VT\3\2\2\2VU\3\2\2\2WX\3\2\2\2XY\7\6\2\2")
        buf.write("Y[\3\2\2\2ZV\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]")
        buf.write("a\3\2\2\2^\\\3\2\2\2_b\5\30\r\2`b\5\24\13\2a_\3\2\2\2")
        buf.write("a`\3\2\2\2b\27\3\2\2\2cd\7\n\2\2d\31\3\2\2\2\f\35#\63")
        buf.write(";AFRV\\a")
        return buf.getvalue()


class DLV_InParser ( Parser ):

    grammarFileName = "DLV_In.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "';'", "':-'", "','", "'not'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "TEXT", "WHITESPACE" ]

    RULE_dlv_file = 0
    RULE_dlv_rule = 1
    RULE_fact = 2
    RULE_head_tail_rule = 3
    RULE_ic = 4
    RULE_head = 5
    RULE_tail = 6
    RULE_positive_atom = 7
    RULE_negative_atom = 8
    RULE_atom = 9
    RULE_atom_content = 10
    RULE_atom_text = 11

    ruleNames =  [ "dlv_file", "dlv_rule", "fact", "head_tail_rule", "ic", 
                   "head", "tail", "positive_atom", "negative_atom", "atom", 
                   "atom_content", "atom_text" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    TEXT=8
    WHITESPACE=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Dlv_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dlv_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.Dlv_ruleContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.Dlv_ruleContext,i)


        def getRuleIndex(self):
            return DLV_InParser.RULE_dlv_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDlv_file" ):
                listener.enterDlv_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDlv_file" ):
                listener.exitDlv_file(self)




    def dlv_file(self):

        localctx = DLV_InParser.Dlv_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dlv_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DLV_InParser.T__2 or _la==DLV_InParser.TEXT:
                self.state = 24
                self.dlv_rule()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dlv_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(DLV_InParser.FactContext,0)


        def head_tail_rule(self):
            return self.getTypedRuleContext(DLV_InParser.Head_tail_ruleContext,0)


        def ic(self):
            return self.getTypedRuleContext(DLV_InParser.IcContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_dlv_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDlv_rule" ):
                listener.enterDlv_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDlv_rule" ):
                listener.exitDlv_rule(self)




    def dlv_rule(self):

        localctx = DLV_InParser.Dlv_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dlv_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 30
                self.fact()
                pass

            elif la_ == 2:
                self.state = 31
                self.head_tail_rule()
                pass

            elif la_ == 3:
                self.state = 32
                self.ic()
                pass


            self.state = 35
            self.match(DLV_InParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positive_atom(self):
            return self.getTypedRuleContext(DLV_InParser.Positive_atomContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)




    def fact(self):

        localctx = DLV_InParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fact)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.positive_atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Head_tail_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def head(self):
            return self.getTypedRuleContext(DLV_InParser.HeadContext,0)


        def tail(self):
            return self.getTypedRuleContext(DLV_InParser.TailContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_head_tail_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead_tail_rule" ):
                listener.enterHead_tail_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead_tail_rule" ):
                listener.exitHead_tail_rule(self)




    def head_tail_rule(self):

        localctx = DLV_InParser.Head_tail_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_head_tail_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.head()
            self.state = 40
            self.tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tail(self):
            return self.getTypedRuleContext(DLV_InParser.TailContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_ic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIc" ):
                listener.enterIc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIc" ):
                listener.exitIc(self)




    def ic(self):

        localctx = DLV_InParser.IcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positive_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.Positive_atomContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.Positive_atomContext,i)


        def getRuleIndex(self):
            return DLV_InParser.RULE_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHead" ):
                listener.enterHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHead" ):
                listener.exitHead(self)




    def head(self):

        localctx = DLV_InParser.HeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_head)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.positive_atom()
                    self.state = 45
                    self.match(DLV_InParser.T__1) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 52
            self.positive_atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positive_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.Positive_atomContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.Positive_atomContext,i)


        def negative_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.Negative_atomContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.Negative_atomContext,i)


        def getRuleIndex(self):
            return DLV_InParser.RULE_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTail" ):
                listener.enterTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTail" ):
                listener.exitTail(self)




    def tail(self):

        localctx = DLV_InParser.TailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(DLV_InParser.T__2)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [DLV_InParser.TEXT]:
                        self.state = 55
                        self.positive_atom()
                        pass
                    elif token in [DLV_InParser.T__4]:
                        self.state = 56
                        self.negative_atom()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 59
                    self.match(DLV_InParser.T__3) 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DLV_InParser.TEXT]:
                self.state = 66
                self.positive_atom()
                pass
            elif token in [DLV_InParser.T__4]:
                self.state = 67
                self.negative_atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Positive_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(DLV_InParser.AtomContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_positive_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositive_atom" ):
                listener.enterPositive_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositive_atom" ):
                listener.exitPositive_atom(self)




    def positive_atom(self):

        localctx = DLV_InParser.Positive_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_positive_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Negative_atomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(DLV_InParser.AtomContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_negative_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegative_atom" ):
                listener.enterNegative_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegative_atom" ):
                listener.exitNegative_atom(self)




    def negative_atom(self):

        localctx = DLV_InParser.Negative_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_negative_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(DLV_InParser.T__4)
            self.state = 73
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(DLV_InParser.TEXT, 0)

        def atom_content(self):
            return self.getTypedRuleContext(DLV_InParser.Atom_contentContext,0)


        def getRuleIndex(self):
            return DLV_InParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = DLV_InParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(DLV_InParser.TEXT)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DLV_InParser.T__5:
                self.state = 76
                self.match(DLV_InParser.T__5)
                self.state = 77
                self.atom_content()
                self.state = 78
                self.match(DLV_InParser.T__6)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_contentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom_text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.Atom_textContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.Atom_textContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DLV_InParser.AtomContext)
            else:
                return self.getTypedRuleContext(DLV_InParser.AtomContext,i)


        def getRuleIndex(self):
            return DLV_InParser.RULE_atom_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_content" ):
                listener.enterAtom_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_content" ):
                listener.exitAtom_content(self)




    def atom_content(self):

        localctx = DLV_InParser.Atom_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom_content)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        self.state = 82
                        self.atom_text()
                        pass

                    elif la_ == 2:
                        self.state = 83
                        self.atom()
                        pass


                    self.state = 86
                    self.match(DLV_InParser.T__3) 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 93
                self.atom_text()
                pass

            elif la_ == 2:
                self.state = 94
                self.atom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(DLV_InParser.TEXT, 0)

        def getRuleIndex(self):
            return DLV_InParser.RULE_atom_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_text" ):
                listener.enterAtom_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_text" ):
                listener.exitAtom_text(self)




    def atom_text(self):

        localctx = DLV_InParser.Atom_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atom_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(DLV_InParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





