# Method resolution order

class A:

    def show(self):
        print("Ini adalah show A")


class B:

    def show(self):
        print("Ini adalah show B")


class C(B, A):
    
    pass


obj = C()
obj.show()
# help(obj)