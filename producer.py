from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from robocorp.tasks import task
from robocorp import workitems
from RPA.FileSystem import FileSystem

import validation

@task
def minimal_task():
    fs = FileSystem()
    image_directory = fs.list_files_in_directory(r"C:\Users\janul\Downloads\invoices")

    text = get_text(image_directory)
    payloads = get_payloads(text, image_directory)
    save_workitems(payloads)


def get_text(image_directory):
    image_data = []

    for i in image_directory:
        # Prep the image for OCR extraction
        image = Image.open(i)
        image = image.convert("L") 
        image = image.filter(ImageFilter.SHARPEN)
        image = ImageEnhance.Contrast(image).enhance(2)
        image = image.resize((image.width * 2, image.height * 2))
        # Get text from images
        text = pytesseract.image_to_string(image)
        text = text.split()
        image_data.append(text)

    return image_data


def get_payloads(data_set, directory):
    # Prep data for workitems
    # Get image information
    fs = FileSystem()
    payloads = []

    for set, image in zip(data_set, 
                          directory):

        file_name = fs.get_file_name(image)
        vat_num = validation.check_vat(set)
        registration_num = validation.check_registration(set)

        payload = dict(file_name=f"{file_name}",
                        vat_number=f"{vat_num}",
                        registration_number=f"{registration_num}")
        payloads.append(payload)

    return payloads


def save_workitems(payloads):
    for payload in payloads:
        variables = dict(traffic_data=payload)
        workitems.outputs.create(variables)