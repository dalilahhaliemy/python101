# say we wanna find the most frequent item
from collections import Counter

text = "They have come to realize that their freedom is inextricably bound to our freedom "\
        "We cannot walk alone. And as we walk we must make the pledge that we shall "\
        "always march ahead. We cannot turn back. There are those who are asking the devotees "\
        "of civil rights, 'When will you be satisfied?' We can never be satisfied as long as "\
        "the Negro is the victim of the unspeakable horrors of police brutality."
text_lower = text.lower()   # to ensure it is not case sensitive

# first, we need to break these strings into words and put all in a list
words = text_lower.split()
print(words)

# now we want to check the frequency of each word
counter = Counter(words)                 # set an object to use in the function Counter
top_three = counter.most_common(3)
print(top_three)
