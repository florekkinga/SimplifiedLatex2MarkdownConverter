lexer grammar LatexLexer;

// tokens
BOLD_OPEN
    : '\\textbf{' -> pushMode(COMMAND)
    ;
DOCUMENT_START
    : '\\begin{document}' -> pushMode(DOCUMENT);

TEXT
    :
    ~[\\}]+
    ;

WHITESPACE
    :  (' '|'\t'|'\r'? '\n')+
    ;

mode COMMAND;
COMMAND_CLOSE
    : '}' -> popMode
    ;

mode DOCUMENT;
DOCUMENT_END
    : '\\end{document}' -> popMode;



//USER_TEXT : \s*\(?(?<![\\beginendtextbf])(\b(?!document\b)\w+)[',:)-.]*[\s\n]*;

