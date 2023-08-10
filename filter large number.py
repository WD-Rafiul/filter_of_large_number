d = {"ineuron" : {"a" : 14, "b" : 10, "c" : 4}, "course" : {"d" : 50, "e" : 34, "f" : 1}, "g" : 5+4j,
     "h" : [45,6,7,8,9,3], "i" : (45,25,2), "k" : "sudh", "l" : 110}
d1 = []
for i in d.values():
    if type(i) == dict or type(i) == list or type(i) == tuple:
        if type(i) == list or type(i)== tuple:
            for a in i:
                d1.append(a)
        else:
            for a in i.values():
                d1.append(a)
    elif type(i) == str or type(i) == complex:
        pass
    else:
        d1.append(i)
d1.sort()

print(d1[-1])m
