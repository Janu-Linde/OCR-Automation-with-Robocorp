from datetime import date

# This script provides function that validate South African VAT and company registration numbers

def validate_company_number(numbers):
    def check_year(num):
        this_year = date.today().year
        if len(num) == 12:
            year = int(num[:4])
            return 1900 <= year <= this_year
        return False

    def check_entity(num):
        entity_codes = ["06", "07", "08", "21", "23", "30"]
        return num[-2:] in entity_codes

    for element in numbers:
        if check_year(element) and check_entity(element):
            return add_slahses(element)
    return "No match found"
    
def validate_vat_number(list):
    for element in list:
        if len(element) == 10 and element.startswith("4"):
            return element
    return "No match found"

def add_slahses(number):
    number = number[:4] + "/" + number[4:10] + "/" + number[-2:]
    return number