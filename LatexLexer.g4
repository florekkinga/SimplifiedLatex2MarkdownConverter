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
    : '\\begin{table}' '[]'? WHITESPACE? '\\begin{tabular}'
    ;

TABLE_ALIGN
    : '{' ('|'? [lrc] '|'?)+ COMMAND_CLOSE
    ;

TABLE_END
    : WHITESPACE? '\\end{tabular}' WHITESPACE? '\\end{table}'
    ;
