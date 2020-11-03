import time
import neblioapi
from neblioapi.rest import ApiException


# create an instance of the API class
api_instance = neblioapi.InsightApi(neblioapi.ApiClient(configuration))
address = '' # str | Address

try:
    # Returns address object
    api_response = api_instance.get_address(address)
    print(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address: %s\n" % e)