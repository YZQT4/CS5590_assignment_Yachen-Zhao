class Person():
    def __init__(self, name, gender): # _init_ constructor
        self.name = name # use self
        self.gender = gender
        self.show()
    def show(self):
        print("name: " + self.name)
        print("gender: " + self.gender)

class Student(Person): # inheritance 1
    def __init__(self, name, gender, studentid): # _init_ constructor
        Person.__init__(self, name, gender)
        self.studentid=studentid
        self.shows()
    def shows(self):
        print("studentid: %d"%self.studentid+"\nThis is a childclass of Person")

class Librarian(Person): # inheritance 2(Multiple inheritance)
    __salarybyhour=0 # Private data member
    def __init__(self, name, gender, staffid, salary): # _init_ constructor
        super().__init__(name, gender) #super call
        self.staffid=staffid
        Librarian.__salarybyhour=salary
        self.show2()
        print("Salary per hour is: %d"%Librarian.__salarybyhour+"\nThis is a childclass of Person")
    def show2(self):
        print("staffid: %d"%self.staffid)

class Book():
    def __init__(self, bookid, title, author): # _init_ constructor
        self.bookid=bookid
        self.title=title
        self.author=author
        self.show3()
    def show3(self):
        print("bookid: %d"%self.bookid)
        print("title: " + self.title)
        print("author: " + self.author)

class Textbook(Book):
    def __init__(self,bookid, title, author, price): # _init_ constructor
        Book.__init__(self,bookid, title, author)
        self.price=price
        print("price:$%d"%self.price+"\nThis is a childclass of Book")

#five instance for five classes
Dan=Person("Dan","Male")
print("\n")
Alice=Student("Alice","female",1)
print("\n")
Nick=Librarian("Nick","male",2,17)
print("\n")
Book1=Book(11,"How to achive your goal","Lily",)
print("\n")
Textbook1=Textbook(29,"Deep learning of Python","Dr.H",99)