import urllib.parse
import urllib.request
import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

address = "Bharthidasan University"

url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})

print (url)
uh = urllib.request.urlopen(url)
data = uh.read()

try: js = json.loads(data.decode())
except: js = None

print(js["results"][0]["place_id"])
