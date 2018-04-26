# Writes a list to a txt file
import sys

def remember(thing):
	# open file
        with open("thingstoremember.txt", "a") as file:
                # write to file
                file.write(thing+"\n")


def show():
        # open file
        with open("thingstoremember.txt") as file:
               for line in file:
                       print(line)




if __name__ == "__main__":
        remember(input("What should I remember? "))
        show()
