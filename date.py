import datetime
from dateutil.relativedelta import *

date_1 = input("Enter a date in the format YYYY,MM,DD: ")
date_2 = input("Enter a date in the format YYYY,MM,DD: ")

start = datetime.datetime.strptime(date_1, '%Y,%m,%d')
end = datetime.datetime.strptime(date_2, '%Y,%m,%d')

split1 = date_1.split(',')
split2 = date_2.split(',')

diff = relativedelta(datetime.date(int(split2[0]),int(split2[1]),int(split2[2])), datetime.date(int(split1[0]),int(split1[1]),int(split1[2])))

print('Complete Difference between two dates: ')
print(diff.years , ' years, ', diff.months, ' months and ', diff.days, ' days')