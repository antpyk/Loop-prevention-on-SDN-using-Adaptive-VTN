import httplib2
import json

h = httplib2.Http(".cache")
h.add_credentials('admin', 'adminpass')

resp, content = h.request('http://10.0.2.2:8083/vtn-webapi/vtns/vtn1/vbridges/vb1/interfaces/detail', "GET")

# bytes to string
cont = content.decode("utf-8")
print(cont)