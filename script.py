from PyPDF2 import PdfFileMerger

pdfs = [r'PDF\COVER PAGE-.STUDY ABROAD  - 9 feb.pdf',r'PDF\INDEX- STUDY ABROAD.pdf',r'PDF\AUSTRALIA..pdf',r'PDF\Australia 1-10.pdf',r'PDF\CANADA...pdf', r'PDF\Canada 11-32.pdf',r'PDF\FINLAND..pdf', r'PDF\Finland 33-36.pdf',r'PDF\FRANCE..pdf',r'PDF\France 37-47.pdf',r'PDF\GERMANY..pdf',r'PDF\Germany 48-72.pdf',r'PDF\IRELAND..pdf',r'PDF\Ireland 73-91.pdf',r'PDF\ISRAEL..pdf',r'PDF\Israil 92-95.pdf',r'PDF\ITALY..pdf',r'PDF\Italy 96-125.pdf',r'PDF\JAPAN..pdf',r'PDF\Japan 126-133.pdf',r'PDF\NETHERLANDS..pdf',r'PDF\Netherland 134-143.pdf',r'PDF\NEW ZEALAND..pdf',r'PDF\New Zealand 144-153.pdf',r'PDF\SINGAPORE..pdf',r'PDF\Singapore 154-170.pdf',r'PDF\SOUTH KOREA..pdf',r'PDF\South Korea 171-177.pdf',r'PDF\SWITZERLAND..pdf',r'PDF\Swizerland 178-193.pdf',r'PDF\U.K..pdf',r'PDF\United Kingdom 194-257.pdf',r'PDF\USA..pdf',r'PDF\USA 258-305.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()