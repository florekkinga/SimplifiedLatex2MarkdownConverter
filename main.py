from antlr4 import *
from LatexLexer import LatexLexer
from LatexParser import LatexParser
from LatexDocumentVisitor import LatexDocumentVisitor


def main():
    lexer = LatexLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    tree = parser.latexDocument()
    markdown_file = LatexDocumentVisitor().visit(tree)
    print("Latex document content in Markdown: \n" + markdown_file)


# run, paste one example from examples.txt, and click ^D
if __name__ == '__main__':
    main()
