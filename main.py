import json
import requests


# The name of a document type in Sensible, e.g., "tax_forms_1040_2018"
DOCUMENT_TYPE = "tax_forms_1040_2018"
# The path to the PDF you'd like to extract from
DOCUMENT_PATH = "PATH/TO/PDF/1040_2018_sample.pdf"
# Your Sensible API key
API_KEY = "YOUR API KEY"


def extract_doc():
    headers = {
        'Authorization': 'Bearer {}'.format(API_KEY),
        'Content-Type': 'application/pdf'
    }
    with open(DOCUMENT_PATH, 'rb') as pdf_file:
        body = pdf_file.read()
        response = requests.request(
        "POST",
        "https://api.sensible.so/v0/extract/{}?environment=development".format(DOCUMENT_TYPE),
        headers=headers,
        data=body)
    try:
        response.raise_for_status()
    except requests.RequestException:
        print(response.text)
    else:
        print(json.dumps(response.json(), indent=2))


if __name__ == '__main__':
    extract_doc()
