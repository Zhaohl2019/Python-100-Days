"""
多重继承
- 菱形继承(钻石继承)
- C3算法(替代DFS的算法)
- 广度优先
"""
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")
class E(D):
    def __init__(self):
        print('进入E')
        super().__init__()
        print("离开E")
e=E()
'''进入E
进入D…
进入B…
进入C…
进入A…
离开A…
离开C…
离开B…
离开D…
离开E
'''
#print(E.mro())#[<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
