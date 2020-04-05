# contact_project
A tool for creating .vcf files from pictures of business cards using azure.

This program takes an image of an input, an azure password, an email password.

The getText function takes a file path to an image and uses the OCR API from Microsoft Azure to extract text.
    The document also requires azure keys in a json file that is not available in this repo.
The array of text and bounding boxes that are given from the OCR algorithm are stored in a csv file in writeArrayCSV
to allow visualization of the text and returned data without using the API as often.
The createVCF function parses this csv. Using a list of names and regular expressions, it determines names, email, 
and a telephone number. This information is assembled into a vcf file.
sendAttachedEmail then emails the attachment to a specified address. There is in input for a password to limit use of
the current email. The current implementation doesn't seem to work well with sending to mobile numbers.
A main function compiles all these functions together to send a contact file based on information from business_card6.jpg
to the output email.
