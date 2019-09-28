from datetime import date
from docxtpl import DocxTemplate
from os import getcwd

def CoverLetter(companyName, id, location, positionName, date):
    doc = DocxTemplate("letter.docx")

    if(location == ""): 
        location = "Ottawa, Ontario"

    context = {
        'date': date,
        'company_name': companyName,
        'jobId': id,
        'location': location,
        'positionName': positionName
    }
    doc.render(context)
    return doc


def getDate(date):
    today = date.today()
    date = today.strftime("%B %d, %Y")
    return date


company_name = input("Enter Company name: ")
jobId = input("Enter Job ID: ")
location = input("Enter Location:")
positionName = input("Enter position Name: ")


doc = CoverLetter(company_name, jobId, location, positionName, getDate(date))

dist = getcwd()

doc.save(dist + '\\' + company_name + '-' + jobId + '.docx')
