import random

# Rolls the dice.

def d(n):
    # d% appears to be just dice that roll for the ten's place
    # and the 1s place.
    if n == "%":
        return d(10)*10+d(10)

    # d10 goes from 0 to 9
    if n == 10:
        return random.randint(0,9)

    # Most other dice go from 1 to n, such as d4, d6, and d8
    return random.randint(1,n)

## Parses a dice roll. This is very simple at the moment, and only accepts
## the following formats:
##
## n (1,2,3, etc.)
## d n (d20, etc.)
## n d m (1d4, 2d6, etc.)
def dparse(string):
    if 'd' in string:
        parts = string.split("d")
        if len(parts) == 1:
            return d(int(parts[0]))
        else:
            total = 0
            if parts[0] == '':
                n == 1
            else:
                n = int(parts[0])

            for k in range(0, n):
                total = total + d(int(parts[1]))

            return total
    else:
        return (int(string))

## The encounter generator stores a table of possible encounters.
class Generator:
    def __init__(self):
        self.encounters = {}
        for x in xrange(0, 100):
            self.encounters[x] = None

        self.encounter_chance = 20

    # load the encounter table
    def load(self, filename):
        f = open(filename, 'r')
        line_no = 0

        for line in f:
            parts = line.split(",")
            if line_no == 0:
                self.encounter_chance = int(parts[1])
                print "Encounter chance:", self.encounter_chance

            elif line_no == 1:
                ## Do nothing
                pass

            elif line_no > 1:
                d_percent = parts[4].split("-")
				# Single percent value.
                if len(d_percent) == 1:
                    self.encounters[int(d_percent[0])] = parts
				# Percent range.
                else:
                    n1 = int(d_percent[0])
                    n2 = int(d_percent[1])

                    for x in xrange(min([n1,n2]), max([n1,n2])+1):
                        self.encounters[x] = parts

            line_no = line_no+1

    ## Get an encounter message. Prints a possible encounter to a screen.
    def get_encounter_message(self):
        # roll to see if there is an encounter

        roll = d("%")
        print "Roll to determine if encounter is found yielded: ",roll

		
        if roll >= self.encounter_chance:
            print "Nothing happens.", str(roll)+">"+ str(self.encounter_chance)
            return
        else:
            # if there is an encounter, decide what it is
            roll = d("%")
            # check which encounter it is on the table
            print "Roll on encounter table is:",roll

            encounter = self.encounters[roll]

            if encounter == None:
                print "Encounter for this roll not listed"
            else:
                print encounter
                print "You encounter:"

				## Determine the number of a certain creature.
                number=dparse(encounter[2])
                CR = encounter[0]
                name=encounter[1]
                habitat=encounter[3]
                notes=encounter[5]

                print "CR (%s)"%CR,number,name,
                if habitat != "":
                    print "in a",habitat
                else:
                    print ""
                print "Notes:",notes

    # number of encounters
    def num_encounters(self):
        return len(self.encounters)
