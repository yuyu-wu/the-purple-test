# *args Exercise: The Purple Test
# Define a function contains_purple  that accepts any number of arguments.  It should return True  if any of the arguments are "purple" (all lowercase). Otherwise, it should return False .  For example:

# contains_purple(25, "purple")   #True

# contains_purple("green", False, 37, "blue", "hello world")   #False

# contains_purple("purple")   #True

# contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")   #True

# contains_purple(1,2,3)  #False

def contains_purple(*args):
    if "purple" in args: return True
    return False