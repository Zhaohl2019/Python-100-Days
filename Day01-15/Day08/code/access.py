class Test:

    def __init__(self, foo):
        self.__foo = foo
        print('init')
    def __bar(self):
        print(self.__foo)
        print('__bar')
    def fun(self):
        print('fun')

def main():
    test = Test('hello')#init
    test.__init__('123')#init
    #test.__bar()#AttributeError: 'Test' object has no attribute '__bar'
    test._Test__bar()#__bar
    print(test._Test__foo)#123
    test.fun()#fun

if __name__ == "__main__":
    main()
