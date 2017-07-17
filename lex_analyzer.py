''' 
lexical analyzer
input   :source code
output  :words list
'''
from Error import ErrorType
from Token import Token
from Token import Place
from lex_check import is_digit,is_letter,is_operator,check_reserve_word

token_list = []
token_no = 0

def lex_input(input_program):
    line_no = 0
    for line in input_program:
        print("line%d"%line_no,line)
        if line[0] == '#':#跳过#开头的注释
            line_no = line_no + 1
            continue
        else:
            lex_analyzer(line, line_no)
            line_no = line_no + 1
    print("="*20,"源程序读取结束！","="*20)
    for token in token_list:
        print(token.print_token())


def lex_analyzer(line, line_no, *token_list):
    ''' 
    词法分析器
    '''
    print(line)
    i = 0
    while i < len(line):
        i = check_word(line, line_no, i)
        i = i + 1

def check_word(line, line_no, i):
    '''
    分割一个个关键字标识符和运算符
    标识符允许是字母开头的字母数字组合
    算术运算符: +, ++, -, --, *, =
    关系运算符: <, <=, >, >=, !=, ==
    布尔表达式: &&, ||, !
    '''
    str_token = ''
    global token_no
    '''
    当读入字母的时候，判断是标识符还是关键字
    '''
    if is_letter(line[i]):
        str_token = str_token + line[i]
        i = i + 1
        while is_letter(line[i]) or is_digit(line[i]):
            str_token = str_token + line[i]
            i = i + 1
        if check_reserve_word(str_token) != -1:
            #place = Place(line_no, i, i + 1)
            token_list.append(Token(token_no, "KEYWORD", line_no, str_token))
            token_no = token_no + 1
            print("%s是保留字"%str_token, check_reserve_word(str_token)) 
        elif line[i] == ' ':
            #place = Place(line_no, i, i + 1)
            token_list.append(Token(token_no, "IDENTIFIER", line_no, str_token))
            token_no = token_no + 1
            print("%s是标识符"%str_token, check_reserve_word(str_token))
        else:
            print("line:%d Error：标识符只能是字母开头的字母数字组合！"%line_no)
        i = i - 1
    elif is_digit(line[i]):
        while is_digit(line[i]):
            str_token = str_token + line[i]
            i = i + 1
        if is_letter(line[i]):
            print("line:%d Error：标识符只能以字母开头！"%line_no)
        elif line[i] == '.':#处理小数
            str_token = str_token + line[i]
            i = i + 1
            while is_digit(line[i]):
                str_token = str_token + line[i]
                i = i + 1
            if line[i] == ' ':
                value = float(str_token)
                print("%f是浮点数"%value)
            else:
                print("line:%d Error：字符格式错误"%line_no)
        elif line[i] == ' ':#处理整数
            value = int(str_token)
            print("%d是整数"%value)
        i = i - 1
    elif line[i] == ' ':
        print("空格")
    elif is_operator(line[i]):
        token = check_operator(line, i, line_no)
        token_no = token.get_no() + 1
        token_list.append(token)
    else:
        print("line %d Error：字符格式错误！"%line_no)
    return i
def check_operator(line, i, line_no):
    '''
    解析运算符
    '''
    operator_dict = {'+':"ADD", '-':"MINUS", '*':"MULTIPLY",#算术运算符 
                     '=':"EQU", '<':"LESS", '>':"MORE", '<=':"LESSEQU", '>=':"MOREEQU", '!=':"NOTEQU",#比较运算符 
                     '!':"NOT", '&&':"AND", '||':"OR", #布尔运算符
                     '[':"LSQU", ']':"RSQU", '(':"LPAR", ')':"RPAR",#界符 
                     '{':"LCUR", '}':"RCUR", ';':"SEP"}
    global token_no
    if is_operator(line[i+1]):
        op = line[i] + line[i + 1]
        i = i + 2
        print("！双运算符 ======",op)
    else:
        op = line[i]
        i = i + 1
    token = Token(token_no, "OPERATER", line_no, operator_dict.get(op, "NONE"))
    return token
