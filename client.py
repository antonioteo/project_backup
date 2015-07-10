__author__ = 'TeodorZ'

import http.client

connection = http.client.HTTPConnection("localhost", 80)
connection.connect()

connection.request('GET', '/get_menu?menu_type=bigMc')
resp = connection.getresponse()
print(resp.status)
data_received = resp.read()
print(data_received)

connection.close()