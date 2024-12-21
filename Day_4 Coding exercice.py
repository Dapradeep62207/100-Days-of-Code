import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Get random item from list
# Option 1
print(random.choice(friends))

# Option 2
random_index= random.randit(0, 4)
print(friends[random_index])
