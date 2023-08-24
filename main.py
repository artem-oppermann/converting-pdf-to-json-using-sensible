import json
import requests
from pathlib import Path

# The name of a document type in Sensible, such as "tax_document"
DOCUMENT_TYPE = "tax_document"
# The path to the PDF you'd like to extract from
DOCUMENT_PATH = Path("1040_2020.pdf")
# The path to save the output
OUTPUT_PATH = Path("response.json")
# The path to save the exception (if occurs)
ERROR_PATH = Path("exception.json")

# Your Sensible API key
SENSIBLE_API_KEY = "YOUR SENSIBLE API KEY"

URL = "https://api.sensible.so/v0/extract/{}?environment=development".format(DOCUMENT_TYPE)

headers = {
        'Authorization': 'Bearer {}'.format(SENSIBLE_API_KEY),
        'Content-Type': 'application/pdf'
    }

def api_call():
    
    with DOCUMENT_PATH.open('rb') as pdf_file:
        body = pdf_file.read()
        response = requests.request(
            "POST",
            URL,
            headers=headers,
            data=body
        )
    return response 
    
def extract_doc():

    response = api_call()
    
    try:
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
        
        with ERROR_PATH.open('w') as error_file:
           error_file.write(str(e))
    else:
        response_json = response.json()
        
        # Access the name in the parsed PDF
        print("Name: %s" %(response_json['parsed_document']['name']['value']))
        # Access the ssn in the parsed PDF
        print("SSN: %s" %(response_json['parsed_document']['ssn']['value']))
        # Access the adress in the parsed PDF
        print("Adress: %s" %(response_json['parsed_document']['home_street_address']['value']))
        
        # Save the JSON output for further analysis
        with OUTPUT_PATH.open('w') as json_file:
            json.dump(response_json, json_file, indent=2)


if __name__ == '__main__':
    extract_doc()

