import re
def email(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
        emails_html = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html_content)
        return emails_html
html_file = "C:/Users/pilip/PycharmProjects/pythonProject3/xtmls.html"
emails = email(html_file)
print(emails)
