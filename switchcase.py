import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    'WHILE',
    'REPEAT',
    'LBRACE',
    'RBRACE',
)

# Define token regex patterns
def t_WHILE(t):
    r'while'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t

# Ignore whitespace and newline characters
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define the context-free grammar
def p_while_repeat(p):
    '''
    while_repeat : WHILE LBRACE REPEAT RBRACE
    '''
    print("Valid 'while repeat' construct")

# Error handling for parsing
def p_error(p):
    print("Syntax error in input")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Example input
input_string = "while { repeat }"

# Parsing the input
parser.parse(input_string)