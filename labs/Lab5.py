import datetime


while True:
    try:
        bday = input("Please enter your exact Date of Birth(eg:-10 02 2022):")
        birthday = datetime.datetime.strptime(bday, '%m %d %Y')
        break
    except:
        print("Please follow the format Month: 01-12 Day:01-31 year:1980-2022, dont in")

tday = datetime.datetime.today()
timedelta = (tday - birthday).total_seconds()
print("You have been alive for:",timedelta,"seconds")
