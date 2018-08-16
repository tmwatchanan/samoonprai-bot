from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
# from oauth2client import file, client, tools
from google.oauth2 import service_account
import os.path
from datetime import datetime
import logging

# Logging
logger = logging.getLogger('SAMOONPRAI')

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMOONPRAI_SPREADSHEET_ID = '1R8NU0NDyJFTjz7p18QWYh5pSbAkdJAAtArg_s-Tnaro'
SAMOONPRAI_RANGE_NAME = 'Herb Image URL!A2:C'
SAMOONPRAI_HERB_IMAGE_FEEDBACK_RANGE = 'Herb Image Feedback!A:C'

client_secrets = os.path.join('secrets', 'credentials.json')
service_account_key_file = os.path.join('secrets', 'samoonprai-thai-service-account-key.json')

def read():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # store = file.Storage('token.json')
    # creds = store.get()
    # if not creds or creds.invalid:
        # flow = client.flow_from_clientsecrets(client_secrets, SCOPES)
        # creds = tools.run_flow(flow, store)
    # service = build('sheets', 'v4', http=creds.authorize(Http()))

    credentials = service_account.Credentials.from_service_account_file(service_account_key_file)
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    SPREADSHEET_ID = SAMOONPRAI_SPREADSHEET_ID
    RANGE_NAME = SAMOONPRAI_RANGE_NAME
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[2]))


def append_image_label(file_path, label):
    credentials = service_account.Credentials.from_service_account_file(service_account_key_file)
    service = build('sheets', 'v4', credentials=credentials)

    value_list = [[datetime.utcnow()], [file_path], [label]]

    resource = {
        "majorDimension": "ROWS",
        "values": value_list
    }
    result = service.spreadsheets().values().append(spreadsheetId=SAMOONPRAI_SPREADSHEET_ID,
                                                 range=SAMOONPRAI_HERB_IMAGE_FEEDBACK_RANGE,
                                                    body=resource,
                                                    valueInputOption='USER_ENTERED'
                                                    ).execute()
    logger.debug(result)
