"""
to send an sms to friends
"""
import urllib.request as U
from sms_constants import SMS_BASE_URL
from sms_constants import SMS_ME
from sms_constants import SMS_USER_API
from sms_constants import MY_MSG

class SMS(object):
    """docstring for SMS"""
    def __init__(self, sms_to=SMS_ME, sms_msg=MY_MSG):
        self.phone = 'tel:' + sms_to
        self.msg = sms_msg
        self.mydata = {}
        self.myurl = SMS_BASE_URL
        self.req = U.Request(SMS_BASE_URL)
        self.req.add_header('Content-Type', 'application/json')
        self.req.add_header('client_id', SMS_USER_API)
        self.req.add_header('SCS-Version', '1')


    def my_add_data(self):
        """what to send"""
        self.mydata = {
                'outboundSMSMessageRequest': {
                    'address':[self.phone],
                    'outboundSMSTextMessage': {
                        'message':MY_MSG
                        }
                    }
                }


        def my_send(self):
            """send the shit over here"""
        U.urlopen(self.req, self.mydata)


def main():
    """ main function """
    sms = SMS()
    sms.my_add_data()
    sms.my_send()

    #print(sms.myurl)
    #print(sms.phone)
    #print(sms.req)
    #print(sms.msg)


if __name__ == '__main__':
    main()
