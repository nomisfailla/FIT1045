class BinaryTree():
    def __init__(self):
        self.v = None
        self.L = None
        self.R = None

    def insert(self, v):
        if self.v == None:
            self.v = v
        else:
            if v < self.v:
                if self.L == None:
                    self.L = BinaryTree()
                self.L.insert(v)
            if v > self.v:
                if self.R == None:
                    self.R = BinaryTree()
                self.R.insert(v)
            if v == self.v:
                print("SOMETHING IS VERY WRONG")
                quit()

    def print(self, i = 0):
        print(("|" * i) + "+" + str(self.v))
        if self.L != None: self.L.print(i + 1)
        if self.R != None: self.R.print(i + 1)

root = BinaryTree()
to_insert = [4, 2, 6, -1]
for i in to_insert:
    root.insert(i)


root.print()
