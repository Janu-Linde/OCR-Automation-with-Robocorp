# OCR Automation Project
This automation project helps companies save costs by verifying whether their vendors are VAT-compliant. The system extracts text from invoice images to identify valid company registration numbers. These details can then be matched against a master vendor database to confirm VAT registration status.

In a South African context, the goal would be to ensure that the company works with VAT-registered vendors, enabling it to claim back input VAT from SARS on qualifying purchases.
## Setup
*Note: This project is set up to run on Windows. It might be possible to run this project on Linux or Mac, but this README does not provide a guide to installation/setup for those operating systems.*

1. Install the Sema4.ai SDK extension for VS Code.
   
2. Install Tesseract on your local machine.
   - Use the Windows installer to install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
   - Note that you will need both the Tesseract engine and Tesseract package.
   
4. Install pip packages
   - **Package names:** *pillow, pytesseract, robocorp-tasks, rpaframework.*
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

# Potential expansion to the project
This project serves as a segment of a larger project. There is still potential to add automation before and after this process. The architecture of the system may change to complement other systems better. This is simply an idea of how a system like this can work.

The section highlighted in green shows where this project fits into the larger scope of potential expansion to the project.

Potential additions to project:
+ *Add a bot that retrieves invoices and puts them into a directory.*
+ *Add a bot that sends the data back to the master database and verifies with existing vendors.*

![image alt](https://github.com/InnoJanu/OCR-Automation-with-Robocorp/blob/main/README%20Images/project_overview.jpg?raw=true)
