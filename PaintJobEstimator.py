# Sabrina Turney
# Sept 6, 2018
# Name of program: Paint Job Estimator
# Description of program:  this program will determine the number of gallons of
# paint used, hours of labor required, cost of paint, labor cost, and total cost
# based on a user entered amount of wall square footage
# It must be modular - which means having multiple modules and calling them from
# main.


# Define global constant
# A global constant has a scope of the entire program, which means every module 
# in the program can see them
# 1 gallon of paint covers 115 square feet
SQFT_PER_GALLON = 115

# Defining the main function
def main():
  
    # Define variables
    userArea = 0.0     # float
    paintPrice = 0.0     # float
    totalGallons = 0.0     # float
    totalHours = 0.0    #float
    paintCost = 0.0     #float
    laborCharge = 0.0   #float
    

    #Have a descriptive user introduction. Remember the \n gives me a blank line
    #after when it is at the end
    print("Welcome to my paint job calculator")
    print("if you tell me how many square feet you have!")
    print("I can tell you how many gallons of paint you will need, how many hours labor, and how much it will cost\n") 
    print("\nFirst let's find out how big your area is\n") 

    #Get user input
    userArea = float(input("How many square feet do you need to paint? "))
    paintPrice = float(input("How much is the paint per gallon? "))

    #Call the other modules passing values to them
    totalGallons = gallonsUsed(userArea)
    totalHours = laborHours(userArea)
    paintCost = totalPaintCost(totalGallons, paintPrice)
    laborCharge = totalLaborCharge(totalHours)
    printCosts(userArea, paintPrice, gallonsUsed, totalHours, paintCost, laborCharge)



#This module will determine the number of gallons required to paint the area
def gallonsUsed(userArea):
    #Call global constant
    global SQFT_PER_GALLON

    #Define variables
    totalGallons = 0.0     # float

    #This is the math. We have to multiply the input value by the global constant 
    totalGallons = userArea / SQFT_PER_GALLON

    #This will return a value that can be used in other modules
    return totalGallons



#This module will determine the number of hours of labor required to paint the area
#8 hours of labor is required for 115 square feet
def laborHours(userArea):
    #Define local constant / you can use local or global depending on need
    HOURS_PER_SQFT = 8
    
    #Define variables
    totalHours = 0.0   # float

    #This is the math. We have to divide the userArea by 8 
    totalHours =  userArea / SQFT_PER_GALLON * HOURS_PER_SQFT

    #This will return a value that can be used in other modules
    return totalHours



#This module will determine the cost of the paint using two parameter values passed
#in from main
def totalPaintCost(totalGallons, paintPrice):

    #This is the math. We have to multiply the totalGallons by the paintPrice
    paintCost = totalGallons * paintPrice

    #This will return a value that can be used in other modules
    return paintCost



#This module will determine the cost of the labor using 1 parameter value passed in
#from main
def totalLaborCharge(totalHours):
    #Define local constant / you can use local or global depending on need
    HOURLY_LABOR_RATE = 20.0

    #This is the math. We have to multiply the laborHours by HOURLY_LABOR_RATE    
    laborCharge = totalHours * HOURLY_LABOR_RATE

    #This will return a value that can be used in other modules
    return laborCharge



#This module will print the costs for the user to see
def printCosts(userArea, paintPrice, gallonsUsed, totalHours, paintCost, laborCharge):
    #Define variables
    totalCost = 0.0   # float

    #Do the math to find the total cost for the user
    #It will be the paint cost plus the labor charge
    totalCost = paintCost + laborCharge
    
    #Display nice friendly output to the user
    #The \t is a tab
    #The %0.02f will format the variable to 2 decimal places
    print("The total cost to paint",userArea,"square feet if your paint costs $%0.02f" % paintPrice,"per gallon is $%0.02f" % totalCost)
    print("The breakdown is as follows")
    print("Paint Cost:\t$%0.02f" % paintCost)
    print("Labor Hours:\t", round(totalHours)) #This will round the total hours up to the next whole hour
    print("Labor Cost:\t$%0.02f" % laborCharge)
    print("\nGood luck with your project!")
    


    
#call the main function now to run the whole thing
main()
