# Generated from Grammar/LatexParser.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("\u00bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\2\3\3\7\3,\n\3\f\3\16\3/\13\3\3\3\3\3\7")
        buf.write("\3\63\n\3\f\3\16\3\66\13\3\7\38\n\3\f\3\16\3;\13\3\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J")
        buf.write("\n\5\3\6\7\6M\n\6\f\6\16\6P\13\6\3\6\3\6\7\6T\n\6\f\6")
        buf.write("\16\6W\13\6\7\6Y\n\6\f\6\16\6\\\13\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7e\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\7\r}\n\r\f\r\16\r\u0080\13\r\3\r\6\r\u0083\n\r\r")
        buf.write("\r\16\r\u0084\3\r\3\r\3\16\3\16\7\16\u008b\n\16\f\16\16")
        buf.write("\16\u008e\13\16\3\16\6\16\u0091\n\16\r\16\16\16\u0092")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00a3\n\21\f\21\16\21\u00a6\13\21")
        buf.write("\3\21\3\21\5\21\u00aa\n\21\3\21\5\21\u00ad\n\21\6\21\u00af")
        buf.write("\n\21\r\21\16\21\u00b0\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\2\2\24\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$\2\3\3\2\5\7\2\u00ca\2&\3")
        buf.write("\2\2\2\4-\3\2\2\2\6<\3\2\2\2\bI\3\2\2\2\nN\3\2\2\2\fd")
        buf.write("\3\2\2\2\16f\3\2\2\2\20j\3\2\2\2\22n\3\2\2\2\24r\3\2\2")
        buf.write("\2\26v\3\2\2\2\30z\3\2\2\2\32\u0088\3\2\2\2\34\u0096\3")
        buf.write("\2\2\2\36\u0099\3\2\2\2 \u009d\3\2\2\2\"\u00b4\3\2\2\2")
        buf.write("$\u00b8\3\2\2\2&\'\7\3\2\2\'(\5\4\3\2()\7\4\2\2)\3\3\2")
        buf.write("\2\2*,\5\6\4\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2")
        buf.write(".9\3\2\2\2/-\3\2\2\2\60\64\5\b\5\2\61\63\5\6\4\2\62\61")
        buf.write("\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("8\3\2\2\2\66\64\3\2\2\2\67\60\3\2\2\28;\3\2\2\29\67\3")
        buf.write("\2\2\29:\3\2\2\2:\5\3\2\2\2;9\3\2\2\2<=\t\2\2\2=\7\3\2")
        buf.write("\2\2>J\5\16\b\2?J\5\20\t\2@J\5\22\n\2AJ\5\24\13\2BJ\5")
        buf.write("\26\f\2CJ\5\30\r\2DJ\5\32\16\2EJ\5\36\20\2FJ\5 \21\2G")
        buf.write("J\5\"\22\2HJ\5$\23\2I>\3\2\2\2I?\3\2\2\2I@\3\2\2\2IA\3")
        buf.write("\2\2\2IB\3\2\2\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2\2IF\3\2\2")
        buf.write("\2IG\3\2\2\2IH\3\2\2\2J\t\3\2\2\2KM\5\6\4\2LK\3\2\2\2")
        buf.write("MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OZ\3\2\2\2PN\3\2\2\2QU\5")
        buf.write("\f\7\2RT\5\6\4\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2")
        buf.write("\2VY\3\2\2\2WU\3\2\2\2XQ\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2")
        buf.write("Z[\3\2\2\2[\13\3\2\2\2\\Z\3\2\2\2]e\5\16\b\2^e\5\20\t")
        buf.write("\2_e\5\30\r\2`e\5\32\16\2ae\5\36\20\2be\5\"\22\2ce\5$")
        buf.write("\23\2d]\3\2\2\2d^\3\2\2\2d_\3\2\2\2d`\3\2\2\2da\3\2\2")
        buf.write("\2db\3\2\2\2dc\3\2\2\2e\r\3\2\2\2fg\7\t\2\2gh\5\n\6\2")
        buf.write("hi\7\b\2\2i\17\3\2\2\2jk\7\n\2\2kl\5\n\6\2lm\7\b\2\2m")
        buf.write("\21\3\2\2\2no\7\13\2\2op\5\6\4\2pq\7\b\2\2q\23\3\2\2\2")
        buf.write("rs\7\f\2\2st\5\6\4\2tu\7\b\2\2u\25\3\2\2\2vw\7\r\2\2w")
        buf.write("x\5\6\4\2xy\7\b\2\2y\27\3\2\2\2z~\7\16\2\2{}\5\6\4\2|")
        buf.write("{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\u0082")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0081\u0083\5\34\17\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7\17\2")
        buf.write("\2\u0087\31\3\2\2\2\u0088\u008c\7\20\2\2\u0089\u008b\5")
        buf.write("\6\4\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008f\u0091\5\34\17\2\u0090\u008f\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\7\21\2\2\u0095")
        buf.write("\33\3\2\2\2\u0096\u0097\7\22\2\2\u0097\u0098\5\n\6\2\u0098")
        buf.write("\35\3\2\2\2\u0099\u009a\7\23\2\2\u009a\u009b\5\6\4\2\u009b")
        buf.write("\u009c\7\24\2\2\u009c\37\3\2\2\2\u009d\u009e\7\25\2\2")
        buf.write("\u009e\u00ae\7\26\2\2\u009f\u00a4\5\6\4\2\u00a0\u00a1")
        buf.write("\7\27\2\2\u00a1\u00a3\5\6\4\2\u00a2\u00a0\3\2\2\2\u00a3")
        buf.write("\u00a6\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a9\7")
        buf.write("\6\2\2\u00a8\u00aa\7\7\2\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00ad\7\30\2\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2")
        buf.write("\u00ae\u009f\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3")
        buf.write("\7\31\2\2\u00b3!\3\2\2\2\u00b4\u00b5\7\32\2\2\u00b5\u00b6")
        buf.write("\5\6\4\2\u00b6\u00b7\7\b\2\2\u00b7#\3\2\2\2\u00b8\u00b9")
        buf.write("\7\33\2\2\u00b9\u00ba\5\6\4\2\u00ba\u00bb\7\34\2\2\u00bb")
        buf.write("\u00bc\5\6\4\2\u00bc\u00bd\7\b\2\2\u00bd%\3\2\2\2\22-")
        buf.write("\649INUZd~\u0084\u008c\u0092\u00a4\u00a9\u00ac\u00b0")
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
                     "'\\end{verbatim}'", "<INVALID>", "<INVALID>", "'&'", 
                     "'\\hline'", "<INVALID>", "'\\say{'", "'\\textcolor{'", 
                     "'}{'" ]

    symbolicNames = [ "<INVALID>", "DOCUMENT_START", "DOCUMENT_END", "TEXT", 
                      "LINE_END", "WHITESPACE", "COMMAND_CLOSE", "BOLD_OPEN", 
                      "ITALICS_OPEN", "HEADER1", "HEADER2", "HEADER3", "ENUM_START", 
                      "ENUM_END", "LIST_START", "LIST_END", "ITEM", "CODE_START", 
                      "CODE_END", "TABLE_START", "TABLE_ALIGN", "CELL_SEPARATOR", 
                      "HLINE", "TABLE_END", "QUOTE_START", "COLOR_START", 
                      "COLOR_MID" ]

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
    RULE_table = 15
    RULE_quote = 16
    RULE_color = 17

    ruleNames =  [ "latexDocument", "documentContent", "text", "latexElement", 
                   "elementContent", "latexNestedElement", "bold", "italics", 
                   "header1", "header2", "header3", "numbered_list", "itemize", 
                   "item", "code", "table", "quote", "color" ]

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
    TABLE_START=19
    TABLE_ALIGN=20
    CELL_SEPARATOR=21
    HLINE=22
    TABLE_END=23
    QUOTE_START=24
    COLOR_START=25
    COLOR_MID=26

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatexDocument" ):
                return visitor.visitLatexDocument(self)
            else:
                return visitor.visitChildren(self)




    def latexDocument(self):

        localctx = LatexParser.LatexDocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_latexDocument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(LatexParser.DOCUMENT_START)
            self.state = 37
            self.documentContent()
            self.state = 38
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocumentContent" ):
                return visitor.visitDocumentContent(self)
            else:
                return visitor.visitChildren(self)




    def documentContent(self):

        localctx = LatexParser.DocumentContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_documentContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 40
                self.text()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.BOLD_OPEN) | (1 << LatexParser.ITALICS_OPEN) | (1 << LatexParser.HEADER1) | (1 << LatexParser.HEADER2) | (1 << LatexParser.HEADER3) | (1 << LatexParser.ENUM_START) | (1 << LatexParser.LIST_START) | (1 << LatexParser.CODE_START) | (1 << LatexParser.TABLE_START) | (1 << LatexParser.QUOTE_START) | (1 << LatexParser.COLOR_START))) != 0):
                self.state = 46
                self.latexElement()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                    self.state = 47
                    self.text()
                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)




    def text(self):

        localctx = LatexParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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


        def table(self):
            return self.getTypedRuleContext(LatexParser.TableContext,0)


        def quote(self):
            return self.getTypedRuleContext(LatexParser.QuoteContext,0)


        def color(self):
            return self.getTypedRuleContext(LatexParser.ColorContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_latexElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatexElement" ):
                listener.enterLatexElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatexElement" ):
                listener.exitLatexElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatexElement" ):
                return visitor.visitLatexElement(self)
            else:
                return visitor.visitChildren(self)




    def latexElement(self):

        localctx = LatexParser.LatexElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_latexElement)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatexParser.BOLD_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.bold()
                pass
            elif token in [LatexParser.ITALICS_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.italics()
                pass
            elif token in [LatexParser.HEADER1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.header1()
                pass
            elif token in [LatexParser.HEADER2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.header2()
                pass
            elif token in [LatexParser.HEADER3]:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.header3()
                pass
            elif token in [LatexParser.ENUM_START]:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.numbered_list()
                pass
            elif token in [LatexParser.LIST_START]:
                self.enterOuterAlt(localctx, 7)
                self.state = 66
                self.itemize()
                pass
            elif token in [LatexParser.CODE_START]:
                self.enterOuterAlt(localctx, 8)
                self.state = 67
                self.code()
                pass
            elif token in [LatexParser.TABLE_START]:
                self.enterOuterAlt(localctx, 9)
                self.state = 68
                self.table()
                pass
            elif token in [LatexParser.QUOTE_START]:
                self.enterOuterAlt(localctx, 10)
                self.state = 69
                self.quote()
                pass
            elif token in [LatexParser.COLOR_START]:
                self.enterOuterAlt(localctx, 11)
                self.state = 70
                self.color()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementContent" ):
                return visitor.visitElementContent(self)
            else:
                return visitor.visitChildren(self)




    def elementContent(self):

        localctx = LatexParser.ElementContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elementContent)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 73
                self.text()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.BOLD_OPEN) | (1 << LatexParser.ITALICS_OPEN) | (1 << LatexParser.ENUM_START) | (1 << LatexParser.LIST_START) | (1 << LatexParser.CODE_START) | (1 << LatexParser.QUOTE_START) | (1 << LatexParser.COLOR_START))) != 0):
                self.state = 79
                self.latexNestedElement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                    self.state = 80
                    self.text()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 90
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


        def quote(self):
            return self.getTypedRuleContext(LatexParser.QuoteContext,0)


        def color(self):
            return self.getTypedRuleContext(LatexParser.ColorContext,0)


        def getRuleIndex(self):
            return LatexParser.RULE_latexNestedElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatexNestedElement" ):
                listener.enterLatexNestedElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatexNestedElement" ):
                listener.exitLatexNestedElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatexNestedElement" ):
                return visitor.visitLatexNestedElement(self)
            else:
                return visitor.visitChildren(self)




    def latexNestedElement(self):

        localctx = LatexParser.LatexNestedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_latexNestedElement)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LatexParser.BOLD_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.bold()
                pass
            elif token in [LatexParser.ITALICS_OPEN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.italics()
                pass
            elif token in [LatexParser.ENUM_START]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.numbered_list()
                pass
            elif token in [LatexParser.LIST_START]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.itemize()
                pass
            elif token in [LatexParser.CODE_START]:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.code()
                pass
            elif token in [LatexParser.QUOTE_START]:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.quote()
                pass
            elif token in [LatexParser.COLOR_START]:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.color()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBold" ):
                return visitor.visitBold(self)
            else:
                return visitor.visitChildren(self)




    def bold(self):

        localctx = LatexParser.BoldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bold)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LatexParser.BOLD_OPEN)
            self.state = 101
            self.elementContent()
            self.state = 102
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItalics" ):
                return visitor.visitItalics(self)
            else:
                return visitor.visitChildren(self)




    def italics(self):

        localctx = LatexParser.ItalicsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_italics)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(LatexParser.ITALICS_OPEN)
            self.state = 105
            self.elementContent()
            self.state = 106
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader1" ):
                return visitor.visitHeader1(self)
            else:
                return visitor.visitChildren(self)




    def header1(self):

        localctx = LatexParser.Header1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_header1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(LatexParser.HEADER1)
            self.state = 109
            self.text()
            self.state = 110
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

        def HEADER2(self):
            return self.getToken(LatexParser.HEADER2, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader2" ):
                return visitor.visitHeader2(self)
            else:
                return visitor.visitChildren(self)




    def header2(self):

        localctx = LatexParser.Header2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_header2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LatexParser.HEADER2)
            self.state = 113
            self.text()
            self.state = 114
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

        def HEADER3(self):
            return self.getToken(LatexParser.HEADER3, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader3" ):
                return visitor.visitHeader3(self)
            else:
                return visitor.visitChildren(self)




    def header3(self):

        localctx = LatexParser.Header3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_header3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(LatexParser.HEADER3)
            self.state = 117
            self.text()
            self.state = 118
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumbered_list" ):
                return visitor.visitNumbered_list(self)
            else:
                return visitor.visitChildren(self)




    def numbered_list(self):

        localctx = LatexParser.Numbered_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numbered_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(LatexParser.ENUM_START)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 121
                self.text()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.item()
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LatexParser.ITEM):
                    break

            self.state = 132
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemize" ):
                return visitor.visitItemize(self)
            else:
                return visitor.visitChildren(self)




    def itemize(self):

        localctx = LatexParser.ItemizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_itemize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(LatexParser.LIST_START)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0):
                self.state = 135
                self.text()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 141
                self.item()
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==LatexParser.ITEM):
                    break

            self.state = 146
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = LatexParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(LatexParser.ITEM)
            self.state = 149
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = LatexParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(LatexParser.CODE_START)
            self.state = 152
            self.text()
            self.state = 153
            self.match(LatexParser.CODE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABLE_START(self):
            return self.getToken(LatexParser.TABLE_START, 0)

        def TABLE_ALIGN(self):
            return self.getToken(LatexParser.TABLE_ALIGN, 0)

        def TABLE_END(self):
            return self.getToken(LatexParser.TABLE_END, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def LINE_END(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.LINE_END)
            else:
                return self.getToken(LatexParser.LINE_END, i)

        def CELL_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.CELL_SEPARATOR)
            else:
                return self.getToken(LatexParser.CELL_SEPARATOR, i)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.WHITESPACE)
            else:
                return self.getToken(LatexParser.WHITESPACE, i)

        def HLINE(self, i:int=None):
            if i is None:
                return self.getTokens(LatexParser.HLINE)
            else:
                return self.getToken(LatexParser.HLINE, i)

        def getRuleIndex(self):
            return LatexParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable" ):
                return visitor.visitTable(self)
            else:
                return visitor.visitChildren(self)




    def table(self):

        localctx = LatexParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_table)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LatexParser.TABLE_START)
            self.state = 156
            self.match(LatexParser.TABLE_ALIGN)
            self.state = 172 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 157
                self.text()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LatexParser.CELL_SEPARATOR:
                    self.state = 158
                    self.match(LatexParser.CELL_SEPARATOR)
                    self.state = 159
                    self.text()
                    self.state = 164
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 165
                self.match(LatexParser.LINE_END)
                self.state = 167
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 166
                    self.match(LatexParser.WHITESPACE)


                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LatexParser.HLINE:
                    self.state = 169
                    self.match(LatexParser.HLINE)


                self.state = 174 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LatexParser.TEXT) | (1 << LatexParser.LINE_END) | (1 << LatexParser.WHITESPACE))) != 0)):
                    break

            self.state = 176
            self.match(LatexParser.TABLE_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuoteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTE_START(self):
            return self.getToken(LatexParser.QUOTE_START, 0)

        def text(self):
            return self.getTypedRuleContext(LatexParser.TextContext,0)


        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuote" ):
                listener.enterQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuote" ):
                listener.exitQuote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuote" ):
                return visitor.visitQuote(self)
            else:
                return visitor.visitChildren(self)




    def quote(self):

        localctx = LatexParser.QuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_quote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(LatexParser.QUOTE_START)
            self.state = 179
            self.text()
            self.state = 180
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR_START(self):
            return self.getToken(LatexParser.COLOR_START, 0)

        def text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LatexParser.TextContext)
            else:
                return self.getTypedRuleContext(LatexParser.TextContext,i)


        def COLOR_MID(self):
            return self.getToken(LatexParser.COLOR_MID, 0)

        def COMMAND_CLOSE(self):
            return self.getToken(LatexParser.COMMAND_CLOSE, 0)

        def getRuleIndex(self):
            return LatexParser.RULE_color

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColor" ):
                listener.enterColor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColor" ):
                listener.exitColor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColor" ):
                return visitor.visitColor(self)
            else:
                return visitor.visitChildren(self)




    def color(self):

        localctx = LatexParser.ColorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_color)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(LatexParser.COLOR_START)
            self.state = 183
            self.text()
            self.state = 184
            self.match(LatexParser.COLOR_MID)
            self.state = 185
            self.text()
            self.state = 186
            self.match(LatexParser.COMMAND_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





