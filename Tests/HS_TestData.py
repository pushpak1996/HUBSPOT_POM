import xlrd
import os

class TestData():

    wb = xlrd.open_workbook('../Test_Data/HS_Test_data.xlsx')

    contact_data = wb.sheet_by_name('contact_data')
    ticket_data = wb.sheet_by_name('ticket_data')
    deal_data = wb.sheet_by_name('deal_data')
    snippet_data = wb.sheet_by_name('snippet_data')
    company_data = wb.sheet_by_name('company_data')
    task_data = wb.sheet_by_name('task_data')
    template_data = wb.sheet_by_name('template_data')

    rel_path = "../Test_Data/HS_Test_data.xlsx"
    abs_path = os.path.abspath(rel_path)
    file = rel_path.split("/")
    verifyfile = file[2]