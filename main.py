len = int(input("Введите длину массива: "))

numbers=[0]*len

for i in range (0,len):
    numbers[i] = int(input("Введите число: "))

numbers_2=[0]*len

for i in range(0,len):
    numbers_2[i] = pow(numbers[i],2)

print(numbers_2)