import PdfDeal
import ExcelFill




#pdf = PdfDeal.pdfplumber.open(r'D:\Downloads\Compressed\02. Evaluation until 30.08.2022\01 VP50647\VP50647.pdf')
# pdf = PdfDeal.pdfplumber.open(r'D:\Downloads\Compressed\02. Evaluation until 30.08.2022\02 VQ57622\VQ57622.pdf')
# print(pdf.pages[0].extract_tables()[0][8][0])

deal = PdfDeal.PDFDeal(r'D:\Downloads\Compressed\02. Evaluation until 30.08.2022')

excel = ExcelFill.ExcelFill(r'D:\Downloads\Compressed\2022-09-20 Aeko Task List.xlsx')

## excel.FillTaskList(deal.AA())

print(deal.GetAllContent())


