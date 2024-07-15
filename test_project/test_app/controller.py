from django.http import HttpResponse
from openpyxl import load_workbook

def read_excel_file(path):
    wb = load_workbook(filename=path, rich_text=True, read_only=True )
    sheet = wb.active


    headers = []
    for cell in sheet[1]:
        val = cell.value if cell.value is not None else ''
        headers.append(str(val))

    data_list = []
    for row in sheet.iter_rows(min_row=2, max_row=10): #strating from second row as 1st row is header
        row_val= []
        for cell in row:
            print(cell.value)
            val = cell.value if cell.value is not None else ''
            row_val.append(str(val))
        data_list.append(row_val)
    
    data_dict = {}
    data_dict['headers'] = headers
    data_dict['value'] = data_list

    return data_dict

def convert_excel_to_json():
    pass

def document_view(url):
    data = read_excel_file(url)
    # return HttpResponse(f"Hello Geeks {data}")
    print(data)


exel_file_path = './static/the-office-lines.xlsx'
document_view(exel_file_path)