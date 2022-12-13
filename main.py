range(100)
list(range(100))

def make_list(num):
  result = []
  for i in range(num):
    result.append(i*2)
  return result

my_list = make_list(100)
# my list points to a location in memory
print(my_list)

# range() is a generator so the list is never created in memory so it doesnt take up space

# generators are always iterable

# The following code will take up unnessacery space in memory

print(list(range(100000)))

def generator_function():
  for i in range(100000):
    yield i

for item in generator_function(1000):
  print(item)

