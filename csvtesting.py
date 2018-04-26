# Read and writes to csv files

import csv

# testread not included in repository
with open("testread.csv", newline = "") as csvfile:
	testreader = csv.DictReader(csvfile, delimiter = ",")
	rows = list(testreader)
	for row in rows[:2]:
			print(row)


with open("testwrite.csv", "a") as csvfile:
	fieldnames = ["recipe", "ingredients", "time", "instructions"]
	testwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
	
	testwriter.writeheader()
	testwriter.writerow({
		"recipe": "fajitas",
		"ingredients": "xyz",
		"time": "15 mins",
		"instructions": "abc"
	})
	testwriter.writerow({
		"recipe": "stew",
		"ingredients": "cde",
		"time": "60 mins",
		"instructions": "fgh"
	})