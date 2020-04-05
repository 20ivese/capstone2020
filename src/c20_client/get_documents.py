"""
Contains class used to retreive documents from regulations.gov
"""
import requests
from c20_client.status_code_check import check_status


def get_documents_data(api_key, offset, date):
    """
    Makes call to regulations.gov and retrieves the documents data
    """
    response = requests.get('https://api.data.gov:443/regulations' +
                            '/v3/documents.json?api_key=' + api_key +
                            '&po=' + str(offset) + '&crd=' + date)

    check_status(response.status_code)

    return response.json()


def get_documents(api_key, offset, start_date, end_date):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    date = start_date + '-' + end_date
    return get_documents_data(api_key, offset, date)
