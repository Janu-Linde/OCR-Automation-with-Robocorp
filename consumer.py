from robocorp.tasks import task
from robocorp import workitems
from RPA.JSON import JSON
from RPA.Excel.Files import Files


@task
def generate_report():
    process_traffic_data()

def process_traffic_data():
    for item in workitems.inputs:
        traffic_data = item.payload["traffic_data"]
        name = traffic_data["file_name"]
        vat = traffic_data["vat_number"]
        reg = traffic_data["registration_number"]

        if invalid(vat) or invalid(reg):
            item.fail()
        else:
            write_to_excel(name, vat, reg)
            item.done()


def invalid(number):
    if number == "No-match-found":
        return True
    else:
        return False


def write_to_excel(file_name, vat_num, reg_num):
    excel = Files()
    
    try:
        excel.open_workbook("output/report.xlsx")
        excel.append_rows_to_worksheet([[file_name, vat_num, reg_num]], header=False)
        excel.save_workbook()

    except FileNotFoundError:
        excel.create_workbook("output/report.xlsx")
        headers = ["File Name", "VAT Number", "Registration Number"]
        excel.append_rows_to_worksheet([headers], header=False)
        excel.append_rows_to_worksheet([[file_name, vat_num, reg_num]], header=False)
        excel.save_workbook()