from datetime import date
from docxtpl import DocxTemplate


def getDate():
    today = date.today()
    month = today.month
    day = str(today.day)
    year = str(today.year)
    if month == 1:
        monthString = "January"
    elif month == 2:
        monthString = "February"
    elif month == 3:
        monthString = "March"
    elif month == 4:
        monthString = "April"
    elif month == 5:
        monthString = "May"
    elif month == 6:
        monthString = "June"
    elif month == 7:
        monthString = "July"
    elif month == 8:
        monthString = "August"
    elif month == 9:
        monthString = "September"
    elif month == 10:
        monthString = "October"
    elif month == 11:
        monthString = "November"
    elif month == 12:
        monthString = "December"
    else:
        print("Invalid date, Please correct")

    fullStringDate = monthString + " " + day + ", " + year
    return fullStringDate


dateString = getDate()
companyName = input("Enter Company name: ")
jobId = input("Enter Job ID: ")
positionName = input("Enter position Name: ")
