do:
movie=int(input("Enter the movie type.\nAvailable movies are\n 1.ACTION\n 2.DRAMA\n 3.COMEDY\n"))
ticket=int(input("Enter the type of ticket:\n 1.NORMAL-$250\n 2.PREMIUM-$600\n"))
count=int(input("Enter the number of tickets\n"))
time=int(input("Select show time\n 1.10:00AM\n 2.2:00PM\n 3.6:00PM\n 4.10:00PM\n"))

match movie:
    case 1:
        print("MOVIE:ACTION")
    case 2:
        print("MOVIE:DRAMA")
    case 3:
        print("MOVIE:COMEDY")
    case _:
        print('Invalid!!')
print("Number of tickets:",count)
match ticket:
    case 1:
        print("Ticket type:NORMAL")
        if count>5:
            #print('You are eligible for discount')
            #print("Total cost: ",count*250)
            print("Total cost: ",count*250*0.1)
        else:
             print("Total cost: ",count*250)
    case 2:
        print("Ticket type:PREMIUM")
        if count>5:
            print("Total cost: ",count*600*0.1)
        else:
              print("Total cost: ",count*600)
       
match time:
    case 1:
        print("Show time:10:00AM")
    case 2:
        print("Show time:2:00PM")
    case 3:
        print("Show time:06:00PM")
    case 4:
        print("Show time:10:00PM")
import datetime
print("Date:",datetime.datetime.now().strftime("%d-%m-%Y "))
print("Do you want to make another booking:yes/no")
while choice=='yes'
