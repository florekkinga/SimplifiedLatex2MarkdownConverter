lexer grammar LatexLexer;

// tokens

DOCUMENT_START
    : '\\begin{document}'
    ;

DOCUMENT_END
    : '\\end{document}'
    ;

TEXT
    :
    ~[\\}]+
    ;

LINE_END
    : '\\\\'
    ;

WHITESPACE
    :  (' '|'\t'|'\r'? '\n')+
    ;

COMMAND_CLOSE
    : '}'
    ;

BOLD_OPEN
    : '\\textbf{'
    ;

ITALICS_OPEN
    : '\\textit{'
    ;

HEADER1
    : '\\section{'
    ;

HEADER2
    : '\\subsection{'
    ;

HEADER3
    : '\\subsubsection{'
    ;

ENUM_START
    : '\\begin{enumerate}'
    ;

ENUM_END
    : '\\end{enumerate}'
    ;

LIST_START
    : '\\begin{itemize}'
    ;

LIST_END
    : '\\end{itemize}'
    ;

ITEM
    : '\\item'
    ;

CODE_START
    : '\\begin{verbatim}'
    ;

CODE_END
    : '\\end{verbatim}'
    ;

TABLE_START
    : '\\begin{table}' '[]'? WHITESPACE? '\\begin{tabular}' '{' -> pushMode(COLUMNS)
    ;

TABLE_END
    : '\\end{tabular}' WHITESPACE? '\\end{table}'
    ;

mode COLUMNS;
COLUMNS_ALIGN
    : COLUMN_ALIGN+ COMMAND_CLOSE -> popMode
    ;

COLUMN_ALIGN
    : '|'? ALIGN_CHAR '|'?
    ;

ALIGN_CHAR
    : 'l'
    | 'r'
    | 'c'
    ;
