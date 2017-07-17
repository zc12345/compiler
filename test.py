''' 
lexical analyzer
input   :source code
output  :words list
'''
from Error import ErrorType
from Token import Token,Place
from lex_check import is_digit,is_letter,is_operator,check_reserve_word,check_operator

token_list = []
token_no = 0
flag_stack = []

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
    lptr = 0
    rptr = 0 #指针指向当前所读部分的左右边界
    while lptr < len(line) and rptr < len(line) and lptr <= rptr:
        place = check_word(line, line_no, lptr, rptr)
        lptr = place.get_lptr()
        rptr = place.get_rptr()

def check_word(line, line_no, lptr, rptr):
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
    if is_letter(line[rptr]):
        rptr = rptr + 1
        while is_letter(line[rptr]) or is_digit(line[rptr]):
            rptr = rptr + 1 #左指针不动，右指针不断右移，直到读取到的字符不再是字母或者数字
        str_token = line[lptr:rptr]
        if check_reserve_word(str_token) != -1:
            place = Place(line_no, lptr, rptr)#关键字
            token_list.append(Token(token_no, "KEYWORD", place, str_token))
            token_no = token_no + 1
            print("%s是保留字"%str_token, check_reserve_word(str_token)) 
        elif line[rptr] == ' ' or line[rptr] == ';' or line[rptr] == '=':
            place = Place(line_no, lptr, rptr)#标识符
            token_list.append(Token(token_no, "IDENTIFIER", place, str_token))
            token_no = token_no + 1
            print("%s是标识符"%str_token, check_reserve_word(str_token))
        else:
            print("line:%d Error：标识符只能是字母开头的字母数字组合！"%line_no)
        lptr = rptr #将左指针移动到右指针处，进行下一次切片取字符操作
    elif is_digit(line[rptr]):
        while is_digit(line[rptr]):
            rptr = rptr + 1
        str_token = line[lptr:rptr]
        if is_letter(line[rptr]):
            print("line:%d Error：标识符只能以字母开头！"%line_no)
        elif line[rptr] == '.':#处理小数
            rptr = rptr + 1
            while is_digit(line[rptr]):
                rptr = rptr + 1
            str_token = line[lptr: rptr]
            value = float(str_token)
            place = Place(line_no, lptr, rptr)
            token_list.append(Token(token_no, "LITERAL", place, str_token))
            token_no = token_no + 1
            print("%f是浮点数"%value)
            if not(line[rptr] == ' ' or line[rptr] == ';'):#小数只可能位于句尾
                print("line:%d Error：字符格式错误"%line_no)
        elif not(line[rptr] == ' ' or line[rptr] == ';' #位于句尾
                 or line[rptr] == ']' or line[rptr] == ','):#位于多维数组
            value = int(str_token)#处理整数
            place = Place(line_no, lptr, rptr)
            token_list.append(Token(token_no, "LITERAL", place, str_token))
            token_no = token_no + 1
            print("%d是整数"%value)
        lptr = rptr
    elif line[rptr] == '\'':#处理char类型的字面量
        if len(flag_stack) == 0:
            flag_stack.append('\'')
        else:
            flag_stack.pop()
        rptr = rptr + 1 
        while rptr < len(line) and line[rptr] != '\'':
            rptr = rptr + 1
        rptr = rptr + 1
        str_token = line[lptr: rptr]
        place = Place(line_no, lptr, rptr)
        token_list.append(Token(token_no, "LITERAL", place, str_token))
        token_no = token_no + 1
        lptr = rptr
        print("%s是字符串"%str_token)
    elif is_operator(line[rptr]):
        token = check_operator(line, line_no, token_no, lptr, rptr)
        token_list.append(token)
        token_no = token_no + 1
        rptr = token.get_place().get_rptr()
    elif line[lptr]==' ':#空格处理：直接跳过
        lptr = lptr + 1
        rptr = rptr + 1
    else:
        print("line %d col(%d,%d) Error：其他词法错误！"%(line_no, lptr, rptr))
        lptr = lptr + 1
        rptr = rptr + 1
    place = Place(line_no, lptr, rptr)
    return place
