from __future__ import print_function
#Import libraries for Python Website Monitoring project
import urllib.request
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.models.send_smtp_email_sender import SendSmtpEmailSender
from sib_api_v3_sdk.models.send_smtp_email_to import SendSmtpEmailTo
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from decouple import config


# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = config('SENDBLUE_API_SECRET')
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key


# create an instance of the API class
api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))
# create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(sender=SendSmtpEmailSender(email="team@allmediterranean.com"), to=[SendSmtpEmailTo(email="team@allmediterranean.com")], html_content="Website is down", text_content="Website is down",  subject="Website is down") # SendSmtpEmail | Values to send a transactional email
#    def __init__(self, sender=None, to=None, bcc=None, cc=None, html_content=None, text_content=None, subject=None, reply_to=None, attachment=None, headers=None, template_id=None, params=None, message_versions=None, tags=None, scheduled_at=None, batch_id=None):  # noqa: E501

try:
    # Send a transactional email
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)

#Monitor the website
def monitor_website(event, context):
       #Visit the website to know if it is up
       input_website = "https://allmediterranean.com"
       status = urllib.request.urlopen(input_website).getcode()
       #If it returns 200, the website is up
       if status != 200:
            #Call email function
            print("The website is down")



       else:
            print("The website is up")
            #Open url and create the hash code


  
monitor_website(1, 1)