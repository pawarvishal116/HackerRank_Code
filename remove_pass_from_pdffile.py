from getpss import getpass             #Import the getpass() function . Allow the user to enter password without displaying on the screen
from pypdf import PdfReader, PdfWriter #Import two classes from pypdf library. (PdfReader - Read an existing pdf file) . (PdfWriter - Create or write new pdf)

input_pdf = input("Enter the input pdf filename: ")
output_pdf = input("Enter the output pdf filename: ")
password = getpass("Enter the password: ")

reader = PdfReader(input_pdf)    # Create reader object

if reader.is_encrypted:
    result = reader.decrypt(password)
    if result == 0:
        raise ValueError("Incorrect password")

write = PdfWriter()

## Copy all pages

for page in reader.pages:   #Loop through all pages in the original pdf .
    write.add_page(page)    # Adds the current page into the new pdf .


## Save without encryption

with open(output_pdf, "wb") as f:  # open() create a new file. "wb" means write binary . PDF files are binary file
    writer.write(f)

print(f"Unlocked PDF saved as: {output_pdf}")