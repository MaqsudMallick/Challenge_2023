import xlwt

def createXL(titles, dates, imgs, likes):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("sheet 1")
    sheet.write(0, 0, "Title")
    sheet.write(0, 1, "Date")
    sheet.write(0, 2, "Likes")
    sheet.write(0, 3, "Image")
    for i in range(1, len(titles)+1):
        sheet.write(i, 0, titles[i-1])
    for i in range(1, len(dates)+1):
        sheet.write(i, 1, dates[i-1])
    for i in range(1, len(likes)+1):
        sheet.write(i, 2, likes[i-1])
    for i in range(1, len(imgs)+1):
        sheet.write(i, 3, imgs[i-1])
    workbook.save("output.xls") 






