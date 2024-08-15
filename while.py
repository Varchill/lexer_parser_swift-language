import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'FOR',
    'IN',
    'IDENTIFIER',
    'COLON',
    'LBRACE',
    'RBRACE',
    'COMMA',
)

# Define the regular expressions for tokens
def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_COLON(t):
    r':'
    return t
 
def t_LBRACE(t):
    r'{'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_COMMA(t):
    r','
    return t

# Ignore whitespace and newline characters
t_ignore = ' \t\n'

# Define error handling for invalid tokens
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Define the context-free grammar rules
def p_for_each_construct(p):
    """
    for_each : FOR IDENTIFIER IN IDENTIFIER COLON LBRACE RBRACE
    """
    print("Valid for_each construct")

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: End of input reached unexpectedly")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Test the parser
if __name__ == "__main__":
    data = "for item in list: {}"
    lexer.input(data)
    for token in lexer:
        print(token)
    
    result = parser.parse(data)