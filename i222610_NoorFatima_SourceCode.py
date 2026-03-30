#i222610 Noor Fatima SE-B
import random
import json
import matplotlib.pyplot as plt
import numpy as np

#Function randomly generates dates with Day from 1 - 31, Month from 1 to 12 and Year from 0000 - 9999 
def population_intialization():
    day = random.randint(1, 31)
    month = random.randint(1, 12)
    year = random.randint(0000, 9999)

    date = f"{day:02}/{month:02}/{year}"
    return date

#Function to extract the day, month and year from date.
def extracting_Day_Month_Year(date_str):
    day_str, month_str, year_str = date_str.split("/")
    day_str = int(day_str)
    month_str = int(month_str)
    year_str = int(year_str)

    return day_str, month_str, year_str

#Valid Categories
#Leap Year
def is_Leap_Year(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    return isLeapYear

#30-Day Month
def is_ThirtyDay_Month(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if month in [4, 6, 9, 11] and (day >= 1 and day <= 30):
        return True
    else:
        return False

#31-Day Month
def is_ThirtyOneDay_Month(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if month in [1, 3, 5, 7, 8, 10, 12] and (day >= 1 and day <= 31):
        return True
    else:
        return False

# Non-leap February > 29
def is_DayOfFeburary_Valid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    isleapYear = is_Leap_Year(date_str)
    if month == 2 and isleapYear:
        if day >= 1 and day <= 29:
            return True
        else:
            return False
    elif month == 2 and not isleapYear:
        if day >= 1 and day <= 28:
            return True
        else:
            return False
    else:
        return False

#Invalid Categories
# Day > 31
def is_Day_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if day < 1 or day > 31:
        return True
    else:
        return False

# Month > 12
def is_Month_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if month < 1 or month > 12:
        return True
    else:
        return False
    
#Year < 0000 or Year > 9999
def is_Year_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if year < 0000 or year > 9999:
        return True
    else:
        return False
    
#Invalid 30-Day Month
def is_ThirtyDay_Month_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return True
    else:
        return False
    
#Invalid 31-Day Month
def is_ThirtyOneDay_Month_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return True
    else:
        return False
    

# Invalid Feburary Day
def is_DayOfFeburary_Invalid(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    isleapYear = is_Leap_Year(date_str)
    if month == 2 and isleapYear:
        if day < 1 or day > 29:
            return True
        else:
            return False
    elif month == 2 and not isleapYear:
        if day < 1 or day > 28:
            return True
        else:
            return False
    else:
        return False

#Boundary Categories
#Min Year
def is_Min_Year(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if year == 0000:
        return True
    else:
        return False
    
#Max Year
def is_Max_Year(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if year == 9999:
        return True
    else:
        return False
    
#Day/Month Transition
def is_DayMonth_Transition(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    isLeapYear = is_Leap_Year(date_str)
    if is_ThirtyOneDay_Month(date_str) and day == 31:
        return True
    elif is_ThirtyDay_Month(date_str) and day == 30:
        return True
    elif month == 2 and isLeapYear and day == 29:
        return True
    elif month == 2 and not isLeapYear and day == 28:
        return True
    else:
        return False
    
#Valid Edge Leap Year (e.g., 29/02/2020)
def is_ValidEdge_LeapYear(date_str):
    day, month, year = extracting_Day_Month_Year(date_str)
    if day == 29 and month == 2 and is_Leap_Year(date_str):
        return True
    else:
        return False

#Function to identify the categories that the randomly generated date falls into.
def date_categories(date):

    #Categories for the date.
    dateCategories = []

    #Valid
    is_LeapYear = is_Leap_Year(date)
    is_ThirtyDayMonth = is_ThirtyDay_Month(date)
    is_ThirtyDayOneMonth = is_ThirtyOneDay_Month(date)
    is_DayOfFeburaryValid = is_DayOfFeburary_Valid(date)

    #Invalid
    is_DayInvalid = is_Day_Invalid(date)
    is_MonthInvalid = is_Month_Invalid(date)
    is_YearInvalid = is_Year_Invalid(date)
    is_ThirtyDayMonthInvalid = is_ThirtyDay_Month_Invalid(date)
    is_ThirtyOneDayMonthInvalid = is_ThirtyOneDay_Month_Invalid(date)
    is_DayOfFeburaryInvalid = is_DayOfFeburary_Invalid(date)
    
    #Boundary
    is_MinYear = is_Min_Year(date)
    is_MaxYear = is_Max_Year(date)
    is_DayMonthTransition = is_DayMonth_Transition(date)
    is_ValidEdgeLeapYear = is_ValidEdge_LeapYear(date)

    if is_LeapYear:
        dateCategories.append("Valid Leap Year")
    
    if is_ThirtyDayMonth:
        dateCategories.append("Valid Thirty Day Month")
    
    if is_ThirtyDayOneMonth:
        dateCategories.append("Valid Thirty One Day Month")

    if is_DayOfFeburaryValid:
        dateCategories.append("Valid Day of Feb")

    if is_DayInvalid:
        dateCategories.append("Invalid Day")

    if is_MonthInvalid:
        dateCategories.append("Invalid Month")

    if is_YearInvalid:
        dateCategories.append("Invalid Year")

    if is_ThirtyDayMonthInvalid:
        dateCategories.append("Invalid Thirty Day Month")

    if is_ThirtyOneDayMonthInvalid:
        dateCategories.append("Invalid Thirty One Day Month")

    if is_DayOfFeburaryInvalid:
        dateCategories.append("Invalid Day of Februrary")
    
    if is_MinYear:
        dateCategories.append("Min Year")

    if is_MaxYear:
        dateCategories.append("Max Year")

    if is_DayMonthTransition:
        dateCategories.append("Day Month Transition")

    if is_ValidEdgeLeapYear:
        dateCategories.append("Edge Leap Year")
    
    return dateCategories

#Function to calculate the fitness of each date in the population.
def calculate_fitness(population):
    #Valid
    count_LeapYear = 0
    count_ThirtyDayMonth = 0
    count_ThirtyDayOneMonth = 0
    count_DayOfFeburaryValid = 0

    #Invalid
    count_DayInvalid = 0
    count_MonthInvalid = 0
    count_YearInvalid = 0
    count_ThirtyDayMonthInvalid = 0
    count_ThirtyOneDayMonthInvalid = 0
    count_DayOfFeburaryInvalid = 0
    
    #Boundary
    count_MinYear = 0
    count_MaxYear = 0
    count_DayMonthTransition = 0
    count_ValidEdgeLeapYear = 0

    populationWithFitnessScore = dict()
    unique = 0
    redundant = 0
    index = 0

    for date in population:
        if is_Leap_Year(date):
            count_LeapYear += 1
            if count_LeapYear == 1:
                unique += 1
            if count_LeapYear > 1:
                redundant += 1
        
        if is_ThirtyDay_Month(date):
            count_ThirtyDayMonth += 1
            if count_ThirtyDayMonth == 1:
                unique += 1
            if count_ThirtyDayMonth > 1:
                redundant += 1
        
        if is_ThirtyOneDay_Month(date):
            count_ThirtyDayOneMonth += 1
            if count_ThirtyDayOneMonth == 1:
                unique += 1
            if count_ThirtyDayOneMonth > 1:
                redundant += 1
        
        if is_DayOfFeburary_Valid(date):
            count_DayOfFeburaryValid +=1
            if count_DayOfFeburaryValid == 1:
                unique += 1
            if count_DayOfFeburaryValid > 1:
                redundant += 1

        if is_Day_Invalid(date):
            count_DayInvalid += 1
            if count_DayInvalid == 1:
                unique += 1
            if count_DayInvalid > 1:
                redundant += 1
        
        if is_Month_Invalid(date):
            count_MonthInvalid += 1
            if count_MonthInvalid == 1:
                unique += 1
            if count_MonthInvalid > 1:
                redundant += 1
        
        if is_Year_Invalid(date):
            count_YearInvalid += 1
            if count_YearInvalid == 1:
                unique += 1
            if count_YearInvalid > 1:
                redundant += 1

        if is_ThirtyDay_Month_Invalid(date):
            count_ThirtyDayMonthInvalid += 1
            if count_ThirtyDayMonthInvalid == 1:
                unique += 1
            if count_ThirtyDayMonthInvalid > 1:
                redundant += 1
        
        if is_ThirtyOneDay_Month_Invalid(date):
            count_ThirtyOneDayMonthInvalid += 1
            if count_ThirtyOneDayMonthInvalid == 1:
                unique += 1
            if count_ThirtyOneDayMonthInvalid > 1:
                redundant += 1

        if is_DayOfFeburary_Invalid(date):
            count_DayOfFeburaryInvalid += 1
            if count_DayOfFeburaryInvalid == 1:
                unique += 1
            if count_DayOfFeburaryInvalid > 1:
                redundant += 1

        if is_Min_Year(date):
            count_MinYear += 1
            if count_MinYear == 1:
                unique += 1
            if count_MinYear > 1:
                redundant += 1
        
        if is_Max_Year(date):
            count_MaxYear += 1
            if count_MaxYear == 1:
                unique += 1
            if count_MaxYear > 1:
                redundant += 1
        
        if is_DayMonth_Transition(date):
            count_DayMonthTransition += 1
            if count_DayMonthTransition == 1:
                unique += 1
            if count_DayMonthTransition > 1:
                redundant += 1
        
        if is_ValidEdge_LeapYear(date):
            count_ValidEdgeLeapYear += 1
            if count_ValidEdgeLeapYear == 1:
                unique += 1
            if count_ValidEdgeLeapYear > 1:
                redundant += 1
   
        fitnessScore = (unique) / (redundant + 1)
        dateCategories = date_categories(date)
        index += 1
        populationWithFitnessScore[index] = [date, fitnessScore, dateCategories]

    return populationWithFitnessScore, unique

#Rank Based Selection is used to select the survivors.
def rank_based_selection(population):
    
    #Sorting the population in descending sort according to the fitness score.
    populationSize = len(population)
    percentageOfSelectingPopulation = 0.7
    selectedPopulation = int(percentageOfSelectingPopulation * len(population))
    datesToBeDuplicated = populationSize - selectedPopulation 

    survivors = dict(sorted(population.items(), key=lambda item: item[1][1], reverse=True))

    #Selecting only first 70% of the dates and duplicated the remaining 30% with the first 30%.
    #Duplicating the first 30% so that the population size stays the same.
    keysOfValuesToBeRemoved = list(survivors.keys())[-datesToBeDuplicated:]
    keysOfSurvivors =  list(survivors.keys())

    j = 0
    for i in keysOfValuesToBeRemoved:
        survivors[i] = survivors[keysOfSurvivors[j]]
        j += 1

    return survivors

#Swap month and year of the incoming dates for crossover.
def swapping(date1, date2):
 
    day1, month1, year1 = extracting_Day_Month_Year(date1)
    day2, month2, year2 = extracting_Day_Month_Year(date2)

    #Swap month and year
    date1 =  f"{day1:02}/{month2:02}/{year2}"
    date2 =  f"{day2:02}/{month1:02}/{year1}"
    
    return date1, date2


#Cross Over
def Cross_Over(population):

    keysOfPopulation =  list(population.keys())
    crossOver = []

    if len(population.keys()) % 2 == 0:
        j = 1
        
        for i in range(0, len(population.keys()), 2):
            date1, date2 = swapping(population[keysOfPopulation[i]][0], population[keysOfPopulation[j]][0])
            crossOver.append(date1)
            crossOver.append(date2)
            j+=2 
    else:
        firstDate = population[keysOfPopulation[0]][0]
        lastDate = population[keysOfPopulation[len(population.keys()) - 1]][0]
        
        j = 1
        
        for i in range(0, len(population.keys()) - 1, 2):
            date1, date2 = swapping(population[keysOfPopulation[i]][0], population[keysOfPopulation[j]][0])
            crossOver.append(date1)
            crossOver.append(date2)
            j+=2 
        

        date1, date2 = swapping(firstDate, lastDate)
        crossOver.append(date2)
    
    return crossOver

#Mutation
def Mutation(population):
    NoOfMutations = int(0.15 * len(population))

    for i in range(NoOfMutations):
        index = random.randint(0, len(population) - 1)
        method = random.randint(1, 6)

        #Change Day + 3
        if method == 1:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day + 3:02}/{month:02}/{year}"
        
        #Change Day - 3
        if method == 2:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day - 3:02}/{month:02}/{year}"

        #Change Month + 1
        if method == 3:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day:02}/{month + 1:02}/{year}"

        #Change Month - 1
        if method == 4:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day:02}/{month - 1:02}/{year}"
        
        #Change Year  + 100
        if method == 5:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day:02}/{month:02}/{year + 100}"

        #Change Year - 100
        if method == 6:
            day, month, year = extracting_Day_Month_Year(population[index])
            population[index] = f"{day:02}/{month - 1:02}/{year - 100}"
        
    
    return population


#Function for printing the best test cases and writing it into the json file.
def printBestEvolvedTestCases(population, noOfGenerations, coverageAchieved):
    print("\n---------------------------------------Best Test Cases--------------------------------------")
    print("\n")
    
    sortedPopulation = dict(sorted(population.items(), key=lambda item: item[1][1], reverse=True))    
    
    print("ID                 DATE                     FITNESS                   CATEGORIES")
    for key, value in sortedPopulation.items():
        date, fitness, categories = value
        print(f"\n{key:02}               {date}                  {fitness:.02}                {categories}")
 
    print(f"\nNumber of Generation       : {noOfGenerations}")
    print(f"\nNumber of Coverage Achieved: {coverageAchieved:.03}")


#Function for writing the best test cases it into the json file.
def writeBestEvolvedTestCases(population):  
    sortedPopulation = dict(sorted(population.items(), key=lambda item: item[1][1], reverse=True))    
    with open("bestTestCases.json", "w") as file:
        json.dump(sortedPopulation, file, indent=4)


#Function to plot line graph of generations against the respective coverages.
def lineGraph(coverages):
    generations = []

    for i in range(100):
        generations.append(i+1)

    x = np.array(generations)
    y = np.array(coverages)

    plt.plot(x,y)
    plt.xlabel("Generation")
    plt.ylabel("Coverage")
    plt.title("Genetic Algorithm Improvement Over Generations")
    plt.show()
    
#Genetic Algorithm
def Genetic_algorithm():
    
    populationSize = 25
    totalCategories = 14
    noOfGenerations = 1
    coverageAchieved = 0
    dates = []
    coverages = []
    unique = 0

    for i in range(populationSize):
        dates.append(population_intialization())

    while 1:
        if(noOfGenerations == 1):
            populationWithFitnessScores, unique = calculate_fitness(dates)
        else:
            populationWithFitnessScores, unique = calculate_fitness(mutation)
        
        coverageAchieved = (unique / totalCategories) * 100
        coverages.append(coverageAchieved)

        if coverageAchieved >= 95 or noOfGenerations == 100:
            printBestEvolvedTestCases(populationWithFitnessScores, noOfGenerations, coverageAchieved)
            writeBestEvolvedTestCases(populationWithFitnessScores)
            lineGraph(coverages)
            break

        randomSelection = rank_based_selection(populationWithFitnessScores)
        crossOver = Cross_Over(randomSelection)
        mutation = Mutation(crossOver)
        noOfGenerations += 1
    

def main():
    Genetic_algorithm()


if __name__ == "__main__":
    main()