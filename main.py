from antlr4 import *
from LatexLexer import LatexLexer
from LatexParserListener import LatexParserListener
from LatexParser import LatexParser
import sys

class printListener(LatexParserListener):
    def enterLatexDocument(self, ctx: LatexParser.LatexDocumentContext):
        print(ctx.documentContent()) # nie do konca rozumiem czym jest te kontekst, bo mozna printować tylko tokeny a nie nazwe jakiejs produkcji

    def enterText(self, ctx:LatexParser.TextContext): # printuje kazdy znaleziony token text
        print(ctx.TEXT())

    def enterCode(self, ctx:LatexParser.CodeContext):
        print(ctx.text().TEXT()) # printuje kazdy znaleziony token text w środku bloku code


def main():
    lexer = LatexLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    tree = parser.latexDocument()
    printer = printListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

# aby uruchomić klikacie run, potem wklejacie tesktowo jakis przyklad i ^D
if __name__ == '__main__':
    main()
