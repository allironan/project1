# collect input
story = input("Tell me a magical story!: ")
# declare substring to be searched
sub = "was";
# create amount integer for counted valeu
amount = story.count(sub)
print "Wow, you said was %s times!" % amount
