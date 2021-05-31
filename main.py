from antlr4 import *
from LatexLexer import LatexLexer
from LatexParser import LatexParser
from LatexDocumentVisitor import LatexDocumentVisitor
import sys


def main(argv):
    if len(sys.argv) > 1:
        input = FileStream(argv[1])
        lexer = LatexLexer(input)
        stream = CommonTokenStream(lexer)
        parser = LatexParser(stream)
        tree = parser.latexDocument()
        markdown_file = LatexDocumentVisitor().visit(tree)
        print("Latex document content in Markdown: \n" + markdown_file)
    else:
        print('Error : Expected a valid file')


# run, paste one example from examples.txt, and click ^D
if __name__ == '__main__':
    main(sys.argv)
