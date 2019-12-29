#Sabrina Turney
#September 7, 2018
#Name of program: Stadium Seating
#Description of program: This program determines based on input how much income is
#generated from three differently priced seat sections for a softball game. 
#It's modular, multiple modules called by main.


#Defining the main module
#Call the other modules from within this module, it runs the program
def main():
    # Define variables
    classA = 0         # whole numbers, since you can't have half a seat
    classB = 0     
    classC = 0  
    ticketSales = 0    #because the costs don't include tax and are whole numbers
                       #I keep using an integer here.
    
    #Have a descriptive user introduction. Remember the \n gives me a blank line
    #after when it is at the end
    print("Welcome to my ticket cost calculator")
    print("if you tell me how many tickets were sold in each section,")
    print("I can tell you how much profit was made!\n") 
    print("\nFirst let's find out how many tickets in each Seating Class you sold!\n") 

    #Get user input
    classA = int(input("How many tickets did you sell in Class A seating? "))
    classB = int(input("How many tickets did you sell in Class B seating? "))
    classC = int(input("How many tickets did you sell in Class C seating? ")) 

    #Call the other modules passing values to them
    ticketSales = calcCost(classA, classB, classC, ticketSales)
    printTotal = printCosts(ticketSales, classA, classB, classC)

#This module will determine the number of gallons required to paint the area
def calcCost(classA, classB, classC, ticketSales):

    #Define variables
    ticketSales = 0
    #Integer - No half seats, whole dollar amounts for tickets

    #This is the math. We have to multiply the input value by the costs per ticket 
    ticketSales = (classA * 15) + (classB * 12) + (classC * 9)

    #This will return a value that can be used in other modules
    return ticketSales


#This module will print the costs for the user to see
def printCosts(ticketSales, classA, classB, classC):
    
    #Display output to the user
    #The f'{variable} will format the variable easy since it's a whole number
    print(f'The total income from ticket sales is ${ticketSales}!')
    print("The breakdown is as follows:")
    print(f'Class A sold {classA} seats, at $15 per seat.')
    print(f'Class B sold {classB} seats, at $12 per seat.')
    print(f'Class C sold {classC} seats, at $9 per seat.')
    print("\nGreat job selling seats!")

#call the main function now to run the whole thing
main()

