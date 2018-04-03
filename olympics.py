#Gets the data from the Olympics.txt file and puts them into two lists,
#one for the year of the Olmypics and one for the place the games took place.
#Return : yearList, placeList
def getData():
    olympData = open("Olympics.txt", 'r')
    yearList = []
    placeList = []
    curLine = olympData.readline()
    #This loop strips the raw data into a year and place. The year has a space
    # between it and the place allowing for the two to be seperated.
    while curLine != "":
        curLine = curLine.strip()
        year, loc = curLine.split("\t")
        yearList.append(year)
        placeList.append(loc)
        curLine = olympData.readline()
    return yearList, placeList
#This method finds the place the Olympics took place in on a specific year.
#Return either an Error or String of location where Olympics were held.
def findLoc(yearList, locList, year):
    counter = 0 
    for i in range(len(yearList)):
        if year == int(yearList[i]):
            return locList[i], counter
        counter += 1
    a = "nowhere because they were not held that year"
    return a, coutner
#Main method. Asks user for a year and returns a string with the place.
# Also tells the user how many times the search loop was exceuted. 
def main():
    yearList, placeList = getData()
    year = int(input("Enter a year that the summer olympics were held: "))
    loc, count = findLoc(yearList, placeList, year)
    print("In the year,", year, "the olympics were in " , loc, ".") 
    print("That loop was executed", count, "times.")
