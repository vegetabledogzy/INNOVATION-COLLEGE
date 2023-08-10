# coding: utf-8

# In[5]:


# Part 1: mapList
def mapList(func, L):
    result = []
    for item in L:
        result.append(func(item))
    return result


def sq(x):
    return x * x


print 'Part 1: mapList'
print(mapList(sq, [1, 2, 3, 4]))


# In[14]:


# Part 2: sumAbs
def mapList(func, L):
    return func(L)


def sumAbs(L):
    for (index, x) in enumerate(L):
        if x < 0:
            L[index] = abs(x)
    return sum(L)

print 'Part 2: sumAbs'
print(mapList(sumAbs, [-1, 2, -3, 4]))


# In[17]:


# Part 3: mapSquare
def mapSquare(func, L):
    squareList = []
    for item1 in L:
        tempList = []
        for item2 in L:
            tempList.append(diff(item1, item2))
        squareList.append(tempList)
    return squareList

def diff(x, y):
    return x - y

print 'Part 3: mapSquare'
print(mapSquare(diff, [1, 2, 3]))

# In[23]:


nested = [[[1, 2],
           3],
          [4,
           [5, 6]],
          7,
          [8, 9, 10]]


# print(nested)
def recursiveRef(L, location):
    result = L
    for index in location:
        result = result[index]
    return result


print(recursiveRef(nested, [3, 1]))
print(recursiveRef(nested, [1, 1, 0]))
print(recursiveRef(nested, [1, 1]))
