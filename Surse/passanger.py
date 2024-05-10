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

    def __init__(self, passangerId=0, pclass=0, name="", sex="", age=0, sibSp=0, parch=0, ticket=0, fare=0, cabin="",
                 embarked="", survived=0, ageGroup = 0):
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
            fieldName = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin',
                         'Embarked', 'Survived']
            data = Passanger.getCsvData(fileName)
            numberColumns = len(data.columns)
            dataTypes = data.dtypes
            for i in range(len(data)):
                passanger = Passanger.convertCsvDataToPassanger(data, i)
                passangers.append(passanger)
            print("Number of columns: " + str(numberColumns))
            print("Column types : \n" + str(dataTypes))
            print("Missing cells on columns: ")
            for i in range(len(fieldName)):
                print(fieldName[i] + " " + str(len(data[data[fieldName[i]].isna()])))
            if len(data[data.duplicated()]) == 0:
                print("No dublicated rows")
            else:
                print("There are dublicated rows")
            print("Number rows: " + str(len(data)))
        return passangers

    def printSurvivorPercentage(passangers):
        x = np.arange(0, 7, 1)
        y = []
        labels = ['Surviving', 'Deaths', 'Class 1', 'Class 2', 'Class 3', 'Male', 'Female']
        percentageSurviving = Passanger.getSurvivorPercentage(passangers)
        print("Survivors: " + str(percentageSurviving))
        print("Deaths: " + str(1 - percentageSurviving))
        y.append(percentageSurviving)
        y.append(1 - percentageSurviving)

        for i in range(1, 4):
            classPercentage = Passanger.getSurvivorPercentageByClass(passangers, i)
            y.append(classPercentage)
            print("Class : " + str(i) + " percentage : " + str(classPercentage))

        percentageMale, percentageFemale = Passanger.getSurvivorPercentageBySex(passangers)
        y.append(percentageMale)
        y.append(percentageFemale)
        print("Male percentage: " + str(percentageMale))
        print("Female percentage: " + str(percentageFemale))
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
            if type(auxiliar.__dict__.get(field)) == int:
                x = [getattr(passanger, field) for passanger in passangers]
                plt.hist(x, bins='auto')
                plt.title(field)
                plt.show()

    def printMissingValues(passangers):
        missingValues = Passanger.findMissingValues(passangers)
        auxiliar = Passanger()
        print("Missing values")
        for i in range(len(missingValues)):
            print(str(missingValues[i]) + " " + str(missingValues[i] / len(passangers)))
        survivedPassangers = [passanger for passanger in passangers if passanger.survived == 1]
        missingValuesSurvived = Passanger.findMissingValues(survivedPassangers)
        deadPassangers = [passanger for passanger in passangers if passanger.survived == 0]
        missingValuesDead = Passanger.findMissingValues(deadPassangers)
        print("Missing values survived")
        for i in range(len(missingValuesSurvived)):
            print(str(missingValuesSurvived[i]) + " " + str(missingValuesSurvived[i] / len(missingValuesSurvived)))
        print("Missing values survived")
        for i in range(len(missingValuesDead)):
            print(str(missingValuesDead[i]) + " " + str(missingValuesDead[i] / len(deadPassangers)))

    def findMissingValues(passangers):
        auxiliar = Passanger()
        missingValues = []
        for field in auxiliar.__dict__.keys():
            x = [getattr(passanger, field) for passanger in passangers]
            valueToFind = auxiliar.__dict__.get(field)
            indices = [index for index, element in enumerate(x) if element == valueToFind]
            missingValues.append(len(indices))
        return missingValues

    def addAgeGroupColumn(data):
        ages = []
        x = np.arange(0, len(data), 1)
        for i in range(len(data)):
            age = data.at[i, 'Age']
            ages.append(Passanger.getAgeGroup(age))
        data['Age Group'] = ages
        plt.title("Age group")
        plt.hist(x)
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
        print("Kids percentage : " + str(len(kids) / len(passangers)))
        plt.bar([0, 1], [kidsPercentage, adultsPercentage])
        plt.xticks([0, 1], ['Kids', 'Adults'])
        plt.show()

    def checkNameTitles(passangers):
        maleTitles = ['Mr.', 'Mrs.', 'Don.', 'Master.']
        femaleTitles = ['Ms.', 'Miss.']
        maleTitlesCount = [0, 0, 0, 0]
        femaleTitlesCount = [0, 0]
        incorrectMatching = 0
        for passanger in passangers:
            tokens = passanger.name.split(" ")
            hasMaleTitle = 0
            for title in maleTitles:
                if title in tokens:
                    hasMaleTitle = 1
                    maleTitlesCount[maleTitles.index(title)] += 1

            for title in femaleTitles:
                if title in tokens:
                    femaleTitlesCount[femaleTitles.index(title)] += 1
            if (hasMaleTitle and passanger.sex == 'female') or (hasMaleTitle == 0 and passanger.sex == 'male'):
                incorrectMatching = 1
                print(passanger)
        print("Names are correct : " + str(1 - incorrectMatching))
        plt.bar(np.arange(0, len(maleTitles) + len(femaleTitles), 1), maleTitlesCount + femaleTitlesCount)
        plt.xticks(np.arange(0, len(maleTitles) + len(femaleTitles), 1), maleTitles + femaleTitles)
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

