from calendar import month_abbr
from datetime import datetime as dt
import jalali

year1 = int( input( 'Year : ' ) )
month1 = int( input( 'Month : ' ) )
day1 = int( input( ( 'Day : ' ) ) ) 
print( 'Your Birthday is', year1,'/',month1,'/',day1 )

sal = jalali.Gregorian(dt.today().year, dt.today().month , dt.today().day ).persian_string()


shamsY = int( sal[:4] ) 
shamsM = int( sal[5:6] )
shamsD = int( sal[7:9] )

print(shamsY, shamsM, shamsD)

birthday =  (shamsY - year1 ) *365 + (shamsM - month1)*30 + shamsD - day1    

print( f'you lived { birthday } days! ' )
