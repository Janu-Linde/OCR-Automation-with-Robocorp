from robocorp.tasks import task

from RPA.JSON import JSON
from RPA.Excel.Files import Files


@task
def generate_report():
    create_excel_file()
    

def read_json():
    js = JSON()
    data = js.load_json_from_file("output/data.json")
    
    combined_data = []
    
    for file in data:
        file_data = []
        file_data.append(file["file_name"])
        file_data.append(file["company_reg_number"])
        file_data.append(file["vat_number"])
        combined_data.append(file_data)
    return combined_data


def create_excel_file():
    excel = Files()
    data = read_json()

    excel.create_workbook("output/report.xlsx")

    headers = ["File Name", "VAT Number", "Registration Number"]
    excel.append_rows_to_worksheet([headers], header=False)
    
    for row in data:
        excel.append_rows_to_worksheet([row])

    excel.save_workbook()