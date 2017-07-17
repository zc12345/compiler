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
        print("line:%d left_ptr:%d right_ptr:%d"%(self.__line, self.__lptr, self.__rptr))

    def get_lptr(self):
        return self.__lptr

    def get_rptr(self):
        return self.__rptr
