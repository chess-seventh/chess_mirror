"""
to get times from TPG OpenData GVA
"""
import urllib.request as U
import json
from tpg_constants import TPG_BASE_URL
from tpg_constants import TPG_STOPS
from tpg_constants import TPG_USER_API



class TPG(object):
    """TPG class"""
    def __init__(self, stop):
        self.stop = stop

    def getTime(self):
        """ sort the mega string"""
        pass

def main():
    """main"""
    t = TPG()
    t.getTIme()


if __name__ == '__main__':
    main()
