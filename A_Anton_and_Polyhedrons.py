n = int(input())
polygons = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8,"Dodecahedron": 12, "Icosahedron" : 20 }
sum = 0
for i in range(n):
    poly = input()
    sum += polygons[poly]
print (sum)