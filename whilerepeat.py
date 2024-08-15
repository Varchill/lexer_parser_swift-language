import ply.lex as lex
import ply.yacc as yacc

# Define the list of tokens
tokens = (
    'IDENTIFIER',
    'WHILE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'EQUAL',
)

# Define regular expressions for tokens
def t_WHILE(t):
    r'while'
    return t

def t_LPAREN(t):
    r'\('
    return t

def t_RPAREN(t):
    r'\)'
    return t

def t_LBRACE(t):
    r'{'
    return t

def t_RBRACE(t):
    r'}'
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_ignore_COMMENT(t):
    r'\/\/.*'
    pass

t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

# Error handling for invalid characters
def t_error(t):
    print(f"Invalid character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the grammar rules
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

def p_expression(p):
    '''expression : IDENTIFIER EQUAL IDENTIFIER
                  | IDENTIFIER'''
    p[0] = p[1]
    if len(p) == 4:
        p[0] = p[1] + p[2] + p[3]

def p_statements(p):
    '''statements : statement statements
                  | empty'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = ''

def p_statement(p):
    '''statement : while_statement
                 | expression SEMICOLON'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = ''

# Error handling for syntax errors
def p_error(p):
    print(f"Syntax error at line {p.lineno}: {p.value}")

# Build the parser
parser = yacc.yacc()

# Sample input to be parsed
input_code = """
while (x == 10) {
    y = x * 2;
    x = x + 1;
}
"""

# Parse the input code
result = parser.parse(input_code)
if result:
    print("Input code is valid.")
else:
    print("There is an error")
