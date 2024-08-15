import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'CASE',
    'COLON',
    'DEFAULT',
    'IDENTIFIER',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
)

# Regular expressions for tokens
def t_CASE(t):
    r'case'
    return t

def t_COLON(t):
    r':'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
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

def t_SEMICOLON(t):
    r';'
    return t

# Ignored characters
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Invalid character: '{t.value[0]}'")
    t.lexer.skip(1)

# Define a simple context-free grammar
def p_switch_case(p):
    '''
    switch_case : CASE IDENTIFIER COLON cases DEFAULT COLON IDENTIFIER COLON cases
    '''
    print("Valid switch-case construct")

def p_cases(p):
    '''
    cases : case_list
          | empty
    '''

def p_case_list(p):
    '''
    case_list : IDENTIFIER COLON statements case_list
    '''

def p_statements(p):
    '''
    statements : LBRACE RBRACE
               | LBRACE IDENTIFIER RBRACE
    '''

def p_empty(p):
    '''
    empty :
    '''

# Error handling
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

# Input Swift 'switch case' construct
input_swift_code = """
switch color {
    case "red":
        print("It's red")
    case "green":
        print("It's green")
    default:
        print("Unknown color")
}
"""

# Parsing
lexer.input(input_swift_code)
for token in lexer:
    pass

result = parser.parse(input_swift_code)