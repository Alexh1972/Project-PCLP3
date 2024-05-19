import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


class Passanger:
    passangerId = 0
    pclass = 0
    name = ""
    sex = "male"
    age = 0
    sibSp = 0
    parch = 0
    ticket = 0
    fare = 0
    cabin = ""
    embarked = ""
    survived = 0
    ageGroup = 0

    def __init__(self, passangerId=-1, pclass=-1, name="", sex="", age=-1, sibSp=-1, parch=-1, ticket=-1, fare=-1, cabin="",
                 embarked="", survived=-1, ageGroup = -1):
        self.name = name
        self.passangerId = passangerId
        self.pclass = pclass
        self.sex = sex
        self.age = age
        self.sibSp = sibSp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked
        self.survived = survived
        self.ageGroup = ageGroup

    def convertCsvDataToPassanger(data, i):
        try:
            return Passanger(data.at[i, 'PassengerId'],
                                  data.at[i, 'Pclass'],
                                  data.at[i, 'Name'],
                                  data.at[i, 'Sex'],
                                  data.at[i, 'Age'],
                                  data.at[i, 'SibSp'],
                                  data.at[i, 'Parch'],
                                  data.at[i, 'Ticket'],
                                  data.at[i, 'Fare'],
                                  data.at[i, 'Cabin'],
                                  data.at[i, 'Embarked'],
                                  data.at[i, 'Survived'],
                                  data.at[i, 'Age Group'])
        except:
            return Passanger(data.at[i, 'PassengerId'],
                             data.at[i, 'Pclass'],
                             data.at[i, 'Name'],
                             data.at[i, 'Sex'],
                             data.at[i, 'Age'],
                             data.at[i, 'SibSp'],
                             data.at[i, 'Parch'],
                             data.at[i, 'Ticket'],
                             data.at[i, 'Fare'],
                             data.at[i, 'Cabin'],
                             data.at[i, 'Embarked'],
                             data.at[i, 'Survived'])

    def __str__(self):
        return str(self.passangerId) + " NAME: " + self.name + " CLASS: " + str(
            self.pclass) + " SEX: " + self.sex + " AGE: " + str(self.age) + " SIBSP: " + str(
            self.sibSp) + " PARCH: " + str(self.parch) + " TICKET: " + str(self.ticket) + " FARE: " + str(
            self.fare) + " CABIN: " + str(self.cabin) + " EMBARKED: " + str(self.embarked) + " SURVIVED: " + str(
            self.survived) + " AGE GROUP: " + str(self.ageGroup)

    def getCsvData(fileName):
        return pd.read_csv(fileName)
    def readPassangersCsvFile(fileName):
        with open(fileName) as file:
            passangers = []
            fieldName = []
            data = Passanger.getCsvData(fileName)
            for field in data.columns:
                fieldName.append(field)
            numberColumns = len(data.columns)
            dataTypes = data.dtypes
            for i in range(len(data)):
                passanger = Passanger.convertCsvDataToPassanger(data, i)
                passangers.append(passanger)
            print("---PRINT CSV FILE DETAILS---")
            print("Number of columns: " + str(numberColumns), end="\n\n")
            print("Column types : \n" + str(dataTypes), end="\n\n")
            print("Missing cells on columns: ")
            for i in range(len(fieldName)):
                print("Column " + fieldName[i] + " number of missing values - " + str(len(data[data[fieldName[i]].isna()])))
            if len(data[data.duplicated()]) == 0:
                print("No dublicated rows", end="\n\n")
            else:
                print("There are dublicated rows", end="\n\n")
            print("Number rows: " + str(len(data)))
            print("---END PRINT CSV FILE DETAILS---", end="\n\n")
        return passangers

    def printSurvivorPercentage(passangers):
        x = np.arange(0, 7, 1)
        y = []
        labels = ['Surviving', 'Deaths', 'Class 1', 'Class 2', 'Class 3', 'Male', 'Female']
        percentageSurviving = Passanger.getSurvivorPercentage(passangers)
        print("---PRINT SURVIVAL RATE---")
        print("No. Survivors - " + str(percentageSurviving))
        print("No. Deaths - " + str(1 - percentageSurviving), end="\n\n")
        y.append(percentageSurviving)
        y.append(1 - percentageSurviving)

        for i in range(1, 4):
            classPercentage = Passanger.getSurvivorPercentageByClass(passangers, i)
            y.append(classPercentage)
            print("Survivors for class - " + str(i) + ", percentage - " + str(classPercentage))
        print()

        percentageMale, percentageFemale = Passanger.getSurvivorPercentageBySex(passangers)
        y.append(percentageMale)
        y.append(percentageFemale)
        print("Male percentage - " + str(percentageMale))
        print("Female percentage - " + str(percentageFemale))
        print("---END PRINT SURVIVAL RATE---", end="\n\n")
        plt.bar(x, y)
        plt.xticks(x, labels)
        plt.title("Surviving rate")
        plt.show()

    def getSurvivorPercentage(passangers):
        totalpassangers = len(passangers)
        countSurviving = 0
        for i in range(totalpassangers):
            if passangers[i].survived:
                countSurviving += 1

        return countSurviving / totalpassangers

    def getSurvivorPercentageByClass(passangers, pclass):
        totalpassangers = len(passangers)
        countSurviving = 0
        classMembers = 0
        for i in range(totalpassangers):
            if passangers[i].pclass == pclass:
                if passangers[i].survived:
                    countSurviving += 1
                classMembers += 1

        return countSurviving / classMembers

    def getSurvivorPercentageBySex(passangers):
        totalpassangers = len(passangers)
        survivingMales = 0
        survivingFemales = 0
        males = 0
        females = 0
        for i in range(totalpassangers):
            if passangers[i].sex == "male":
                if passangers[i].survived:
                    survivingMales += 1
                males += 1
            else:
                if passangers[i].survived:
                    survivingFemales += 1
                females += 1

        return survivingMales / males, survivingFemales / females

    def printHistogram(passangers):
        auxiliar = Passanger()
        for field in auxiliar.__dict__.keys():
            if isinstance(auxiliar.__dict__.get(field), (int, float, complex)):
                x = [getattr(passanger, field) for passanger in passangers if passanger.__dict__.get(field) != auxiliar.__dict__.get(field)]
                if len(x) != 0:
                    plt.hist(x, bins='auto')
                    plt.title(field)
                    plt.show()

    def printMissingValues(passangers):
        missingValues = Passanger.findMissingValues(passangers)
        auxiliar = Passanger()
        print("---PRINT MISSING VALUES---")
        for i in range(len(missingValues)):
            print("Column \"" + str(missingValues[i][0]) + "\" missing values percentage - " + str(missingValues[i][1] / len(passangers)))
        survivedPassangers = [passanger for passanger in passangers if passanger.survived == 1]
        missingValuesSurvived = Passanger.findMissingValues(survivedPassangers)
        deadPassangers = [passanger for passanger in passangers if passanger.survived == 0]
        missingValuesDead = Passanger.findMissingValues(deadPassangers)
        print()
        print("Missing values survived")
        for i in range(len(missingValuesSurvived)):
            print("Column \"" + str(missingValuesSurvived[i][0]) + "\" missing values percentage - " + str(missingValuesSurvived[i][1] / len(survivedPassangers)))
        print()
        print("Missing values dead")
        for i in range(len(missingValuesDead)):
            print("Column \"" + str(missingValuesDead[i][0]) + "\" missing values percentage - " + str(missingValuesDead[i][1] / len(deadPassangers)))
        print("---END PRINT MISSING VALUES---", end="\n\n")
    def findMissingValues(passangers):
        auxiliar = Passanger()
        missingValues = []
        for field in auxiliar.__dict__.keys():
            x = [getattr(passanger, field) for passanger in passangers]
            valueToFind = auxiliar.__dict__.get(field)
            indices = [index for index, element in enumerate(x) if element == valueToFind or pd.isna(element)]
            missingValues.append([field, len(indices)])
        return missingValues

    def addAgeGroupColumn(data):
        ages = []
        x = np.arange(0, len(data), 1)
        for i in range(len(data)):
            age = data.at[i, 'Age']
            ages.append(Passanger.getAgeGroup(age))
        data['Age Group'] = ages
        plt.title("Age group")
        plt.hist(ages)
        plt.show()
        return data

    def getAgeGroup(age):
        ages = [20, 40, 60]
        i = 0
        while i < len(ages) and age > ages[i]:
            i += 1
        return i + 1

    def printSurvivingRateByAge(data):
        passangers = []
        for i in range(len(data)):
            passangers.append(Passanger.convertCsvDataToPassanger(data, i))
        x = []
        for i in range(1, 5):
            passangersByAge = [passanger for passanger in passangers if passanger.ageGroup == i and passanger.sex == "male"]
            survivors = [passanger for passanger in passangersByAge if passanger.survived == 1]
            rate = len(survivors) / len(passangersByAge)
            x.append(rate)

        plt.plot(np.arange(1, 5, 1), x)
        plt.title("Survive rate by age")
        plt.show()

    def printSurvivingRateKidsAdults(passangers):
        kids = [passanger for passanger in passangers if passanger.age < 18]
        adults = [passanger for passanger in passangers if passanger.age >= 18]
        kidsPercentage = Passanger.getSurvivorPercentage(kids)
        adultsPercentage = Passanger.getSurvivorPercentage(adults)
        print("---COMPARE CHILDREN TO ADULTS---")
        print("Children percentage : " + str(len(kids) / len(passangers)))
        print("---END COMPARE CHILDREN TO ADULTS---", end="\n\n")
        plt.bar([0, 1], [kidsPercentage, adultsPercentage])
        plt.xticks([0, 1], ['Children', 'Adults'])
        plt.show()

    def checkNameTitles(passangers):
        maleTitles = ['Mr.', 'Don.', 'Master.', 'Dr.', 'Capt.', 'Col.', 'Rev.', 'Major.', 'Sir.', 'Jonkheer.']
        femaleTitles = ['Mrs.', 'Ms.', 'Miss.', 'Dr.', 'Capt.']
        maleTitlesCount = np.zeros(len(maleTitles))
        femaleTitlesCount = np.zeros(len(femaleTitles))
        incorrectMatching = 0
        for passanger in passangers:
            tokens = passanger.name.split(" ")
            unisexTitle = 0
            hasMaleTitle = 0
            for title in maleTitles:
                if title in tokens:
                    if title in femaleTitles:
                        unisexTitle = 1
                    hasMaleTitle = 1
                    maleTitlesCount[maleTitles.index(title)] += 1

            for title in femaleTitles:
                if title in tokens:
                    femaleTitlesCount[femaleTitles.index(title)] += 1
            if ((hasMaleTitle and passanger.sex == 'female') or (hasMaleTitle == 0 and passanger.sex == 'male')) and unisexTitle == 0:
                incorrectMatching = 1
                print(passanger)
        print("---CHECK NAME TITLES---")
        print("Name titles are correct : " + str((1 - incorrectMatching == 1)))
        print("---END CHECK NAME TITLES---", end="\n\n")
        plt.bar(np.arange(0, len(maleTitles) + len(femaleTitles), 1), np.concatenate((maleTitlesCount, femaleTitlesCount)))
        plt.xticks(np.arange(0, len(maleTitles) + len(femaleTitles), 1), np.concatenate((maleTitles, femaleTitles)))
        plt.show()

    def replaceMissingValues(data):
        passangers = []
        for i in range(len(data)):
            passangers.append(Passanger.convertCsvDataToPassanger(data, i))
        data = data.replace(' ', np.nan)
        for i in range(0, len(data)):
            for field in data.columns:
                if pd.isna(data.at[i, field]):
                    if field == 'Age' or field == 'Parch' or field == 'Fare' or field == 'SibSp':
                        classField = field[0].lower() + field[1:len(field)];
                        x = [getattr(passanger, classField) for passanger in passangers if passanger.survived == data.at[i, 'Survived'] and not pd.isna(getattr(passanger, classField))]
                        newValue = sum(x) / len(x)
                        data.at[i, field] = newValue
                    elif field == 'Pclass' or field == 'Sex' or field == 'Embarked' or field == 'Name' or field == 'Cabin' or field == 'Ticket':
                        classField = field[0].lower() + field[1:len(field)];
                        x = [getattr(passanger, classField) for passanger in passangers if passanger.survived == data.at[i, 'Survived'] and not pd.isna(getattr(passanger, classField))]
                        unique, counts = np.unique(x, return_counts=True)
                        index = np.argmax(counts)
                        data.at[i, field] = unique[index]
        return data

    def analyseDeathsByFactors(data):
        sb.scatterplot(data=data, x="Pclass", y="Fare", hue="Survived", s = 20)
        plt.legend()
        plt.show()

