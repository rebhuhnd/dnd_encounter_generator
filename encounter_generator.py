import sys
import generator

args = sys.argv
if len(args)<=1:
    choice = raw_input("Enter name of encounter table file to use: ")
else:
    choice = args[1]

gen = generator.Generator()
gen.load(choice)

gen.get_encounter_message()

raw_input("Press any key to exit.")
