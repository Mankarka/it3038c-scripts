import datetime

while True:
        bday = input("Please enter your exact Date of Birth(eg:10 02 2022):")
        birthday = datetime.datetime(bday,'%m %d %Y')
        break
else:
        print("Please follow the format Month: 01-12 Day:01-31 year:1980-2022")

tday = datetime.datetime.today
timeSec = (tday - birthday).total_seconds()
print("You have been alive for:",timeSec,"seconds")
