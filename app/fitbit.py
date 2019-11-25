# import fitbit
# import app.gather_keys_oauth2 as auth2
# import datetime
#
# CLIENT_ID='22BFHK'
# CLIENT_SECRET='92af1fb017e08d1b4426a5e092257e85'
#
# server = auth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
# server.browser_authorize()
#
# ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
# REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
# auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN,
#                              refresh_token=REFRESH_TOKEN)

from app import fitbit
import app.send_survey as send_survey
import importlib

data = fitbit.time_series(resource='activities/heart')

if data > 100:
    importlib.import_module(send_survey)

