from Surse.passanger import Passanger


def executeTasks(fileName):
	print("Choose command")
	print("1. Analyse .csv file")
	print("2. Print surviving percentage")
	print("3. Print the histograms of numerical columns")
	print("4. Print missing columns")
	print("5. Add age group column")
	print("6. Print surviving rate by age")
	print("7. Print surviving rate adults vs children")
	print("8. Check name titles")
	print("9. Replace missing values")
	print("10. Deaths graph by fare")

	command = int(input())
	passangers = Passanger.readPassangersCsvFile(fileName)
	data = Passanger.getCsvData(fileName)
	if command == 2:
		Passanger.printSurvivorPercentage(passangers)
	elif command == 3:
		Passanger.printHistogram(passangers)
	elif command == 4:
		Passanger.printMissingValues(passangers)
	elif command == 5 or command == 6:
		newData = Passanger.addAgeGroupColumn(data)
		newData.to_csv("Date/age_group_added.csv")
		if command == 6:
			Passanger.printSurvivingRateByAge(newData)
	elif command == 7:
		Passanger.printSurvivingRateKidsAdults(passangers)
	elif command == 8:
		Passanger.checkNameTitles(passangers)
	elif command == 9:
		fullData = Passanger.replaceMissingValues(data)
		fullData.to_csv("Date/no_missing_values.csv")
	elif command == 10:
		Passanger.analyseDeathsByFactors(data)

