import math
import bitarray
a = bitarray.bitarray()
with open('test.mp3', 'rb') as fh:
    a.fromfile(fh)
print(len(a), ' len')
start = int(len(a)/2-3*math.sqrt(len(a)))
end = int(len(a)/2+3*math.sqrt(len(a)))
# seq = a[0:-1]
#
# print(seq)
