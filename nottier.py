class Nottier():
    def __init__(self):
        self.status 
        pass

    # def __new__(self):
    #     raise "1"

    def callback(self, args):
        pass

class A(Nottier):
    def __init_(self,name):
        super(A,self).__init_(name)
        self.status = 0
        print("123")
        pass
    
    def __new__(self,name):
        print("实例A开始创建")
        return self

    def callback(self,*args):
        # super().callback(args)
        print("hello,world!")

if __name__ == "__main__" :
    B = A("bb")

    B.callback("a")


