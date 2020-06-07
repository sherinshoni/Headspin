def sum_series(num):
    sum=0
    fact=1
    for i in range(1,num+1):
        fact=fact*i
	sum=sum+(i/fact)
    return sum

num=int(input("Enter the number"))
sum=sum_series(num)
print("Sum of the series = ",sum)
