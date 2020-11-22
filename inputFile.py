class Member:

    # The mine characteristics of this class
    def __init__(self, name, mobileNumber, email):
        self.name = name
        self.mobileNumber = mobileNumber
        self.email = email

    # Function for display information a member
    def Display(self):
        print("Name is : ", self.name)
        print("mobile Number is : ", self.mobileNumber)
        print("Email is : ", self.email)
        print("-----------------------")

    # How much has the member read a book
    def ReedBooks(self, LBooks):

        self.LBooks = LBooks



class Books:

    # The mine characteristics of this class
    def __init__(self, title, pages, category):
        self.title = title
        self.pages = pages
        self.category = category





# Create new Members
M1 = Member("Fhad", "0563445626", "fhad1224@gmail.com")
M2 = Member("Rashed", "0553749983", "Rashed1998@gmail.com")
M3 = Member("Mazen", "0559923466", "mazen1112@gmail.com")
M4 = Member("Saleh", "0560034254", "salehkk@gmail.com")
M5 = Member("Rame", "0541113832", "rame333@gmail.com")
M6 = Member("Eyad", "0558893634", "eyad2004@gmail.com")
M7 = Member("Mohammed", "0560448773", "mohmmed55@gmail.com")
M8 = Member("AbdulAziz", "0543473226", "azeez99@gmail.com")
M9 = Member("Omar", "0563329843", "omaaar44@gmail.com")
M10 = Member("Ali", "0546654982", "ali34@gmail.com")

#add in list
members = [M1,M2,M3,M4,M5,M6,M7,M8,M9,M10]

# Create new books
Book1 = Books("Don Quixote", 863, "Novel")
Book2 = Books("The Diary of a Young Girl", 214, "Autobiography")
Book3 = Books("Silent Spring", 448, "scientific")
Book4 = Books("In Cold Blood", 343, "literature")
Book5 = Books("One Hundred Years of Solitude", 681, "Novel")
Book6 = Books("Look Homeward, Angel", 544, "Novel")
Book7 = Books("A Short History of Nearly Everything", 512, "scientific")
Book8 = Books("The Universe in a Nutshell", 224, "scientific")
Book9 = Books("Thinking, Fast and Slow", 499, "scientific")
Book10 = Books("The Selfish Gene", 238, "scientific")

# The books that members have read
M1.ReedBooks([Book3, Book6, Book10, Book2, Book8])
M2.ReedBooks([Book1, Book8, Book2, Book10, Book9])
M3.ReedBooks([Book4, Book7, Book5, Book6, Book10])
M4.ReedBooks([Book2, Book4, Book1, Book10, Book8])
M5.ReedBooks([Book10, Book5, Book9, Book7, Book4])
M6.ReedBooks([Book8, Book2, Book3, Book9, Book10, Book1])
M7.ReedBooks([Book7, Book6, Book2, Book9, Book4, Book5])
M8.ReedBooks([Book1, Book5, Book10, Book2, Book8, Book3, Book6])
M9.ReedBooks([Book4, Book8, Book7, Book10, Book1, Book2, Book5])
M10.ReedBooks([Book6, Book5, Book10, Book4, Book2, Book1, Book7, Book3])


