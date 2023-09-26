# Diamond Problem

class A:

    def show(self):
        print("Ini adalah show A")


class B(A):

    def show(self):
        print("Ini adalah show B")


class C(A):

    def show(self):
        print("Ini adalah show C")


class D(B, C):

    pass


obj = D()
obj.show()
# help(obj)