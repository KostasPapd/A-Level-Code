def isLeap(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False

def isValDay(d, m, y):
    dayStr = str(d)
    if len(dayStr) == 2 or len(dayStr) == 1:
        m31 = [1, 3, 5, 7, 8, 10, 12]
        if m == 2:
            if isLeap(y) == True:
                maxDay = 29
            else:
                maxDay = 28
        elif m in m31:
            maxDay = 31
        else:
            maxDay = 30
        if d >= 1 and d <= maxDay:
            return True
        else:
            return False
    else:
        return False


def isValMon(m):
    mStr = str(m)
    if len(mStr) == 2 or len(mStr) == 1:
        if m > 0 and m < 13:
            return True
        else:
            return False
    else:
        return False

def isValYear(y):
    length = str(y)
    if len(length) == 4:
        return True
    else:
        return False

def isValDate(date):
    dd = int(date[:2])
    mm = int(date[3:5])
    yyyy = int(date[6:10])
    day = isValDay(dd, mm, yyyy)
    month = isValMon(mm)
    year = isValYear(yyyy)
    if day == True:
        if month == True:
            if year == True:
                print("The date is valid")
            else:
                print("The date is invalid")
        else:
            print("The date is invalid")
    else:
        print("The date is invalid")

def main(date):
    dayLen = len(date)
    while dayLen != 10:
        date = input("Enter your date in the format dd mm yyyy: ")
        dayLen = len(date)

    isValDate(date)

date = input("Enter your date in the format dd mm yyyy: ")
main(date)
