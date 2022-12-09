#class name


class hotel():

    def __init__(self,total_bill = None,suite = None,address = None,
    restaurant = None,act= None,name = None,checkindate = None,checkoutdate = None,
    guest_number =0 ,a = 1000):
        print("\n\n===============Welcome to Hotel==========================\n")
        self.total_bill = total_bill
        self.suite = suite
        self.address = address
        self.restaurant = restaurant
        self.act = act
        self.name = name
        self.checkindate = checkindate
        self.chekoutdate = checkoutdate
        self.guest_number = guest_number
        self.a = a

    
    


    def check_in(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        self.checkindate = int(input("\nEnter your check in date:"))
        self.chekoutdate = int(input("\nEnter your check out date"))
        self.guest_number +1
        print("\n Thank you for choosing us ""\n"
        " Your room number is:", self.guest_number,"\n")


    def show_rooms(self):
        print("We have the following rooms available")
        print("1 . Single bed ----------> 3000 INR per night")
        print("2 . Double bed ----------> 5000 INR per night")
        print("3 . luxury Suite----------> 8000 INR per night")
        print("4 . Presedential Suite ----------> 10000 INR per night")
        
        x = int(input("Enter your choice"))
        n = self.chekoutdate - self.checkindate

        if (x == 1):

            print("You have opted for Single Bed")
            self.suite = 3000 *n
        elif(x ==2):
            print("You have opted for Double Bed")
            self.suite = 5000 *n
        elif(x == 3):
            print("You have opted Luxury Suite")
            self.suite = 8000 *n
        elif(x ==4):
            print("You have opted Presedential Suite")
            self.suite = 10000 *n
        else:
            print("please choose your room")


    def restaurant_bill(self):
        print("==============Menu===================")

        print("1 . Water Bottle-------------> 20 INR")
        print("2 . Tea & Coffee-------------> 25 INR")
        print("3 . BreakFast Combo----------> 100 INR")
        print("4 . Lunch--------------------> 150 INR")
        print("5 . Dinner-------------------> 120 INR")
        print("6 . Snacks-------------------> 50 INR")
        print("7 . Not needed")

        while(True):

            c = int(input("Enter your choice:"))

            if c==1:
               d = int(input("Number of guests:"))
               self.restaurant =self.restaurant + 20*d

            if c ==2:
                d = int(input("Enter the number of guests"))
                self.restaurant = self.restaurant + 25*d
            
            if c == 3:
                d = int(input("Enter the number of guests"))
                self.restaurant = self.restaurant + 100*d
            
            if c == 4:
                d = int(input("Enter the number of guests"))
                self.restaurant = self.restaurant + 150*d

            if c == 5:
                d = int(input("Enter the number of guests"))
                self.restaurant = self.restaurant + 120*d

            if c == 6:
                d = int(input("Enter the number of guests"))
                self.restaurant = self.restaurant + 50*d
            


            elif c == 7:
                break
            else:
                print("Invalid requests")

        print("The Total restaurant bill generated is Rs",self.restaurant,"\n")



    def activity(self):

        print("===========Activity Menu=================")
        print("1 . Table Tennis-------------> 100 INR/Hour")
        print("2 . Swimming pool------------> 100 INR/Hour")
        print("3 . Snooker------------------> 70 INR/Hour")
        print("4 . Game Room----------------> 150 INR/Hour")
        print("5 . Gymnasium----------------> 120 INR/Hour")
        
        

        while(True):

            a = int(input("Enter your choice:"))

            if (a ==1):
                h = int(input("Number of hours"))
                self.act = self.act + 100*h

            elif(a == 2):
                h = int(input("Number of hours"))
                self.act = self.act + 100*h

            elif (a == 3):
                h = int(input("Number of hours"))
                self.act = self.act + 70*h

            elif (a == 4):
                h = int(input("Number of hours"))
                self.act = self.act + 150*h

            elif (a ==5):
                h = int(input("Number of hours"))
                self.act = self.act + 120*h
            
            elif (a ==6):
                break

            else:
                print("Invalid Option")

            print("Total Activity bill is Rs",self.activity,"\n")


    def display_details(self):
        
        print("************ Hotel Bill*************")
        print("Customer Details:")
        print("Customer Name",self.name)
        print("Customer Address",self.address)
        print("Check in Date",self.checkindate)
        print("Check out Date",self.chekoutdate)
        print("Guest Number",self.guest_number)
        print("Your Room rent",self.suite)
        print("Your Restaurant Bill is",self.restaurant)
        print("Your activity bill is",self.act)

        self.total_bill = self.suite + self.restaurant + self.act

        print("Your Sub total bill is ",self.total_bill)
        print("Additional Service charge is",self.a)
        print("The total Grand total bill is",self.total_bill + self.a)








def initialize():
    l = hotel()
    return l

def run(l):
    while(True):

        print("1.Please Check in here:")
        print("2.Check  and book your room ")
        print("3.Check out the Restaurant")
        print("4.Check out Activty Zone ")
        print("5.Show detailed bill ")
        print("6.Exit")

        ch = int(input("Enter your choice:"))
        if (ch ==1):
            l.check_in()

        if (ch ==2):
            l.show_rooms()

        if (ch ==3):
            l.restaurant_bill()

        if (ch == 4):
            l.activty()

        if (ch == 5):
            l.display_details()

        if (ch ==6):

            exit()


def main():

    l =initialize()
    run(l)

if __name__ == "__main__" :
       main()




















       
