from django.http import HttpResponse
from openpyxl import load_workbook

def read_excel_file(path):
    wb = load_workbook(filename=path, rich_text=True, read_only=True )
    sheet = wb.active
    headers = [cell.value for cell in table_range[0]]

    # for row in sheet.iter_rows(values_only=True):
    #     print(row)
    #     break
    return headers

def convert_excel_to_json():
    pass

def document_view(url):
    data = read_excel_file(url)
    return HttpResponse(f"Hello Geeks {data}")