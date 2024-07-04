array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
length = len(array)
temp = 0
mediana = 0

for i in range(length-2):
    for j in range(length-i-1):
        if array[j] > array [j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp

print(array)

if length % 2 == 0:
    mediana = (array[length//2 - 1] + array[length//2]) / 2
else:
    mediana = array[length//2]
print(f"La mediana es {mediana}")