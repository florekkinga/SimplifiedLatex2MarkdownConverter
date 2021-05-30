parser grammar LatexParser;

options { tokenVocab=LatexLexer; }

latexDocument
    :
    DOCUMENT_START documentContent DOCUMENT_END
    ;

documentContent
    :
    text? (latexElement text?)*
    ;

text
    : TEXT
    | WHITESPACE
    ;

latexElement
    : BOLD_OPEN text* (latexElement text?)* COMMAND_CLOSE
    ;
