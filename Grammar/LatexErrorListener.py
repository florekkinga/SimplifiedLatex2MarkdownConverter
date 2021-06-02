import sys
from antlr4.error.ErrorListener import ErrorListener


class LatexErrorListener(ErrorListener):

    def __init__(self):
        super(LatexErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("If you specifed an output file it has not been created.\n")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!")