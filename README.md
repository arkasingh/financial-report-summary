# Financial Report Extraction and Summarization

Here we are trying to extract financial reports from a pdf file and create an Excel sheet with all the meaningful fields from each report.
We use the Investigation Details field and feed it into our language model to generate a short summary against each report and write that back to our spreadsheet.

We have a [*Sample Financial Reports Data.pdf*](https://github.com/arkasingh/text-summary/blob/main/Data/Sample_Financial_Reports_Data.pdf)
with financial reports.

pdf2excel.py creates Excel file output.xlsx
summarize.py takes the Excel file as input and modifies it to add a Report Summary.
