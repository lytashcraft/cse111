import random

def main():
    # A singular past tense phrase
    print(make_sentence(1, "past"))

    # A singular present tense phrase
    print(make_sentence(1, "present"))

    # A singular future tense phrase
    print(make_sentence(1, "future"))

    # A plural past tense phrase
    print(make_sentence(2, "past"))

    # A plural present tense phrase
    print(make_sentence(2, "present"))

    # A plural future tense phrase
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Build and return a sentence with four components:
    a determiner, a noun, a prepositional phrase, and a verb.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    phrase = get_prepositional_phrase(quantity)
    verb = get_verb(quantity, tense)

    sentence = f"{determiner} {noun} {phrase} {verb}."
    return sentence.capitalize()

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

def get_preposition():
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of a preposition, a determiner, and a noun.
    """
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    phrase = f"{preposition} {determiner} {noun}"
    return phrase

main()
