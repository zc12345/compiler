from Token import Place,Token
def is_operator(char):
    '''
    检查是否为运算符
    '''
    operator_dict = ['+', '-', '*', '=', '<', '>', '!', '[', ']', '(', ')', '{', '}', ';', '&', '|']
    for operator in operator_dict:
        if operator == char:
            return True
    return False

def is_letter(char):
    '''
    检查是否是字母
    '''
    if (char <= 'z' and char >= 'a') or (char <= 'Z' and char >= 'A'):
        return True
    else:
        return False

def is_digit(char):
    '''
    检查是否是数字
    '''
    if char <= '9' and char >= '0':
        return True
    else:
        return False

def check_reserve_word(str):
    '''
    检查是否是保留字
    '''
    reserve_dict = {'if':1, 'then':2, 'else':3, 'do':4, 'while':5,
                    'for':6, 'int':7, 'float':8, 'char':9, 'boolean':10,
                    'and':11, 'or':12, 'not':13, 'true':14, 'false':15,
                    'null':16}
    
    return reserve_dict.get(str, -1)

def check_operator(line, line_no, token_no, lptr, rptr):
    '''
    解析运算符
    '''
    operator_dict = {'+':"ADD", '-':"MINUS", '*':"MULTIPLY",#算术运算符 
                     '=':"EQU", '<':"LESS", '>':"MORE", '<=':"LESSEQU", '>=':"MOREEQU", '!=':"NOTEQU",#比较运算符 
                     '!':"NOT", '&&':"AND", '||':"OR", #布尔运算符
                     '[':"LSQU", ']':"RSQU", '(':"LPAR", ')':"RPAR",#界符 
                     '{':"LCUR", '}':"RCUR", ';':"SEP"}
    if rptr + 1 < len(line) and is_operator(line[rptr + 1]):
        rptr = rptr + 2
        op = line[lptr: rptr]
    else:
        rptr = rptr + 1
        op = line[lptr: rptr]
    place = Place(line_no, lptr, rptr)
    token = Token(token_no, "OPERATER", place, operator_dict.get(op, "NONE"))
    return token
