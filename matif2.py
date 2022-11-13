a = [1,2,3,4,5,6,7]
b = [4,5,6,7,8,9]
r = [[1,5],[4,5],[1,4],[4,6],[3,7],[7,6]]
domain = []
Range = []
invers = []

#Domain
for i in range(len(r)):
    hasil = r[i][0]
    domain.append(hasil)
domain = list(dict.fromkeys(domain))
print ("Domain",sorted(domain))

#Range
for j in range(len(a)):
    untuka = a[j]
    for i in range (len(b)):
     untukb = b[i]
     if untuka == untukb:
         Range.append(untuka)
print("Range",Range)

#invers dari Rcl
for i in range (len(r)):
    temp = r[i][0]
    r[i][0] = r[i][1]
    r[i][1] = temp
    invers.append(r[i])
print("invers R",invers)
