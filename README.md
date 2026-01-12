# OCR Automation Project
This automation project helps companies save costs by verifying whether their vendors are VAT-compliant. The system extracts text from invoice images to identify valid company registration numbers. These details can then be matched against a master vendor database to confirm VAT registration status.

In a South African context, the goal would be to ensure that the company works with VAT-registered vendors, enabling it to claim back input VAT from SARS on qualifying purchases.
## Setup
*Note: This project is set up to run on Windows. It might be possible to run this project on Linux or Mac, but this README does not provide a guide to installation/setup for those operating systems.*

1. Install the Sema4.ai SDK extension for VS Code.
   
2. Install Tesseract on your local machine.
   - Use the Windows installer to install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
   - Note that you will need both the Tesseract engine and Tesseract package.
   ```
   pip install pytesseract # install package
   ```
4. Install other pip packages
   - **Package names:** *pillow, robocorp-tasks, rpaframework.*
 ```
 pip install "package name"
 ```

## Run in VS Code
To run the project, there are two parts you need to run. 
1. First run the "Get Invoice Data" task.
2. Then run the "Generate Excel" task.

<img src="https://github.com/InnoJanu/OCR-Automation-with-Robocorp/blob/main/README%20Images/run_in_vs_code.jpg?raw=true"
     alt="Run in VS Code Image"
     width="40%" />

# How the automation works
![image alt]([https://github.com/InnoJanu/OCR-Automation-with-Robocorp/blob/main/README%20Images/run_in_vs_code.jpg?raw=true](https://github.com/Janu-Linde/OCR-Automation-with-Robocorp/blob/main/README%20Images/how_it_works%20v2.jpg?raw=true))

Potential additions to project:
+ *Add a bot that retrieves invoices and puts them into a directory.*
+ *Post Excel data back to master database.*


