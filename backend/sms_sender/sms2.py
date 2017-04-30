import urllib3
import json

data = {
        'outboundSMSMessageRequest': {
            'address':['tel:+41798300270'],
            'outboundSMSTextMessage': {
                'message':'ZeBoss'
                }
            }
        }

req = urllib2.Request('https://api.swisscom.com/v1/messaging/sms/outbound/tel%3A%41798300270/requests')
req.add_header('Content-Type', 'application/json')
req.add_header('client_id', 'SMS_CLIENT_API')

result = urllib2.urlopen(req, json.dumps(data))

#print '\n'.join(result.readlines())

"""


import urllib3
import json

data = {
        "from":"MY_PHONE",
        "to":"MY_PHONE",
        "body":"Hello world:-)"
        }

req = urllib2.Request('https://api.swisscom.com/messaging/sms')
req.add_header('Content-Type', 'application/json; charset=utf-8')
req.add_header('client_id', 'MY_API')

result = urllib2.urlopen(req, json.dumps(data))

print '\n'.join(result.readlines())

"""
