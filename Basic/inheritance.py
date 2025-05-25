# class employee:
#     name="ram"
#     age=12

# class hello:
#     game="pubg"

# class hi(employee,hello):
#     def show(self):
#         print(f"name is {self.name} game is {self.game}")

# b=hi()
# b.show()

class coder:
    def __init__(self):
        print("hello")
    a=1

class program:
    b=2
    @classmethod
    def show(self):
        print(f"b={self.b}")
    

# class reader(program):  
#     def __init__(self):
#         super().__init__()
#         print("world")
#     c=3

# r=reader()
# print(r.a,r.b,r.c)
c=program()
c.b=3
c.show()