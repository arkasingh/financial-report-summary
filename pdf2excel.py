import pdfplumber
import pandas as pd
import re

def report_fields(report):
    data_fields = {
        'Report #': r"FINANCIAL REPORT\s(.+)",
        'Reporting Entity': r"Reporting Entity/\s(.+)",
        'Transaction date': r"Transaction date\s(.+)",
        'Account Holder': r"Account holder\s(.+)",
        'Conductor': r"Conductor\s(.+)",
        'DECISION STR': r"DECISION STR\s([\w\s\(\).,]+)(?=ADVISORY|INVESTIGATION SUMMARY)",
        'INVESTIGATION SUMMARY': r"INVESTIGATION SUMMARY\s([\w\s.\(\),$\-’]+)(?=Business Client Profiles|Client Profile:)",
        'Name': r"Name: (.+)",
        'Ref. No.': r"Ref\. No\.?:? (\d+)",
        'Gender': r"Gender:\s(.+)",
        'Date of Birth': r"Date of Birth:\s(.+)",
        'Address': r"Address:\s([\d\w\s,]+)(?=Phone)",
        'Phone': r"Phone:?([\(\w\):\-\d ]+)",
        'E-mail': r"E-mail:\s(.+)",
        'Business Type': r"Business Type:\s([\w\s\-]+)(?=\sOwner)",
        'Owner': r"Owner\(s\):\s(.+)",
        'Business Owned': r"Business Owned:(.+)",
        'Authorities': r"Authorities:(.+)(?=\sClient)",
        'Identifiction': r"Identifiction:\s([\w\n \d]+)(?=Occupation)",
        'Occupation': r"Occupation:\s(.+)",
        'Employer': r"Employer:\s(.+)",
        'Client Since': r"Client Since:\s(.+)",
        'Established': r"Established:(.+)",
        'DATATHON Accounts': r"DATATHON Accounts:([\w\d\s\n\-\(\),\]\[]+)(?=Legal Name|Client Profile Name|INVESTIGATION DETAILS)",
        'INVESTIGATION DETAILS': r"INVESTIGATION DETAILS\s([\s\w\.\-\,\(\)\a$:;\’\[\]/]+)(?=CONCLUSION|RECOMMENDATION)",
        'RECOMMENDATION': r"RECOMMENDATION\s([\w\s\’,.\-]+)(?=\sAPPENDICES|\sREFERENCES)",
        'APPENDICES': r"APPENDICES\s([\w\s\:.\-$,]+)(?=\sREFERENCES)",
        'REFERENCES': r"REFERENCES\s([\w\s\:.\-$,\/”\[\]:\(\)]+)(?=\sREPORTING)",
        'ACTIONS TAKEN': r"S ACTIONS TAKEN\s“([\w\s.]+)"
    }
    new_data = {}
    report = re.sub(r"Page \d+ of \d+", "", report)
    for key in data_fields.keys():
        new_data[key] = "\n\n".join(re.findall(data_fields[key], report))
    return(new_data)

#Extract text from PDF
file_path = 'text-summary/Sample Financial Reports Data.pdf'
excel_path = "text-summary/output.xlsx"
mypdf = pdfplumber.open(file_path)

reports = []
data = []
curr_report = ''
flag = 0

#extracting the fields from the report
for i in range(len(mypdf.pages)):
    curr_page = mypdf.pages[i].extract_text()
    #finding the beginning of a report
    if re.search('FINANCIAL REPORT', curr_page):
        flag = 1
        if len(curr_report) > 0:
            data.append(report_fields(curr_report))
        curr_report = ''
    if flag == 1:
        curr_report = curr_report + curr_page
data.append(report_fields(curr_report)) #adding the last report

#converting list to dataframe and saving in an excel
df = pd.DataFrame(data)
df.to_excel(excel_path, sheet_name = 'Report details', index=False)
