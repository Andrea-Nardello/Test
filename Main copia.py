# In[Esercizio 10.1]
def nasted_sum(t):
    somma = 0
    for i in t:
        somma += sum(i)
    return somma


t = [[1,2], [3], [4,5,6]]
nast = nasted_sum(t)
print(nast)

# In[Esercizio 10.2]

def cumsum(cina):
    a =[]
    for i in range(len(cina)):
        if i == 0:
            a.append(cina[i])
        else:
            a.append(cina[i]+a[i-1])
    return a
cergo = [1,2,3]
print(cumsum(cergo))
print(cergo)

# In[Esercizio 10.3]

def middle(t):
    a = t[1:-1]
    return a
print(middle([1,2,3,4]))

# In[Cap 11]

def histogram(s):
    d = dict()
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d
print(histogram("brontosaurus"))
