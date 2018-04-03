#Gets the data from the Olympics.txt file and puts them into two lists,
#one for the year of the Olmypics and one for the place the games took place.
#Return : yearList, placeList
def getData():
    olympData = open("Olympics.txt", 'r')
    yearList = []
    placeList = []
    curLine = olympData.readline()
    while curLine != "":
        curLine = curLine.strip()
        year, loc = curLine.split("\t")
        yearList.append(year)
        placeList.append(loc)
        curLine = olympData.readline()
    return yearList, placeList
#This uses Binary Searching to locate the location of a specific Olympic Games.

def findLoc(yearList, locList, year):
   guess = 0
   length = len(yearList)
   counter = 0
   #This loop will keep running until counter equals the guess then it throws
   # an error string
   while True:
        if guess == length:
            return "nowhere because that was not a valid year", counter
        mid = (guess + length) // 2
        midYear = int(yearList[mid])
        if midYear == year:
            return locList[mid], counter
        if midYear < year:
            guess = mid + 1
        else:
            length = mid
        counter += 1
#Main method. Asks user for a year and returns a string with the place.
# Also tells the user how many times the search loop was exceuted.
def main():
    yearList, placeList = getData()
    year = int(input("Enter a year that the summer olympics were held: "))
    loc, count = findLoc(yearList, placeList, year)
    print("In the year,", year, "the olympics were in " , loc, ".")
    print("That loop was executed", count, "times.")
