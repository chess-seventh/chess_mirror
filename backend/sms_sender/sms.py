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

#print '\n'.join(result.readlines())
