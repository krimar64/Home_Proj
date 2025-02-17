# String concatenation
# write "subscribe to ____"
# youtuber = "Kylie Ying" # some string variable

# a few way to do this
# print(subscribe to " + youtuber)
# print(subscribe to {}" .format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous = input("Famous: ")

madlib = f"Computer programming is so {adj}! It makes me excited because \
I love to to {verb1} Stay hydrated and {verb2} like you are {famous}!"

print(madlib)