import numpy as np

a = np.empty((5, 5), np.object)
print(a)

a[2, 1] = 'P'
a[2, 3] = 'P'
print(a)

print(a == 'P')

print(a[np.where(a == 'P')])

places = np.empty((10, 10), np.object)
places[2, 3] = 'H'
places[7, 5] = 'P'
places[1, 3] = 'P'
places[7, 2] = 'H'

types = ['P', 'H']
for t in types:
    locations = np.where(places == t)
    print(t, locations)


def distance(current, other):
    total = (current[0] - other[0]) ** 2 + (current[1] - other[1]) ** 2
    return total ** 0.5


row = int(input('Satir: '))
col = int(input('Sutun: '))
current = [row, col]
for t in types:
    locations = np.where(places == t)
    X = locations[0]
    Y = locations[1]
    mindist = 1000
    minloc = None
    for i in range(len(X)):
        loc = [X[i], Y[i]]
        dist = distance(current, loc)
        if dist < mindist:
            mindist = dist
            minloc = loc
    print("En yakin %s locaksyonu (%d,%d) konumunda ve %d uzaklıktadır"
          % (t, minloc[0], minloc[1], mindist))
