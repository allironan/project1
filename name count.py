# Import statements are supposed to go on top :)
import collections

# collect input
story = raw_input("Tell me a magical story!: ")

# Split the sentence by spaces
story_array = story.split(" ")

# Create Counter for words in the story
cnt = collections.Counter(story_array)

# Print output
print "Word count from your story:\n%s" % cnt
