# Iterating a list in reverse order
a = ["foo", "bar", "baz"]
#Using reversed
for i in reversed(a):
  print(i)

# Enumerate returns a generator and generators cannot be reversed so we need to convert it into a list
# https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
for i, e in reversed(list(enumerate(a))): 
  print(i, e) 
  
# Range with step
for i in range(len(a) - 1, -1, -1): 
  print(i, a[i])
  
#Using slices [::-1] reverses array for the loop but not permanently
for item in a[::-1]:
    print item
    
 

