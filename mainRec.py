class Rectangle():

    def __init__(self, size):
        self.sizeRec = size

    def printSomething(self):
        print("Works")



if __name__ == "__main__":
    rec = Rectangle(6)
    rec.printSomething