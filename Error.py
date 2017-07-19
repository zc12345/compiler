from Token import Place

error_dict = {
    0:"标识符只能是字母开头的字母和数字组合！",#词法错误
    1:"该符号不能识别",
    2:"标识符长度超过限制",
    3:"\'不匹配",
    9:"其他词法错误",
    10:"(括号不匹配",#语法错误
    11:")括号不匹配",
    12:"[括号不匹配",
    13:"]括号不匹配",
    14:"{括号不匹配",
    15:"}括号不匹配",
    16:"缺少;",
    17:"if语句缺少then",
    18:"do-while语句缺少do",
    19:"do-while语句缺少while",
    20:"call之后不是过程名",
    29:"其他语法错误",
    30:"类型不一致",#语义错误
    31:"作用域错误",
    32:"说明错误",
    33:"变量未定义",
    39:"其他语义错误"
}
class ErrorType(object):
    def __init__(self, error_type, place):
        self.__error_type = error_type
        self.__content = error_dict.get(error_type,"NONE")
        self.__place = place

    def print_error(self):
        print("error:\t位置:%s 错误类型:%s 错误内容:%s"%(self.__place.get_place(), self.__error_type, self.__content))