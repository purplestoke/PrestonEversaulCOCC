import numpy

array = numpy.random.randint(0,22, size=(5,5), dtype=int)
print(array)
print(array[1, 2])
print(numpy.sum(array))

for i in range(5):
    if i == 0:
        print(f"The mean across the horizontal axis is {numpy.mean(array, axis=1)}\n")
    print(f"Max Value in Column {i+1} is {numpy.max(array[:, i])}\n")
