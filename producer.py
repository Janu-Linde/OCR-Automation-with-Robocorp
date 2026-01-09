import json

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# from robocorp import workitems
from robocorp.tasks import task
from RPA.FileSystem import FileSystem
import validation

# pytesseract.pytesseract.tesseract_cmd = r"C:\My Program Files\Tesseract\tesseract.exe"

@task
def minimal_task():
    fs = FileSystem()
    directory = r"invoices"
    image_directory = fs.list_files_in_directory(directory)

    combined_data = []
    

    # if not fs.does_file_exist("output/data.json"):
    #     with open("output/data.json", "w") as f:
    #         pass

    for path in image_directory:
        file_name = fs.get_file_name(path)

        image = prep_image(path)
        text = get_text(image)
        comp_reg = validation.validate_company_number(text)
        vat_num = validation.validate_vat_number(text)
        
        data = dict(
            file_name=f"{file_name}",
            company_reg_number=f"{comp_reg}",
            vat_number=f"{vat_num}"   
        )

        combined_data.append(data)
        
    with open("output/data.json", "w") as f:
        json.dump(combined_data, f, indent=4)


def prep_image(image_path):
    image = Image.open(image_path)
    image = image.convert("L") 
    image = image.filter(ImageFilter.SHARPEN)
    image = ImageEnhance.Contrast(image).enhance(2)
    image = image.resize((image.width * 2, image.height * 2))
    
    return image


def get_text(image):
    text = pytesseract.image_to_string(image)
    text = text.split()
    text = [digits_only(word) for word in text]
    return text


def digits_only(number):
    cleaned = "".join(character for character in number if character.isdigit())
    return cleaned