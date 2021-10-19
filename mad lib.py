"""

# string concatenation (aka to put strings together)
# suppose we want to create a string that says "susbscribe to an youtuber"

youtuber = "a" # a string variable

# a few ways to do this
print ("subscribe to " + youtuber)
print ("subscribe to {}".format(youtuber))
print (f"subscribe to {youtuber}")

"""
name = input("What is your name?")
adj1 = input("Adjective: ")
verb = input ("Verb: ")
adj2 = input("Adjective: ")
famous_person = input("Famous Person: ")

madlib = f"My name is {name}." \
         f"Computer programming is so {adj1}! " \
         f"I'm excited to learn more about it all the time." \
         f"I love {verb}ing very much!" \
         f"Stay hungry and {adj2} like you are {famous_person}"
print (madlib)
