import datetime

def ageChecker(age):
    if age >= 18:
        return "You are in legal age!"
    else:
        return "You are a minor!"

startYear = int(input("Birth year: "))
startMonth = int(input("Birth month: "))
startDay = int(input("Birth day: "))

userBirthday = datetime.datetime(startYear, startMonth, startDay)

y = datetime.datetime.now()

z = y - userBirthday
z.total_seconds

yearsOld = z.days//365

print(f"""
================================================      
You have lived for {z.days} days, {z.seconds} seconds, and
you are {yearsOld} years old! {ageChecker(yearsOld)}
================================================""")