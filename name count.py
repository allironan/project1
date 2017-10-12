# collect input
story = raw_input("Tell me a magical story!: ")
# declare substring to be searched
# sub = "was"
# amount = story.count(sub)
story_array = story.split(" ")
import collections
cnt = collections.Counter(story_array)
# cnt = story_array.Counter("was")
# for word in ['was']:
    # cnt[word] =+ 1
print "Wow, you said was %s times!" % cnt
