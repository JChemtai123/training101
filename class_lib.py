class Library:
    genre = []
    books = 0
    members = []
#constructor
    def __init__(self,gen,bks,mems):
        self.genre= gen
        self.books= bks
        self.members = mems
    def lend(self):
         self.books -= 1