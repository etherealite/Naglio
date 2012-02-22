"""
"This code reads a lot better when I know what it does."
-Michael Karpeles
"""
#from service import Service
from requester import GET
#from expects import Expects, StatusCode

apirequester = GET('https://tinypay.me/ping/server', 1)
apirequester.sendrequest()
#statusrule = StatusCode('apiservice', 200)
#apirules = [statusrule]
#apiexpects = Expects(apirules)
#apiservice = Service('apiservice', apirequester, Response,  apiexpects)
