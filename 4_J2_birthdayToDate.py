from datetime import datetime as dt
import jalali

bd = input('Please enter your birthday like 1393-24-3 : ')
bd = jalali.persian(bd).gregorian_string()
bd = datetime.strptime(bd, '%y-%m-%d')
today = datetime.today()
delta = today - bd
print(delta)
