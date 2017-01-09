import string

f = open('input.txt')
f.readline()
f.readline()
N = f.readline()
d = {}
for line in f:

    #words = line.strip().split(' - ')

    words = line.strip(' \t\n\r ').replace(' ','').split('-')
    #print(words)

    en = words[0]
    lat = words[1].split(',')
    print(en)
    print(lat)
    for key in lat:
        if key in d:
            d[key].append(en)
            print("if  ", d)
        else:
            d[key] = [en]
            print("else  ", d)
f.close()

for key in d:
   d[key].sort()
print("sort  ", d)

g = open('output.txt', 'w')
g.write(str(len(d)) + '\n')
for lat in sorted(d):

    g.write(lat + ' - ' + ', '.join(d[lat]) + '\n')
print("sorted  ", sorted(d))
g.close()