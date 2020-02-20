# in coding, as long as it fits the criteria, we don't care who it is
# as long as it behaves as a duck, it is a duck
# say we have a class, which we have a function in it with variable ide
class Laptop:

    def code(self, ide):
        ide.execute()            # IDE class must have function execute, ide is an object of IDE class here


# say we want to have a class for this ide
class IDE:

    def execute(self):
        print("Compiling")
        print("Running")


#ide1 = IDE()
#lap1 = Laptop()
#lap1.code(ide1)    # need to pass an IDE class object

# OR, say we have another class
class MyEditor:

    def execute(self):
        print("Convention check")
        print("Grammar check")


ide1 = MyEditor()
lap1 = Laptop()
lap1.code(ide1)
# here ide1 is an object of MyEditor class
# it still can use code method since MyEditor class has execute method as well
# we don't care if ide variable in Laptop is from what class, as long as it has execute function, it can be used
