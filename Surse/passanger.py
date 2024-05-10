import pandas as pd
import numpy as np
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

    def __init__(self, passangerId, pclass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked):
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

    def print(self):
        print(str(self.passangerId) +
              " NAME: " +
              self.name +
              " CLASS: " +
              str(self.pclass) +
              " SEX: " +
              self.sex +
              " AGE: " +
              str(self.age) +
              " SIBSP: " +
              str(self.sibSp) +
              " PARCH: " +
              str(self.parch) +
              " TICKET: " +
              str(self.ticket) +
              " FARE: " +
              str(self.fare) +
              " CABIN: " +
              str(self.cabin) +
              " EMBARKED: " +
              str(self.embarked))

    def readPassangersCsvFile(fileName):
        with open(fileName) as file:
            passangers = []
            fieldName = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
            data = pd.read_csv(fileName)
            numberColumns = len(data.columns)
            dataTypes = data.dtypes
            for i in range(len(data)):
                passanger = Passanger(data.at[i,'PassengerId'],
                                      data.at[i,'Pclass'],
                                      data.at[i,'Name'],
                                      data.at[i,'Sex'],
                                      data.at[i,'Age'],
                                      data.at[i,'SibSp'],
                                      data.at[i,'Parch'],
                                      data.at[i,'Ticket'],
                                      data.at[i,'Fare'],
                                      data.at[i,'Cabin'],
                                      data.at[i,'Embarked'])
                passangers.append(passanger)
            print("Number of columns: " + str(numberColumns))
            print("Column types : \n" + str(dataTypes))
            for i in range(len(fieldName)):
                print(fieldName[i] + " " + str(len(data[data[fieldName[i]].isna()])))
            if len(data[data.duplicated()]) == 0:
                print("No dublicated rows")
            else:
                print("There are dublicated rows")
            print("Number rows: " + str(len(data)))
        return passangers

