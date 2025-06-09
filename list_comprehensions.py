# Program will make list 3d that cant be equal to n

x = int(input("Insert First Number : "))
y = int(input("Insert Second Number : "))
z = int(input("Insert Third Number : "))
n = int(input("Insert Fourth Number : "))

result = [[i,j,k]
        for i in range (x + 1)
        for j in range (y + 1)
        for k in range (z + 1)
        if i+j+k != n]

print(result)