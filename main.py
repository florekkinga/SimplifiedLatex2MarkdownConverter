from antlr4 import *
from Grammar.LatexLexer import LatexLexer
from Grammar.LatexParser import LatexParser
from Grammar.LatexDocumentVisitor import LatexDocumentVisitor
import sys


def main(argv):
    if len(sys.argv) > 1:
        prepared_file = prepare_input(argv[1])
        if len(sys.argv) > 2:
            output_name = argv[2]
        else:
            output_name = None
        lexer = LatexLexer(InputStream(prepared_file))
        stream = CommonTokenStream(lexer)
        parser = LatexParser(stream)
        tree = parser.latexDocument()
        markdown_file = LatexDocumentVisitor(output_name).visit(tree)
        print("Latex document content in Markdown: \n" + markdown_file)
    else:
        print('Error : Expected a valid file')

def prepare_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        while "\\begin{document}" not in lines[0]:
            lines.pop(0)
        return ''.join(lines)

# run, paste one example from examples.txt, and click ^D
if __name__ == '__main__':
    main(sys.argv)
