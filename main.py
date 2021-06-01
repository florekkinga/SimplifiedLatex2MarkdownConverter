from antlr4 import *
from Grammar.LatexLexer import LatexLexer
from Grammar.LatexParser import LatexParser
from Grammar.LatexDocumentVisitor import LatexDocumentVisitor
from Grammar.LatexErrorListener import LatexErrorListener
import sys

options = """
-f, --file  specify input file path
-o, --out   specify output file path
While all of those options are optional, they must be used in this order.
"""


def main(argv):
    if len(sys.argv) > 2 and (argv[1] == "-f" or argv[1] == "--file"):
        launch_from_file(argv)
    elif len(sys.argv) == 1 or (len(sys.argv) > 2 and (argv[1] == "-o" or argv[1] == "--out")):
        launch_from_paste(argv)
    else:
        print('Error : Invalid command syntax. Available options:', options)


def launch_from_file(argv):
    prepared_file = prepare_input(argv[2])
    if len(sys.argv) > 4 and (argv[3] == "-o" or argv[3] == "--output"):
        output_name = argv[4]
    else:
        output_name = None
    lexer = LatexLexer(InputStream(prepared_file))
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    parser.addErrorListener(LatexErrorListener())
    tree = parser.latexDocument()
    markdown_file = LatexDocumentVisitor(output_name).visit(tree)
    print("Latex document content in Markdown: \n" + markdown_file)


def prepare_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        while "\\begin{document}" not in lines[0]:
            lines.pop(0)
        return ''.join(lines)


def launch_from_paste(argv):
    if len(sys.argv) > 2 and (argv[1] == "-o" or argv[1] == "--output"):
        output_name = argv[2]
    else:
        output_name = None

    print("Paste your LaTeX document contents (without preamble) and enter EOF:\n")
    lexer = LatexLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    parser.addErrorListener(LatexErrorListener())
    tree = parser.latexDocument()
    markdown_file = LatexDocumentVisitor(output_name).visit(tree)
    print("Latex document content in Markdown: \n" + markdown_file)


# run, paste one example from examples.txt, and click ^D
if __name__ == '__main__':
    main(sys.argv)
