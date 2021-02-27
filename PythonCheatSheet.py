''' Lists '''
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
    
#Slices in Python
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
a[start:stop:step] # start through not past stop, by step


'''
Heaps
By default implements a min heap (heapq is the module)
https://docs.python.org/3/library/heapq.html
'''
heapq.heapify(x) #Transform list x into a heap, in-place, in linear time.
heapq.heappop(x) #Heap pop from heap x
heapq.heappush(x,1) 
'''
Push item on the heap, then pop and return the smallest item from the heap. 
The combined action runs more efficiently than heappush() followed by a separate call to heappop().
'''
heapq.heappushpop(heap, item)



'''
Counter example
You have a long string of words with no punctuation or capital letters and you want to count how many times each word appears.
You could use a dictionary or defaultdict and increment the counts, but collections.Counter provides a cleaner and more convenient way to do exactly that. 
Counter is a subclass of dict that uses 0 as the default value for any missing element and makes it easier to count occurrences of objects:
'''
from collections import Counter
words = "if there was there was but if \
there was not there was not".split()
counts = Counter(words)
counts #Counter({'if': 2, 'there': 4, 'was': 4, 'not': 2, 'but': 1})

'''
When you pass in the list of words to Counter, it stores each word along with a count of how many times that word occurred in the list.
Are you curious what the two most common words were? Just use .most_common():
'''
counts.most_common(2) #[('there', 4), ('was', 4)]
#.most_common() is a convenience method and simply returns the n most frequent inputs by count.

counts.most_common()[0][0] #To find the most common element

#Iterating items in counter
for w,c in counts:
  print(w,c)
  
  

    
 

