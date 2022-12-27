# یک عدد صحیح از کابر بگیرید و میانگین اعدا از صفر تا آن عدد را محاسبه کنید (از حلقه استفاده کنید)

number = int(input( 'Number : ' ))

# 0 + 1 + 2 + 3 + ... + number

firstNum = 0

for i in range(number+1):
    firstNum += i
    miangin = firstNum / number
print(miangin)

