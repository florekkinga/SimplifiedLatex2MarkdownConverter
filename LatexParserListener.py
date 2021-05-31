# Generated from LatexParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete listener for a parse tree produced by LatexParser.
class LatexParserListener(ParseTreeListener):

    # Enter a parse tree produced by LatexParser#latexDocument.
    def enterLatexDocument(self, ctx:LatexParser.LatexDocumentContext):
        pass

    # Exit a parse tree produced by LatexParser#latexDocument.
    def exitLatexDocument(self, ctx:LatexParser.LatexDocumentContext):
        pass


    # Enter a parse tree produced by LatexParser#documentContent.
    def enterDocumentContent(self, ctx:LatexParser.DocumentContentContext):
        pass

    # Exit a parse tree produced by LatexParser#documentContent.
    def exitDocumentContent(self, ctx:LatexParser.DocumentContentContext):
        pass


    # Enter a parse tree produced by LatexParser#text.
    def enterText(self, ctx:LatexParser.TextContext):
        pass

    # Exit a parse tree produced by LatexParser#text.
    def exitText(self, ctx:LatexParser.TextContext):
        pass


    # Enter a parse tree produced by LatexParser#latexElement.
    def enterLatexElement(self, ctx:LatexParser.LatexElementContext):
        pass

    # Exit a parse tree produced by LatexParser#latexElement.
    def exitLatexElement(self, ctx:LatexParser.LatexElementContext):
        pass


    # Enter a parse tree produced by LatexParser#elementContent.
    def enterElementContent(self, ctx:LatexParser.ElementContentContext):
        pass

    # Exit a parse tree produced by LatexParser#elementContent.
    def exitElementContent(self, ctx:LatexParser.ElementContentContext):
        pass


    # Enter a parse tree produced by LatexParser#latexNestedElement.
    def enterLatexNestedElement(self, ctx:LatexParser.LatexNestedElementContext):
        pass

    # Exit a parse tree produced by LatexParser#latexNestedElement.
    def exitLatexNestedElement(self, ctx:LatexParser.LatexNestedElementContext):
        pass


    # Enter a parse tree produced by LatexParser#bold.
    def enterBold(self, ctx:LatexParser.BoldContext):
        pass

    # Exit a parse tree produced by LatexParser#bold.
    def exitBold(self, ctx:LatexParser.BoldContext):
        pass


    # Enter a parse tree produced by LatexParser#italics.
    def enterItalics(self, ctx:LatexParser.ItalicsContext):
        pass

    # Exit a parse tree produced by LatexParser#italics.
    def exitItalics(self, ctx:LatexParser.ItalicsContext):
        pass


    # Enter a parse tree produced by LatexParser#header1.
    def enterHeader1(self, ctx:LatexParser.Header1Context):
        pass

    # Exit a parse tree produced by LatexParser#header1.
    def exitHeader1(self, ctx:LatexParser.Header1Context):
        pass


    # Enter a parse tree produced by LatexParser#header2.
    def enterHeader2(self, ctx:LatexParser.Header2Context):
        pass

    # Exit a parse tree produced by LatexParser#header2.
    def exitHeader2(self, ctx:LatexParser.Header2Context):
        pass


    # Enter a parse tree produced by LatexParser#header3.
    def enterHeader3(self, ctx:LatexParser.Header3Context):
        pass

    # Exit a parse tree produced by LatexParser#header3.
    def exitHeader3(self, ctx:LatexParser.Header3Context):
        pass


    # Enter a parse tree produced by LatexParser#numbered_list.
    def enterNumbered_list(self, ctx:LatexParser.Numbered_listContext):
        pass

    # Exit a parse tree produced by LatexParser#numbered_list.
    def exitNumbered_list(self, ctx:LatexParser.Numbered_listContext):
        pass


    # Enter a parse tree produced by LatexParser#itemize.
    def enterItemize(self, ctx:LatexParser.ItemizeContext):
        pass

    # Exit a parse tree produced by LatexParser#itemize.
    def exitItemize(self, ctx:LatexParser.ItemizeContext):
        pass


    # Enter a parse tree produced by LatexParser#item.
    def enterItem(self, ctx:LatexParser.ItemContext):
        pass

    # Exit a parse tree produced by LatexParser#item.
    def exitItem(self, ctx:LatexParser.ItemContext):
        pass


    # Enter a parse tree produced by LatexParser#code.
    def enterCode(self, ctx:LatexParser.CodeContext):
        pass

    # Exit a parse tree produced by LatexParser#code.
    def exitCode(self, ctx:LatexParser.CodeContext):
        pass


    # Enter a parse tree produced by LatexParser#table.
    def enterTable(self, ctx:LatexParser.TableContext):
        pass

    # Exit a parse tree produced by LatexParser#table.
    def exitTable(self, ctx:LatexParser.TableContext):
        pass



del LatexParser