from antlr4 import *
from LatexLexer import LatexLexer
from LatexParser import LatexParser
from LatexParserListener import LatexParserListener
from LatexParserVisitor import LatexParserVisitor
from MarkdownFile import MarkdownFile


class PrintListener(LatexParserListener):

    # prints every occurrence of documentContent token/rule
    def enterLatexDocument(self, ctx: LatexParser.LatexDocumentContext):
        print("document content: \n" + ctx.documentContent().getText())

    # prints every occurrence of text token/rule
    def enterText(self, ctx: LatexParser.TextContext):
        print("text token: " + ctx.getText())

    # prints every occurrence of text token/rule inside code rule
    def enterCode(self, ctx: LatexParser.CodeContext):
        print("text inside code command: " + ctx.text().getText())


class LatexDocumentVisitor(LatexParserVisitor):
    def visitLatexDocument(self, ctx: LatexParser.LatexDocumentContext):
        text = self.visit(ctx.documentContent())
        return MarkdownFile(text).generate()

    def visitDocumentContent(self, ctx: LatexParser.DocumentContentContext):
        return self.visitChildren(ctx)

    def visitLatexElement(self, ctx: LatexParser.LatexElementContext):
        return self.visitChildren(ctx)

    def visitHeader1(self, ctx: LatexParser.Header1Context):
        header1 = '# ' + ctx.text().getText() + '\n'
        return header1

    def visitBold(self, ctx: LatexParser.BoldContext):
        bold = '**' + ctx.elementContent().getText() + '**'
        return bold

    def visitText(self, ctx: LatexParser.TextContext):
        return ctx.getText()

    def visitChildren(self, ctx):
        elements = []
        for child in ctx.children:
            elements.append(self.visit(child))
        content = ''.join(elements)
        return content


def main():
    lexer = LatexLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    tree = parser.latexDocument()
    # printer = PrintListener() -> for version with listener
    # walker = ParseTreeWalker() -> for version with listener
    # walker.walk(printer, tree) -> for version with listener
    markdown_file = LatexDocumentVisitor().visit(tree)  # -> visitor version
    print("Latex document content in Markdown: \n")
    print(markdown_file)  # -> visitor version


# run, paste the content of example.txt, and click ^D
if __name__ == '__main__':
    main()
