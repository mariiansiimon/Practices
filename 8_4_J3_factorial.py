# یک عدد صحیح از کاربر بگیرید و فاکتوریل آن عدد را محاسبه کنید (از طریق حلقه).

# number = 5 -> 5! = 1 * 2 * 3 * 4 * 5

number = int(input(' Number : '))

fact = 1
for i in range(1,number+1):
    fact *= i
print(fact)
