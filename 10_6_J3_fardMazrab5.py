# برنامه ای بنویسید یک عدد صحیح از کاربر بگیرد و مجموع اعداد فرد از صفر تا آن عدد را محاسبه کرده و در مجموع اعداد مضرب 5 از صفر تا آن عدد ضرب کند.

# number / 0+1+3+5+7....+number (number odd or even ) 

num = int( input( 'Number : ' ))
jam = 0

if num % 2 == 0 :
    for i in range(1, num, 2):
        jam += i
    print(jam)

else:
    for i in range(1, num + 1, 2):
        jam += i
    print(jam)


for i in range(0, num + 1 , 5) :
    jam += i
    print(i)
print(jam)


# Teacher's code

n = 1000
s_odd = 0
s_5 = 0

for i in range( n + 1 ):
    if i % 2 != 0:
        s_odd += i
    if i % 2 == 0 :
        s_5 += i

s_5 * s_odd
