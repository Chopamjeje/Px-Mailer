Email Automation
This is a Python script for automating the sending of emails with various purposes such as sending orders, requesting quotations, checking mailbox quota, and more.

Getting Started
These instructions will get you a copy of the project up and running on your local machine.

Prerequisites
Python 3
Internet connection
Installing
Clone the repository using git:

bash
Copy code
git clone https://github.com/prixzlex/Px-Mailer.git
Or download the repository as a ZIP file and extract it to your preferred directory.

Install the required packages using setup file:

Copy code
python3 setup.py
Usage
To use the script, simply run the "pxmailer" commmand on your terminal and follow the prompts.

Features
Order generation: generates an HTML email message with a link to the order files and sends it to the recipient's email address.
Quotation request: generates an HTML email message requesting a quotation and sends it to the recipient's email address.
Mailbox quota check: generates an HTML email message requesting the recipient to check their mailbox quota and sends it to the recipient's email address.
Payment request: generates an HTML email message requesting payment for a completed order and sends it to the recipient's email address.
Big file reminder: generates an HTML email message reminding the recipient to upload a big file before its expiration date and sends it to the recipient's email address.
LinkedIn message: generates a subject line for a LinkedIn message with various options such as business, urgent, invitation, request, new, and fresh.
Purchase order subject: generates a subject line for a purchase order with various options such as invoice, order, information, please review, kind...
Customization
You can customize the email messages and subject lines by editing the users fm.txt file.

Contributing
Contributions are welcome. Please fork the repository and submit a pull request.

Authors
Your Name - Prixzlex
License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Acknowledgments
OpenAI for providing the GPT-3.5 architecture used to train the ChatGPT language model.
Base64 for providing a way to encode and decode email addresses.
Random for providing a way to generate random values in Python.
