class ErrorType(object):
    def __init__(self, error_type, content, place):
        self.__error_type = error_type
        self.__content = content
        self.__place = place

    def print_error(self):
        print("error:\t位置：%s 错误类型：%s 错误内容：%s"%(self.__place, self.__error_type, self.__content))