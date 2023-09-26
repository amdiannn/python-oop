class A:

    def methodA(self):
        print("Ini adalah method A")


class B:

    def methodB(self):
        print("Ini adalah method B")


class C(A, B):

    pass


objectD = C()

objectD.methodA()
objectD.methodB()