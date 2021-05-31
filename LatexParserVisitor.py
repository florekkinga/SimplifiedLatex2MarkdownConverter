# Generated from LatexParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatexParser import LatexParser
else:
    from LatexParser import LatexParser

# This class defines a complete generic visitor for a parse tree produced by LatexParser.

class LatexParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatexParser#latexDocument.
    def visitLatexDocument(self, ctx:LatexParser.LatexDocumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#documentContent.
    def visitDocumentContent(self, ctx:LatexParser.DocumentContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#text.
    def visitText(self, ctx:LatexParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#latexElement.
    def visitLatexElement(self, ctx:LatexParser.LatexElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#elementContent.
    def visitElementContent(self, ctx:LatexParser.ElementContentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#latexNestedElement.
    def visitLatexNestedElement(self, ctx:LatexParser.LatexNestedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#bold.
    def visitBold(self, ctx:LatexParser.BoldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#italics.
    def visitItalics(self, ctx:LatexParser.ItalicsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#header1.
    def visitHeader1(self, ctx:LatexParser.Header1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#header2.
    def visitHeader2(self, ctx:LatexParser.Header2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#header3.
    def visitHeader3(self, ctx:LatexParser.Header3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#numbered_list.
    def visitNumbered_list(self, ctx:LatexParser.Numbered_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#itemize.
    def visitItemize(self, ctx:LatexParser.ItemizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#item.
    def visitItem(self, ctx:LatexParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#code.
    def visitCode(self, ctx:LatexParser.CodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatexParser#table.
    def visitTable(self, ctx:LatexParser.TableContext):
        return self.visitChildren(ctx)



del LatexParser