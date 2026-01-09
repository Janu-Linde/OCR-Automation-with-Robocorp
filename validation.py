# This script provides funcitonality to validate South African VAT numbers and company registration numbers.
# Data format: ['solutions', '2021/087654/07', '4123456789', 'architect']

# Number Examples 
# Company Registration Number: ["2021/123456/07"]
# VAT Number: ["4987654321"]


def check_registration(items):
    for item in items:
        if (
            len(item) == 14
            and int(item[:4]) < 2027
            and int(item[:4]) > 1899
        ):
            return item
        
    return "No-match-found"


def check_vat(items):
    for item in items:
        if (
            len(item) == 10
            and int(item[0]) == 4
        ):
            return item
    return "No-match-found"