from Surse.passanger import Passanger


def executeTasks(fileName):
	passangers = Passanger.readPassangersCsvFile(fileName)
	data = Passanger.getCsvData(fileName)
	# Passanger.printSurvivorPercentage(passangers)
	# Passanger.printHistogram(passangers)
	# Passanger.printMissingValues(passangers)
	newData = Passanger.addAgeGroupColumn(data)
	newData.to_csv("Date/age_group_added.csv")

