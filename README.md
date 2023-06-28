# Financial Report Extraction and Summarization

This project tries to extract financial reports from a pdf file and create an Excel sheet with all the meaningful fields from each report.
The Investigation Details field is fed into our language model to generate a short summary of each financial investigation report.

### Data
We have a [*Sample Financial Reports Data.pdf*](https://github.com/arkasingh/text-summary/blob/main/Data/Sample_Financial_Reports_Data.pdf)
with financial reports.

### Task 1 - Extracting fields from the unorganized pdf input data

The [!*Regular Expression*](https://docs.python.org/3/library/re.html) module is utilized in the [*pdf2excel.py*](https://github.com/arkasingh/text-summary/blob/main/pdf2excel.py) to extract the relevant data from the [*Sample Financial Reports Data.pdf*](https://github.com/arkasingh/text-summary/blob/main/Data/Sample_Financial_Reports_Data.pdf) file and outputs an Excel file [*output.xlsx*](https://github.com/arkasingh/text-summary/blob/main/Data/output.xlsx) with all the information organized.

### Task 2 - Summarizing Investigation Details

The "*INVESTIGATION DETAILS*" column is extracted from the Excel file [*output.xlsx*](https://github.com/arkasingh/text-summary/blob/main/Data/output.xlsx) in the 
[*summarize.py*](https://github.com/arkasingh/text-summary/blob/main/summarize.py) file. Hugging Face's [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) is utilized to summarize the investigation details and a Report Summary sheet is addedd to the Excel file as an output.

### Sample Result
#### Target Summary
This STR for 99999B.C. LTD. (and sole owner Kal Mao) relates to outgoing bank drafts, conducted between March 10, 2020 and May 29, 2020, which are deemed suspicious as the business is seemingly connected to the sale of unlicensed Cannabis. The outgoing bank drafts (which totaled $309,728.83) were sourced through e-transfers from various third parties (at various financial institutions). Some of the remitters of the e-transfers were using names such as CAMMA Trumpet as a payee name, which is seemingly connected to cammatrumpet.ca an online, unlicensed Cannabis dispensary. There is no indication on the Health Canada website that 99999B.C. LTD. or CAMMA Trumpet are licensed to produce or distribute Cannabis. Given that the account activities of 99999B.C. LTD. are seemingly linked to dealings with an unlicensed Cannabis dispensary, an STR is being filed.
#### Generated Summary
99999B.C.Ltd. received $310,557.79 in e-transfers from various third parties. Some of the third parties were using names such as Marijuana, Cannabis dealer, CAMMA Trumpet, and cammatrumpet.ca for a payee name. The website of the payee was seized by the Maple Leaf Police Service due to its contravention of the Cannabis Act.


