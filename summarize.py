
import pandas as pd
from transformers import pipeline
from openpyxl import load_workbook

excel_path = "text-summary/output.xlsx"
df = pd.read_excel(excel_path)

summary = []

#Summarizing texts for each report
summarizer = pipeline("summarization", model="philschmid/bart-large-cnn-samsum")
for i in range(len(df)):
    input_text = df['INVESTIGATION DETAILS'][i]
    output = summarizer(input_text, max_length=300, min_length=30, do_sample=False, truncation=True)
    summary_text = output[0]['summary_text']
    print("Summary Report #{}:{}".format(i+1,summary_text))
    summary.append(summary_text)

#Adding new column for summarized text
df['Generated Summary'] = summary

# Generating workbook
ExcelWorkbook = load_workbook(excel_path)
# Generating the writer engine
writer = pd.ExcelWriter(excel_path, engine = 'openpyxl')
# Assigning the workbook to the writer engine
writer.book = ExcelWorkbook
# Adding the Sumarries to the excel as a new sheet
df['Generated Summary'].to_excel(writer, sheet_name = 'Summary', index=False)
writer.save()
writer.close()
