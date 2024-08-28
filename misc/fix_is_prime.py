
def is_prime(num):
    list1 = []
    while num >= 2:
        if num % 1 != 0 and num % type(int) == type(int) and type(int) != 0:
            list = list.append(num)
        else:
            return True
    return list

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
