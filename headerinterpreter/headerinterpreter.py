import re
import time
import json

def extract_header_info(header_text):
    headers = {}
    attachment_info = []

    # Regular expressions to extract header information
    header_regex = re.compile(r'^(.*?):\s+(.*?)$', re.MULTILINE)
    attachment_regex = re.compile(r'Content-Type: (.*?);.*?name="(.*?)".*?Content-Disposition: (.*?);.*?filename="(.*?)"', re.DOTALL | re.IGNORECASE)

    # Extract header information
    matches = header_regex.findall(header_text)
    for match in matches:
        key = match[0].strip()
        value = match[1].strip()
        headers[key] = value

    # Extract attachment information, if any
    matches = attachment_regex.findall(header_text)
    for match in matches:
        content_type = match[0].strip()
        name = match[1].strip()
        content_disposition = match[2].strip()
        filename = match[3].strip()
        attachment_info.append((content_type, name, content_disposition, filename))

    return headers, attachment_info

def filter_header_info(headers):
    filtered_headers = {}
    filtered_keys = [
        'Reply-to-display-name', 'Reply-to', 'Subject', 'Bcc', 'To', 'To-display-name', 'Return-path',
        'From-domain', 'From-display-name', 'From', 'Eml', 'Email-body', 'Cc-display-name', 'Cc',
        'Bcc-display-name', 'Thread-index', 'Send-date', 'User-agent', 'Attachment', 'Received-header-ip',
        'Received-header-hostname', 'Mime-boundary', 'Message-id', 'Ip-src', 'Header', 'X-mailer'
    ]
    for key in filtered_keys:
        if key in headers:
            filtered_headers[key] = headers[key]
    return filtered_headers

def save_info_to_file(headers, attachment_info, output_file, output_format):
    if output_format == 'txt':
        output_file += '.txt'
        with open(output_file, 'w') as file:
            # Write header information to the output file
            file.write('From: {}\n'.format(headers.get('From', '')))
            file.write('To: {}\n'.format(headers.get('To', '')))
            file.write('Subject: {}\n'.format(headers.get('Subject', '')))
            file.write('Date: {}\n'.format(headers.get('Date', '')))
            file.write('Message-ID: {}\n'.format(headers.get('Message-ID', '')))
            file.write('Return-Path: {}\n'.format(headers.get('Return-Path', '')))
            file.write('X-Sender-IP: {}\n'.format(headers.get('X-Sender-IP', '')))

            # Write attachment information to the output file
            if attachment_info:
                file.write('\nAttachment information:\n')
                for attachment in attachment_info:
                    file.write('Content-Type: {}\n'.format(attachment[0]))
                    file.write('Name: {}\n'.format(attachment[1]))
                    file.write('Content-Disposition: {}\n'.format(attachment[2]))
                    file.write('Filename: {}\n'.format(attachment[3]))
                    file.write('\n')

    elif output_format == 'json':
        output_file += '.json'
        filtered_headers = filter_header_info(headers)
        output_data = {
            'headers': filtered_headers,
            'attachments': attachment_info
        }
        with open(output_file, 'w') as file:
            json.dump(output_data, file, indent=4)

    print('The information has been saved to the file "{}".'.format(output_file))
    print('Interpretation completed.')

def main():
    print('''
  _    _                   _               _         _                                 _               
 | |  | |                 | |             (_)       | |                               | |              
 | |__| |  ___   __ _   __| |  ___  _ __   _  _ __  | |_  ___  _ __  _ __   _ __  ___ | |_  ___  _ __  
 |  __  | / _ \ / _` | / _` | / _ \| '__| | || '_ \ | __|/ _ \| '__|| '_ \ | '__|/ _ \| __|/ _ \| '__| 
 | |  | ||  __/| (_| || (_| ||  __/| |    | || | | || |_|  __/| |   | |_) || |  |  __/| |_|  __/| |    
 |_|  |_| \___| \__,_| \__,_| \___||_|    |_||_| |_| \__|\___||_|   | .__/ |_|   \___| \__|\___||_|    
                                                                    | |                                
                                                                    |_|                                
    HEADER INTERPRETER by: Caique Barqueta
    ''')

    while True:
        try:
            input_file = input('Enter the path to the email header file (.txt): ')
            with open(input_file, 'r') as file:
                header_text = file.read()
            break
        except FileNotFoundError:
            print('File not found. Please enter a valid file path.')

    output_file = input('Enter the path to the output file: ')
    output_format = input('Enter the output file format (txt or json): ').lower()

    while output_format not in ['txt', 'json']:
        output_format = input('Invalid format. Please enter txt or json: ').lower()

    headers, attachment_info = extract_header_info(header_text)
    save_info_to_file(headers, attachment_info, output_file, output_format)
    
    time.sleep(2)  # Delay for 2 seconds

if __name__ == '__main__':
    main()
