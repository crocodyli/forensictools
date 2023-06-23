import PyPDF2

#Meta: 
#Author-Caique Barqueta
#Twitter: https://twitter.com/crocodylii 

def remove_pdf_password(input_file, output_file, password):
    with open(input_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if reader.is_encrypted:
            reader.decrypt(password)

        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_file, 'wb') as output:
            writer.write(output)

# Usage example
input_file = 'input.pdf'  # Replace with the path to your input PDF file
output_file = 'output_no_password.pdf'  # Replace with the desired path for the output PDF file (without password)
password = 'your_password'  # Replace with the correct password

remove_pdf_password(input_file, output_file, password)
