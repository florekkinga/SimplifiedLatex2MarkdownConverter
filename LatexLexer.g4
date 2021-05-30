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
    : '\\section'
    ;

HEADER2
    : '\\subsection'
    ;

HEADER3
    : '\\subsubsection'
    ;

ENUM_START
    : '\\begin{enumerate}'
    ;

ENUM_END
    : '\\end{enumerate}'
    ;

ITEM
    : '\\item'
    ;

