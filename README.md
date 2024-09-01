# FunLocker
#### Written by: Toughrebel4041

## Overview
FunLocker is a password-locked file decryptor (so far only have .docx and .pdf file decryptors). FunLocker uses a set of base passwords provided by the user to attempt to unlock encrypted files. The program will generate various combinations of these passwords to maximize the chances of successfully decrypting the file. This is useful if you have a list of possible passwords that you commonly use and need to recover access to a file that has been encrypted with one of these passwords.

This repository contains two tools for decrypting password-protected files:
1. `decryptWord.py` - A tool to unlock encrypted Word documents.
2. `decryptPDF.py` - A tool to unlock encrypted PDF files.

## Prerequisites
Before using these tools, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

### Dependencies
You need to install the required Python libraries. You can do this using the provided `requirements.txt` file.

1. Clone this repository:
   ```
   git clone https://github.com/Toughrebel4041/FunLocker
   cd FunLocker
   ```
   
2. Install the dependencies for Word and PDF decryption:

```bash
pip install -r requirements.txt
```

The requirements.txt file should include:
```bash
msoffcrypto-tool
pikepdf
scapy
```

## Usage
### decryptWord.py
This script attempts to unlock an encrypted Word document using a list of base passwords.

Ensure you have msoffcrypto-tool installed (it will be installed with requirements.txt).

Run the script and follow the prompts:

```bash
python decryptWord.py

Enter your base passwords separated by commas (e.g., password1,password2)
Enter the name of the .docx file to decrypt (e.g., File.docx)
Enter the desired name for the output file (e.g., Decrypted_File.docx)
```

### decryptPDF.py
This script attempts to unlock an encrypted PDF file using a list of base passwords.

Ensure you have pikepdf installed (it will be installed with requirements.txt).

Run the script and follow the prompts:

```bash
python decryptPDF.py

Enter your base passwords separated by commas (e.g., password1,password2)
Enter the name of the PDF file to decrypt (e.g., File.pdf)
Enter the desired name for the output file (e.g., Decrypted_File.pdf)
```

### Notice: You might want to place the pdf or docx file on the same directory as the decryptor

## License
This project is licensed under the MIT License - see the [LICENSE](https://www.github.com/Toughrebel4041/FunLocker/LICENSE) file for details.
```bash
This expanded description provides a comprehensive overview of the FunLocker project, detailing its functionality, installation instructions, and usage.
```
