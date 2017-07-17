''' 
lexical analyzer
input   :source code
output  :words list
'''
from Error import ErrorType
from Token import Token
from Token import Place

def lex_analyzer(line,line_no):
    ''' 
    词法分析器
    '''
    print(line)
    i = 0
    '''
    for ch in line:
        print("character %d"%i,ch,line[i])
        i = i + 1
    i = 0
    '''
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
    if is_letter(line[i]):
        str_token = str_token + line[i]
        i = i + 1
        while is_letter(line[i]) or is_digit(line[i]):
            str_token = str_token + line[i]
            i = i + 1
        if check_reserve_word(str_token) != -1:
            print("%s是保留字"%str_token, check_reserve_word(str_token))
        elif line[i] == ' ':
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
        i = check_operator(line, i)
    else:
        print("line %d Error：字符格式错误！"%line_no)
    return i
def check_operator(line, i):
    '''
    解析运算符
    '''
    if line[i] == '+':
        print("操作符：+")
    elif line[i] == '-':
        print("操作符：-")
    elif line[i] == '*':
        print("操作符：*")
    elif line[i] == '=':
        print("操作符：=")
    elif line[i] == '<':
        print("操作符：<")
    elif line[i] == '>':
        print("操作符：>")
    elif line[i] == '!':
        print("操作符：!")
    elif line[i] == ';':
        print("分隔符：;")
    elif line[i] == '[':
        print("操作符：[")
    elif line[i] == ']':
        print("操作符：]")
    elif line[i] == '(':
        print("操作符：(")
    elif line[i] == ')':
        print("操作符：)")
    elif line[i] == '{':
        print("操作符：{")
    elif line[i] == '}':
        print("操作符：}")
    return i

def is_operator(char):
    '''
    确定是否为运算符
    '''
    operator_dict = ['+', '-', '*', '=', '<', '>', '!', '[', ']', '(', ')', '{', '}', ';']
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
