class Token(object):
    '''
    token 类
    需要添加：参数检查
    '''
    def __init__(self, no, type, place, value):
        self.__no = no #token编号
        self.__type = type #token类型
        self.__place = place #token地址，多少行多少列
        self.__value = value #token值

    def print_token(self):
        print("%s\t%s\t%s\t%s"%(self.__no, self.__type, self.__place.get_place(), self.__value))

    def get_no(self):
        return self.__no
    def get_type(self):
        return self.__type
    def get_place(self):
        return self.__place
    def get_value(self):
        return self.__value

class Place(object):
    def __init__(self, line, lptr, rptr):
        self.__line = line
        self.__lptr = lptr
        self.__rptr = rptr
    def get_place(self):
        return [self.__line, self.__lptr, self.__rptr]

    def print_place(self):
        print("line:%d col:(%d :%d)"%(self.__line, self.__lptr, self.__rptr))

    def get_lptr(self):
        return self.__lptr

    def get_rptr(self):
        return self.__rptr

class Production(object):
    '''
    语法分析的文法中每个产生式
    '''
    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_left(self, left):
        self.__left = left
    
    def set_right(self, right):
        self.__right = right

    def print_production(self):
        print("%s -> %s"%(self.__left,self.__right))

class Quad_code(object):
    '''
    语义分析产生的四元式
    '''
    def __init__(self, quad_no, op, arg1, arg2, result):
        self.__quad_no = quad_no
        self.__op = op
        self.__arg1 = arg1
        self.__arg2 = arg2
        self.__result = result
        
    def get_quad_no(self):
        return self.__quad_no
    def get_op(self):
        return self.__op
    def get_arg1(self):
        return self.__arg1
    def get_arg2(self):
        return self.__arg2
    def print_quad_code(self):
        print("quad_no.%s\t%s\t%s\t%s\t%s"%(self.__quad_no, self.__op, self.__arg1, self.__arg2, self.__result))