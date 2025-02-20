import numpy as np

array_1D = np.array([5,10,15,20,25])

print(array_1D)

print("\n" + "-" *20 + "\n")

array_a2 = np.array([1,2,3,4,5])

index = 0
for number in array_a2:

    array_a2[index] = number + 10
    index = index + 1

print(array_a2)

print("\n" + "-" *20 + "\n")

data = np.array([[1, 2], [3, 4]])

print(data)

print("\n" + "-" *20 + "\n")

array_a4 = np.array([1,2,3,4,5])

print(array_a4.mean())
print("\n" + "-" *20 + "\n")

array_a5 = np.array([1,2,3,4,5])

print(array_a5[0], array_a5[len(array_a5)-1])

print("\n" + "-" *20 + "\n")


