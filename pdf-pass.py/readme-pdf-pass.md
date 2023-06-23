Brazilian and other countries' phishing files are presenting passwords so that they can be difficult to identify for analysis, acting as a form of defense evasion.

Therefore, it is possible to decrypt the file without executing it, using the python script "pdf-pass.py", changing the information inside the file, defining the storage location, eviction and password used.

Remembering that the script does not brute force the pdf.

After decrypting the data, the PDF will present a HASH different from the original one, since the content inside the file has been modified so that it can be analyzed with other tools, such as: pdfid.py, pdf-parser.py...

Example:
YwmPFaJ7lkuq.pdf (md5: F2CD59643FB4FAFEC66F50833F637C48) converted to file without password: file_without_password.pdf (md5 312B625A05096803EDBCDCC5C5EF8C52 ).
