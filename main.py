from bs4 import BeautifulSoup
import re
import requests
urls = ["https://webbullindia.com/",
        "https://devobyte.com/",
        "https://digitalnotebook.in",
        "https://www.doorsstudio.com/digital/",
        "https://cxr.agency/",
        'https://www.brightedge.com/',
        'https://seovalley.com/',
        'https://www.digitalsilk.com/',
        'https://www.luminary.com/' ]

def fetch_and_save_to_file(url, path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    with open(path, "w") as f:
        f.write(response.text)

i=1
for url in urls:
    fetch_and_save_to_file(url, f'data/sitedata{i + 1}.html')

    with open(f'data/sitedata{i+1}.html', 'r') as f:
        html_doc = f.read()

    pattern = re.compile(r"^tel:|\+91")
    soup = BeautifulSoup(html_doc, 'html.parser')
    for a in soup.find_all('a', href=pattern):
        print(url)
        print('phone_number',a['href'].strip())
        print('\n')
