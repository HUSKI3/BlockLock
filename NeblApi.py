import time
import neblioapi
from neblioapi.rest import ApiException


def run_tests():
    try:
        # Returns address object
        api_response = api_instance.get_address(address)
        print(api_response)
    except ApiException as e:
        print("Exception when calling InsightApi->get_address: %s\n" % e)

class transactionClass:
    def __init__(self,sender,reciever):
        self.sender = "" # address of the sender
        self.reciever = "" # end point of ntp1 token
        api_instance = neblioapi.TestnetInsightApi()
    def send(self,timed=False,time=0,args=None):
        send_tx_request = neblioapi.SendTxRequest()
        try:
            api_response = self.api_instance.send_tx(send_tx_request)
        except ApiException as e:
            api_response = "Failed",e
        return api_response


def create_transaction(sender,reciever):
    transaction = transactionClass(sender,reciever)
    return transaction

def get_balance(address=None,website=False):
    api_instance = neblioapi.TestnetInsightApi()
    if website:
        return api_instance.testnet_get_address("TKXJo16ggP7ENENcqW2qG51XHsKXr5GVPr")
    else:
        if address:
            return api_instance.testnet_get_address(address)
        else:
            return "No address"

def test_transaction():
    return "e"