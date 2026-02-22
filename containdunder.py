class Library:
    def __init__(self,books):
        self.books = books
    def __contains__(self,item):
        return item in self.books
lib = Library(["DSA", "Python", "Java", "SQL"])
print("Python" in lib)
print("HTML" in lib)