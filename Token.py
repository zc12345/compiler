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
        print("%s\t%s\t%s\t%s"%(self.__no, self.__type, self.__place, self.__value))

    def get_no(self):
        return self.__no
    def get_type(self):
        return self.__type
    def get_place(self):
        return self.__place
    def get_value(self):
        return self.__value

class Place(object):
    def __init__(self, line, col_left, col_right):
        self.__line = line
        self.__col_left = col_left
        self.__col_right = col_right

    def print_place(self):
        print("line:%d col_left_ptr:%d col_right_ptr:%d"%(self.__line, self.__col_left, self.__col_right))