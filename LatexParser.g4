parser grammar LatexParser;

options { tokenVocab=LatexLexer; }

latexDocument
    : DOCUMENT_START documentContent DOCUMENT_END
    ;

documentContent
    : text* (latexElement text*)*
    ;

text
    : TEXT
    | WHITESPACE
    | LINE_END
    ;

latexElement
    : bold
    | italics
    | header1
    | header2
    | header3
    | numbered_list
    | itemize
    | code
    ;

elementContent
    : text* (latexNestedElement text*)*
    ;

latexNestedElement
    : bold
    | italics
    | numbered_list
    | itemize
    | code
    ;

bold
    : BOLD_OPEN elementContent COMMAND_CLOSE
    ;

italics
    : ITALICS_OPEN elementContent COMMAND_CLOSE
    ;

header1
    : HEADER1 text COMMAND_CLOSE
    ;

header2
    : HEADER2 text COMMAND_CLOSE
    ;

header3
    : HEADER3 text COMMAND_CLOSE
    ;

numbered_list
    : ENUM_START text* item+ ENUM_END
    ;

itemize
    : LIST_START text* item+ LIST_END
    ;

item
    : ITEM elementContent
    ;

code
    : CODE_START text CODE_END
    ;

