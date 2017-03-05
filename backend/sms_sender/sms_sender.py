

class SMS(object):
  """docstring for SMS"""
    def __init__(self, arg):
        self.arg = arg

    def connect(self):
        pass
    def send(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()


# python 2

import urllib2, json

#__FRA = "+41798300270"


data = {
  "from" : "+41798300270",
  "to" : "+41798300270",
  "text" : "Who is the boss"
  }

"""
data = {
            "from": __ME,
            "to": __ABE,
            "body":"Hello world"
       }

"""

req = urllib2.Request('https://api.swisscom.com/messaging/v1/sms/')

header = {'SCS-Version':'1', 'Content-Type':'application/json; charset=utf-8', 'apikey':'gU0UNSLgwOj69HZOmQ0XSuUKyxNc2CZU'}

req.add_header('SCS-Version', '1')
req.add_header('Content-Type', 'application/json; charset=utf-8')
req.add_header('apikey', 'gU0UNSLgwOj69HZOmQ0XSuUKyxNc2CZU')



result = urllib2.urlopen(req, json.dumps(data))
#urllib2.urlopen.request('POST', )


print '\n'.join(result.readlines())