madLibs = "\n{} is having a {} party!\nIt's going to be at {} on {}.\nPlease make sure to show up at {}, or else you will be required to {} with your {}.\nRSVP at {}."

name = input("Enter a name: ").title()
theme = input("Enter a theme for the party: ").lower()
place = input("Enter a place name: ")
day = input("Enter a day of the week: ").capitalize()
time = input("Enter a time: ").upper()
verb = input("Enter a verb: ").lower()
animal = input("Enter a type of animal: ").lower()
bodyPart = input("Enter a body part: ").lower()
contact = input("Enter some contact information: ")

if animal[0] in ["a", "e", "i", "o", "u"]:
    animal = verb + " an " + animal
else:
    animal = verb + " a " + animal

print(madLibs.format(name, theme, place, day, time, animal, bodyPart, contact))
