# Include the SendinBlue library\
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
# sib_api_v3_sdk.configuration.api_key_prefix['api-key'] = 'Bearer'

api_instance = sib_api_v3_sdk.EmailCampaignsApi()

# Define the campaign settings\
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
    name= "Livre d'Or",
    subject= "",
    sender= { "name": "From name", "email": "paulo.najib@gmail.com"},
    type= "classic",

    # Content that will be sent\
    html_content= "Congratulations! You successfully sent this example campaign via the SendinBlue API.",

    # Select the recipients\
    recipients= {"listIds": [2, 7]},

    # Schedule the sending in one hour\
    scheduled_at= "2018-01-01 00:00:01"
)

# Make the call to the client\
try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    print(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)
