from antlr4 import *
from Grammar.LatexLexer import LatexLexer
from Grammar.LatexParser import LatexParser
from Grammar.LatexDocumentVisitor import LatexDocumentVisitor
from Grammar.LatexErrorListener import LatexErrorListener
import sys

options = """
This command is used to conver TeX into MarkDown.
Usage:
    = To run, read TeX from console (without preamble) and output MarkDown into console:
        python main.py
    = Available options allow reading input from console and outputting MarkDown into file

-h, --help      display this text
-f, --file      specify input file path
-o, --out       specify output file path
-i, --inline    use inline HTML in output file. If not used every command that would need to be converted to inline HTML is omitted (text is left in output). Ex: \\textcolor{color}{text}.
-s, --silent    silence console MarkDown output. Will impact the command only if output file is specified with -o or --out. Will still print information about output file.
"""

options_list = ["-h", "--help", "-f", "--file", "-o", "--out", "-i", "--inline", "-s", "--silent"]

def main(argv):
    if not all(item in options_list for item in argv if item[0] == '-'):
        print("Invalid option used. Available options:", options)
        return
    
    if len(argv) > 1 and argv[1] not in options_list:
        print("Invalid usage. Refer to -h or --help for more info.")

    try:
        if "-h" in argv or "--help" in argv:
            print("Available options:", options)
        elif "-f" in argv or "--file" in argv:
            launch_from_file(argv)
        else:
            launch_from_paste(argv)
    except IndexError:
        print("One or more of used options needs a value specified. Refer to -h or --help for more info.")


def launch_from_file(argv):
    try:
        f_index = argv.index('-f') + 1
    except ValueError:
        f_index = argv.index('--file') + 1
    prepared_file = prepare_input(argv[f_index])

    output_name = get_output_name(argv)
    inline_html = ("-i" in argv or "--inline" in argv)

    lexer = LatexLexer(InputStream(prepared_file))
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    parser.addErrorListener(LatexErrorListener())
    tree = parser.latexDocument()
    markdown_file = LatexDocumentVisitor(output_name, inline_html).visit(tree)
    if ("-s" not in argv and "--silent" not in argv) or output_name == None:
        print("Latex document content in Markdown: \n" + markdown_file)


def prepare_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        while "\\begin{document}" not in lines[0]:
            lines.pop(0)
        return ''.join(lines)


def launch_from_paste(argv):
    output_name = get_output_name(argv)
    inline_html = ("-i" in argv or "--inline" in argv)

    print("Paste your LaTeX document contents (without preamble) and enter EOF:\n")
    lexer = LatexLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LatexParser(stream)
    parser.addErrorListener(LatexErrorListener())
    tree = parser.latexDocument()
    markdown_file = LatexDocumentVisitor(output_name, inline_html).visit(tree)
    if ("-s" not in argv and "--silent" not in argv) or output_name == None:
        print("Latex document content in Markdown: \n" + markdown_file)


def get_output_name(argv):
    if "-o" in argv or "--out" in argv:
        return extract_name(argv)
    else:
        return None


def extract_name(argv):
    try:
        o_index = argv.index('-o') + 1
    except ValueError:
        o_index = argv.index('--out') + 1
    return argv[o_index]


# run, paste one example from examples.txt, and click ^D
if __name__ == '__main__':
    main(sys.argv)
