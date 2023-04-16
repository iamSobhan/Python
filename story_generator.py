import random

# Set up the story template
story_template = "Once upon a time, there was a {adj} {noun} named {name}. {name} loved to {verb} all day long, but one day, {pronoun} {verb}ed {adv} and found a {adj2} {noun2} in the {place}. {name} was so {adj3} that {pronoun} {verb2}ed the {noun2} all the way home."

# Set up the word lists
adjectives = ["happy", "sad", "funny", "serious", "angry", "sleepy"]
nouns = ["cat", "dog", "bird", "fish", "snake", "lion"]
names = ["Tom", "Jerry", "Alice", "Bob", "Lucy", "Peter"]
verbs = ["run", "jump", "sleep", "eat", "dance", "sing"]
pronouns = ["he", "she", "it"]
adverbs = ["quickly", "slowly", "carefully", "happily", "sadly"]
adj2s = ["big", "small", "colorful", "beautiful", "ugly"]
noun2s = ["flower", "tree", "rock", "river", "mountain"]
places = ["park", "forest", "beach", "mountain"]

# Generate the story
adj = random.choice(adjectives)
noun = random.choice(nouns)
name = random.choice(names)
verb = random.choice(verbs)
pronoun = random.choice(pronouns)
adv = random.choice(adverbs)
adj2 = random.choice(adj2s)
noun2 = random.choice(noun2s)
adj3 = random.choice(adjectives)
verb2 = random.choice(verbs)

story = story_template.format(adj=adj, noun=noun, name=name, verb=verb, pronoun=pronoun, adv=adv, adj2=adj2, noun2=noun2, adj3=adj3, verb2=verb2, place=random.choice(places))

print(story)
