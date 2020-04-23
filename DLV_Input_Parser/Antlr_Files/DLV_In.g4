grammar DLV_In;

options {
    language = Python3;
}


// Parser Rules


dlv_file : (dlv_rule)* ;

dlv_rule : ( fact | head_tail_rule | ic ) '.' ;

fact: positive_atom ;

head_tail_rule : head tail ;

ic : tail ;

head : ( positive_atom ';' )* positive_atom ;

tail :  ':-' ( (positive_atom|negative_atom) ',' )* (positive_atom|negative_atom) ;

positive_atom : atom ;

negative_atom : 'not' atom ;

atom : TEXT ('(' atom_content ')')? ;

atom_content: ( ( atom_text | atom ) ',' )* ( atom_text | atom ) ;

atom_text: TEXT ;





// Lexer Rules

TEXT: [a-zA-Z0-9_"]+ ;

WHITESPACE : ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+ -> skip ;