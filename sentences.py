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
  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """

  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)

  sentence = (f"{determiner} {noun} {verb}.")
  return sentence.capitalize()

def get_determiner(quantity):
  """
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word


def get_noun(quantity):
  """
  Return: a randomly chosen noun.
    """
  if quantity == 1:
      words = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
  else:
      words = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_verb(quantity, tense):
  """
  Return: a randomly chosen verb.
  """
  if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  elif tense == "future":
        words = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"] 

     # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

main()