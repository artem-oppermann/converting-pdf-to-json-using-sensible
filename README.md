# Easily Converting PDF to JSON

The Python code main.py uses the Sensible API to extract data from a PDF document. The PDF document is assumed to be of type "tax_forms_1040_2018" or any other name you have used when creating the document type in the Sensible web application. The extracted data from this document will be returned in a JSON format.

The code begins by importing the necessary modules, `json` and `requests`. It then defines three variables: `DOCUMENT_TYPE`, `DOCUMENT_PATH`, and `API_KEY`

- `DOCUMENT_TYPE` is the type of document to extract data from, in this case "tax_forms_1040_2018".
- `DOCUMENT_PATH` specifies the file path to the local PDF document on your computer that you'll extract data from and convert to JSON format.
- `API_KEY` is your unique Sensible API key used for authentication.

The `extract_doc() ` function is then defined. This function sets the headers and reads the PDF document from `DOCUMENT_PATH ` using a context manager. It then sends a `POST` request to the Sensible API endpoint using the `requests` module. In this step all data from the PDF is extracted according to the previously defined JSON config. The extracted data from the PDF is returned in a JSON format as a response. This response is checked for errors, and if there are no errors, the extracted data is printed using the `json` module. 

Finally, the script checks if the script is being run as the main module `(__name__ == '__main__')` and if it is, it calls the `extract_doc()` function. This ensures that the function is only called when the script is run as a standalone program and not when it's imported as a module.

To run the code, be sure to specify your API key, the local path to your PDF, and the name of the doc type that you created in the Sensible web application. You can execute the file either in a console or in an IDE like [Spyder](https://www.spyder-ide.org/) or [PyCharm](https://www.jetbrains.com/de-de/pycharm/). 

After executing the application, you should receive the following output:

```
{
  "id": "c8478973-02d9-4f2c-9eae-d3d7c3442d67",
  "created": "2023-03-01T17:08:35.529Z",
  "completed": "2023-03-01T17:08:50.172Z",
  "status": "COMPLETE",
  "type": "tax_forms_1040_2018",
  "configuration": "tax_form_1",
  "environment": "production",
  "parsed_document": {
    "Year": {
      "type": "string",
      "value": "2018"
    },
    "filing_status.single": {
      "type": "boolean",
      "value": false
    },
    "filing_status.married_filing_jointly": {
      "type": "boolean",
      "value": false
    },
    "filing_status.married_filing_separately": {
      "type": "boolean",
      "value": false
    },
    "filing_status.head_of_household": {
      "type": "boolean",
      "value": true
    },
    "filing_status.qualifying_widow": {
      "type": "boolean",
      "value": false
    },
    "name": {
      "type": "string",
      "value": "Gemanna Gomez"
    },
    "ssn": {
      "type": "string",
      "value": "111-22-3333"
    },
    "spouse_name": null,
    "spouse_ssn": null,
    "home_street_address": {
      "type": "string",
      "value": "13434 Doe Street"
    },
    "home_apartment_number": null,
    "home_city_state_zipcode": {
      "type": "string",
      "value": "San Francisco CA 92694"
    },
    "wages_salaries_tips": null,
    "tax_exempt_interest": null,
    "taxable_interest": null,
    "qualified_dividends": null,
    "ordinary_dividends": null,
    "ira_distributions": null,
    "ira_distributions_taxable_amount": null,
    "pensions_and_annuities": null,
    "pensions_and_annuities_taxable_amount": null,
    "social_security_benefits": null,
    "social_security_benefits_taxable_amount": null,
    "capital_gain_or_loss": null,
    "other_income": null,
    "total_income": null,
    "adjustments_to_income": null,
    "adjusted_gross_income": {
      "source": "74,944",
      "value": 74944,
      "type": "number"
    },
    "standard_deduction": {
      "source": "20,398",
      "value": 20398,
      "type": "number"
    },
    "qualified_business_deduction": {
      "source": "8,532",
      "value": 8532,
      "type": "number"
    },
    "taxable_income": {
      "source": "46,014",
      "value": 46014,
      "type": "number"
    },
    "tax": {
      "source": "5,251",
      "value": 5251,
      "type": "number"
    },
    "child_tax_credit": {
      "source": "2,000",
      "value": 2000,
      "type": "number"
    },
    "other_tax_including_self_employment": null,
    "total_tax": {
      "source": "6,635",
      "value": 6635,
      "type": "number"
    },
    "federal_income_tax_withheld": {
      "source": "4,972",
      "value": 4972,
      "type": "number"
    },
    "earned_income_credit": null,
    "additional_child_tax_credit": null,
    "american_opportunity_credit": null,
    "total_other_payments": null,
    "total_payments": {
      "source": "4,972",
      "value": 4972,
      "type": "number"
    },
    "overpaid_amount": null,
    "overpaid_refund_amount": null,
    "routing_number": {
      "type": "string",
      "value": "u"
    },
    "account_type.checking": {
      "type": "boolean",
      "value": false
    },
    "account_type.savings": {
      "type": "boolean",
      "value": false
    },
    "account_number": null,
    "amount_you_owe": {
      "source": "1,663",
      "value": 1663,
      "type": "number"
    },
    "estimated_tax_penalty": null,
    "signed": {
      "type": "boolean",
      "value": false
    },
    "signed_date": null,
    "spouse_signed": {
      "type": "boolean",
      "value": false
    },
    "spouse_signed_date": null
  },
  "validations": [],
  "validation_summary": {
    "fields": 54,
    "fields_present": 25,
    "errors": 0,
    "warnings": 0,
    "skipped": 0
  },
  "classification_summary": [
    {
      "configuration": "tax_form_1",
      "fingerprints": 5,
      "fingerprints_present": 5,
      "score": {
        "value": 25,
        "fields_present": 25,
        "penalties": 0
      }
    }
  ],
  "errors": [],
  "file_metadata": {
    "info": {
      "modification_date": "2022-06-16T11:25:28.000-04:00"
    }
  }
}
```
