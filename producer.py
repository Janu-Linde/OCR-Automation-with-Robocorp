from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# from robocorp import workitems
from robocorp.tasks import task
from RPA.FileSystem import FileSystem
import validation

@task
def minimal_task():
    fs = FileSystem()
    image_directory = fs.list_files_in_directory(r"invoices")

    global combined_invoice_data
    combined_invoice_data = []

    for path in image_directory:
        file_name = fs.get_file_name(path)
        image = prep_image(path)
        text = get_text(image)
        return_invoice_results(text, file_name)

    print(combined_invoice_data)
        

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
    return text


def return_invoice_results(text, name):
    
    vat_num = validation.check_vat(text)
    registration_num = validation.check_registration(text)

    invoice_results = dict(file_name=f"{name}",
                        vat_Number=f"{vat_num}",
                        registration_Number=f"{registration_num}")
    
    combined_invoice_data.append(invoice_results)