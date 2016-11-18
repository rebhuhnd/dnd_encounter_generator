import sys
import generator

args = sys.argv
if len(args)<=1:
    choice = raw_input("Enter name of encounter table file to use: ")
else:
    choice = args[1]

gen = generator.Generator()
gen.load(choice)

get_another=True

while get_another:
	gen.get_encounter_message()
	get_another = 'y' in raw_input("Get another encounter from this table? (y/n)")

raw_input("Press any key to exit.")
