#   و مقدار ارقام و رشته ها را در متغییرهای جداگانه ای ذخیره کند days2hours24 برنامه ای بنویسید مقداری مثل .


note = 'days2hours24'

digit = 0
alpha = ''

for i in note:
    if i.isdigit():
        digit = int(digit) + int(i) 
    else:
        print(note)
print(digit)
