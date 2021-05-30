# Generated from LatexParser.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("\u0093\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\7\3&\n\3")
        buf.write("\f\3\16\3)\13\3\3\3\3\3\7\3-\n\3\f\3\16\3\60\13\3\7\3")
        buf.write("\62\n\3\f\3\16\3\65\13\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5A\n\5\3\6\7\6D\n\6\f\6\16\6G\13\6\3\6\3")
        buf.write("\6\7\6K\n\6\f\6\16\6N\13\6\7\6P\n\6\f\6\16\6S\13\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7Z\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\7\rr\n\r\f\r\16\ru\13\r\3\r\6\rx\n\r\r\r\16")
        buf.write("\ry\3\r\3\r\3\16\3\16\7\16\u0080\n\16\f\16\16\16\u0083")
        buf.write("\13\16\3\16\6\16\u0086\n\16\r\16\16\16\u0087\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\2\2\21\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36\2\3\3\2\5\7\2\u0098")
        buf.write("\2 \3\2\2\2\4\'\3\2\2\2\6\66\3\2\2\2\b@\3\2\2\2\nE\3\2")
        buf.write("\2\2\fY\3\2\2\2\16[\3\2\2\2\20_\3\2\2\2\22c\3\2\2\2\24")
        buf.write("g\3\2\2\2\26k\3\2\2\2\30o\3\2\2\2\32}\3\2\2\2\34\u008b")
        buf.write("\3\2\2\2\36\u008e\3\2\2\2 !\7\3\2\2!\"\5\4\3\2\"#\7\4")
        buf.write("\2\2#\3\3\2\2\2$&\5\6\4\2%$\3\2\2\2&)\3\2\2\2\'%\3\2\2")
        buf.write("\2\'(\3\2\2\2(\63\3\2\2\2)\'\3\2\2\2*.\5\b\5\2+-\5\6\4")
        buf.write("\2,+\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\62\3\2\2")
        buf.write("\2\60.\3\2\2\2\61*\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\5\3\2\2\2\65\63\3\2\2\2\66\67\t\2\2")
        buf.write("\2\67\7\3\2\2\28A\5\16\b\29A\5\20\t\2:A\5\22\n\2;A\5\24")
        buf.write("\13\2<A\5\26\f\2=A\5\30\r\2>A\5\32\16\2?A\5\36\20\2@8")
        buf.write("\3\2\2\2@9\3\2\2\2@:\3\2\2\2@;\3\2\2\2@<\3\2\2\2@=\3\2")
        buf.write("\2\2@>\3\2\2\2@?\3\2\2\2A\t\3\2\2\2BD\5\6\4\2CB\3\2\2")
        buf.write("\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2FQ\3\2\2\2GE\3\2\2\2H")
        buf.write("L\5\f\7\2IK\5\6\4\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3")
        buf.write("\2\2\2MP\3\2\2\2NL\3\2\2\2OH\3\2\2\2PS\3\2\2\2QO\3\2\2")
        buf.write("\2QR\3\2\2\2R\13\3\2\2\2SQ\3\2\2\2TZ\5\16\b\2UZ\5\20\t")
        buf.write("\2VZ\5\30\r\2WZ\5\32\16\2XZ\5\36\20\2YT\3\2\2\2YU\3\2")
        buf.write("\2\2YV\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z\r\3\2\2\2[\\\7\t\2")
        buf.write("\2\\]\5\n\6\2]^\7\b\2\2^\17\3\2\2\2_`\7\n\2\2`a\5\n\6")
        buf.write("\2ab\7\b\2\2b\21\3\2\2\2cd\7\13\2\2de\5\6\4\2ef\7\b\2")
        buf.write("\2f\23\3\2\2\2gh\7\13\2\2hi\5\6\4\2ij\7\b\2\2j\25\3\2")
        buf.write("\2\2kl\7\13\2\2lm\5\6\4\2mn\7\b\2\2n\27\3\2\2\2os\7\16")
        buf.write("\2\2pr\5\6\4\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2")
        buf.write("tw\3\2\2\2us\3\2\2\2vx\5\34\17\2wv\3\2\2\2xy\3\2\2\2y")
        buf.write("w\3\2\2\2yz\3\2\2\2z{\3\2\2\2{|\7\17\2\2|\31\3\2\2\2}")
        buf.write("\u0081\7\20\2\2~\u0080\5\6\4\2\177~\3\2\2\2\u0080\u0083")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0085")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0086\5\34\17\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\7")
        buf.write("\21\2\2\u008a\33\3\2\2\2\u008b\u008c\7\22\2\2\u008c\u008d")
        buf.write("\5\n\6\2\u008d\35\3\2\2\2\u008e\u008f\7\23\2\2\u008f\u0090")
        buf.write("\5\6\4\2\u0090\u0091\7\24\2\2\u0091\37\3\2\2\2\16\'.\63")
        buf.write("@ELQYsy\u0081\u0087")
        return buf.getvalue()


class LatexParser ( Parser ):

    grammarFileName = "LatexParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\begin{document}'", "'\\end{document}'", 
                     "<INVALID>", "'\\\\'", "<INVALID>", "'}'", "'\\textbf{'", 
                     "'\\textit{'", "'\\section{'", "'\\subsection{'", "'\\subsubsection{'", 
                     "'\\begin{enumerate}'", "'\\end{enumerate}'", "'\\begin{itemize}'", 
                     "'\\end{itemize}'", "'\\item'", "'\\begin{verbatim}'", 
                     "'\\end{verbatim}'" ]

    symbolicNames = [ "<INVALID>", "DOCUMENT_START", "DOCUMENT_END", "TEXT", 
                      "LINE_END", "WHITESPACE", "COMMAND_CLOSE", "BOLD_OPEN", 
                      "ITALICS_OPEN", "HEADER1", "HEADER2", "HEADER3", "ENUM_START", 
                      "ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", 
                      "CODE_END" ]

    RULE_latexDocument = 0
    RULE_documentContent = 1
    RULE_text = 2
    RULE_latexElement = 3
    RULE_elementContent = 4
    RULE_latexNestedElement = 5
    RULE_bold = 6
    RULE_italics = 7
    RULE_header1 = 8
    RULE_header2 = 9
    RULE_header3 = 10
    RULE_numbered_list = 11
    RULE_itemize = 12
    RULE_item = 13
    RULE_code = 14

    ruleNames =  [ "latexDocument", "documentContent", "text", "latexElement", 
                   "elementContent", "latexNestedElement", "bold", "italics", 
                   "header1", "header2", "header3", "numbered_list", "itemize", 
                   "item", "code" ]

    EOF = Token.EOF
    DOCUMENT_START=1
    DOCUMENT_END=2
    TEXT=3
    LINE_END=4
    WHITESPACE=5
    COMMAND_CLOSE=6
    BOLD_OPEN=7
    ITALICS_OPEN=8
    HEADER1=9
    HEADER2=10
    HEADER3=11
    ENUM_START=12
    ENUM_END=13
    LIST_START=14
    LIST_END=15
    ITEM=16
    CODE_START=17
    CODE_END=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LatexDocumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOCUMENT_START(self):
            return self.getToken(LatexParser.DOCUMENT_START, 0)

        def documentContent(self):
            return self.getTypedRuleContext(LatexParser.DocumentContentContext,0)


        def DOCUMENT_END(self):
            return self.getToken(LatexParser.DOCUMENT_END, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_latexDocument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatexDocument" ):
                listener.enterLatexDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatexDocument" ):
                listener.exitLatexDocument(self)




    def latexDocument(self):

        localctx = LatexParser.LatexDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_latexDocument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(LatexParser.DOCUMENT_START)
            self.state = 31
            self.documentContent()
            self.state = 32
            self.match(LatexParser.DOCUMENT_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def latexElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.LatexElementContext)
            else:
                return self.getTypedRuleContext(LatexParser.LatexElementContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_documentContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocumentContent" ):
                listener.enterDocumentContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocumentContent" ):
                listener.exitDocumentContent(self)




    def documentContent(self):

        localctx = LatexParser.DocumentContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_documentContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 34
                self.text()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.BOLD_OPEN) | (1 << LatexParser.ITALICS_OPEN) | (1 << LatexParser.HEADER1) | (1 << LatexParser.ENUM_START) | (1 << LatexParser.LIST_START) | (1 << LatexParser.CODE_START))) != 0):
                self.state = 40
                self.latexElement()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                    self.state = 41
                    self.text()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(LatexParser.TEXT, 0)

        def WHITESPACE(self):
            return self.getToken(LatexParser.WHITESPACE, 0)

        def LINE_END(self):
            return self.getToken(LatexParser.LINE_END, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = LatexParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LatexElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bold(self):
            return self.getTypedRuleContext(LatexParser.BoldContext,0)


        def italics(self):
            return self.getTypedRuleContext(LatexParser.ItalicsContext,0)


        def header1(self):
            return self.getTypedRuleContext(LatexParser.Header1Context,0)


        def header2(self):
            return self.getTypedRuleContext(LatexParser.Header2Context,0)


        def header3(self):
            return self.getTypedRuleContext(LatexParser.Header3Context,0)


        def numbered_list(self):
            return self.getTypedRuleContext(LatexParser.Numbered_listContext,0)


        def itemize(self):
            return self.getTypedRuleContext(LatexParser.ItemizeContext,0)


        def code(self):
            return self.getTypedRuleContext(LatexParser.CodeContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_latexElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatexElement" ):
                listener.enterLatexElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatexElement" ):
                listener.exitLatexElement(self)




    def latexElement(self):

        localctx = LatexParser.LatexElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_latexElement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.bold()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.italics()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.header1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.header2()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.header3()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.numbered_list()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.itemize()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 61
                self.code()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def latexNestedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.LatexNestedElementContext)
            else:
                return self.getTypedRuleContext(LatexParser.LatexNestedElementContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_elementContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementContent" ):
                listener.enterElementContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementContent" ):
                listener.exitElementContent(self)




    def elementContent(self):

        localctx = LatexParser.ElementContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elementContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 64
                self.text()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.BOLD_OPEN) | (1 << LatexParser.ITALICS_OPEN) | (1 << LatexParser.ENUM_START) | (1 << LatexParser.LIST_START) | (1 << LatexParser.CODE_START))) != 0):
                self.state = 70
                self.latexNestedElement()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                    self.state = 71
                    self.text()
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LatexNestedElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bold(self):
            return self.getTypedRuleContext(LatexParser.BoldContext,0)


        def italics(self):
            return self.getTypedRuleContext(LatexParser.ItalicsContext,0)


        def numbered_list(self):
            return self.getTypedRuleContext(LatexParser.Numbered_listContext,0)


        def itemize(self):
            return self.getTypedRuleContext(LatexParser.ItemizeContext,0)


        def code(self):
            return self.getTypedRuleContext(LatexParser.CodeContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_latexNestedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatexNestedElement" ):
                listener.enterLatexNestedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatexNestedElement" ):
                listener.exitLatexNestedElement(self)




    def latexNestedElement(self):

        localctx = LatexParser.LatexNestedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_latexNestedElement)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatexParser.BOLD_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.bold()
                pass
            elif token in [LatexParser.ITALICS_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.italics()
                pass
            elif token in [LatexParser.ENUM_START]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.numbered_list()
                pass
            elif token in [LatexParser.LIST_START]:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.itemize()
                pass
            elif token in [LatexParser.CODE_START]:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.code()
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


    class BoldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOLD_OPEN(self):
            return self.getToken(LatexParser.BOLD_OPEN, 0)

        def elementContent(self):
            return self.getTypedRuleContext(LatexParser.ElementContentContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_bold

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBold" ):
                listener.enterBold(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBold" ):
                listener.exitBold(self)




    def bold(self):

        localctx = LatexParser.BoldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bold)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(LatexParser.BOLD_OPEN)
            self.state = 90
            self.elementContent()
            self.state = 91
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItalicsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITALICS_OPEN(self):
            return self.getToken(LatexParser.ITALICS_OPEN, 0)

        def elementContent(self):
            return self.getTypedRuleContext(LatexParser.ElementContentContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_italics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItalics" ):
                listener.enterItalics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItalics" ):
                listener.exitItalics(self)




    def italics(self):

        localctx = LatexParser.ItalicsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_italics)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(LatexParser.ITALICS_OPEN)
            self.state = 94
            self.elementContent()
            self.state = 95
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADER1(self):
            return self.getToken(LatexParser.HEADER1, 0)

        def text(self):
            return self.getTypedRuleContext(LatexParser.TextContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_header1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader1" ):
                listener.enterHeader1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader1" ):
                listener.exitHeader1(self)




    def header1(self):

        localctx = LatexParser.Header1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_header1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(LatexParser.HEADER1)
            self.state = 98
            self.text()
            self.state = 99
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADER1(self):
            return self.getToken(LatexParser.HEADER1, 0)

        def text(self):
            return self.getTypedRuleContext(LatexParser.TextContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_header2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader2" ):
                listener.enterHeader2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader2" ):
                listener.exitHeader2(self)




    def header2(self):

        localctx = LatexParser.Header2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_header2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(LatexParser.HEADER1)
            self.state = 102
            self.text()
            self.state = 103
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Header3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEADER1(self):
            return self.getToken(LatexParser.HEADER1, 0)

        def text(self):
            return self.getTypedRuleContext(LatexParser.TextContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_header3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader3" ):
                listener.enterHeader3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader3" ):
                listener.exitHeader3(self)




    def header3(self):

        localctx = LatexParser.Header3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_header3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(LatexParser.HEADER1)
            self.state = 106
            self.text()
            self.state = 107
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numbered_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM_START(self):
            return self.getToken(LatexParser.ENUM_START, 0)

        def ENUM_END(self):
            return self.getToken(LatexParser.ENUM_END, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.ItemContext)
            else:
                return self.getTypedRuleContext(LatexParser.ItemContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_numbered_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumbered_list" ):
                listener.enterNumbered_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumbered_list" ):
                listener.exitNumbered_list(self)




    def numbered_list(self):

        localctx = LatexParser.Numbered_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numbered_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(LatexParser.ENUM_START)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 110
                self.text()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 116
                self.item()
                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LatexParser.ITEM):
                    break

            self.state = 121
            self.match(LatexParser.ENUM_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIST_START(self):
            return self.getToken(LatexParser.LIST_START, 0)

        def LIST_END(self):
            return self.getToken(LatexParser.LIST_END, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.ItemContext)
            else:
                return self.getTypedRuleContext(LatexParser.ItemContext,i)


        def getRuleIndex(self):
            return LatexParser.RULE_itemize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemize" ):
                listener.enterItemize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemize" ):
                listener.exitItemize(self)




    def itemize(self):

        localctx = LatexParser.ItemizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_itemize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(LatexParser.LIST_START)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 124
                self.text()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.item()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LatexParser.ITEM):
                    break

            self.state = 135
            self.match(LatexParser.LIST_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ITEM(self):
            return self.getToken(LatexParser.ITEM, 0)

        def elementContent(self):
            return self.getTypedRuleContext(LatexParser.ElementContentContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = LatexParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(LatexParser.ITEM)
            self.state = 138
            self.elementContent()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE_START(self):
            return self.getToken(LatexParser.CODE_START, 0)

        def text(self):
            return self.getTypedRuleContext(LatexParser.TextContext,0)


        def CODE_END(self):
            return self.getToken(LatexParser.CODE_END, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)




    def code(self):

        localctx = LatexParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(LatexParser.CODE_START)
            self.state = 141
            self.text()
            self.state = 142
            self.match(LatexParser.CODE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





