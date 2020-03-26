

import httplib2

h = httplib2.Http(".cache")
h.add_credentials('admin', 'adminpass')

resp, content = h.request('http://10.0.2.2:8083/vtn-webapi/vtns/vtn1/vbridges/vb1/interfaces/if1/portmap/detail', "GET")

# bytes to string
cont = content.decode("utf-8")
print(cont)

# test map 2 port
resp, content = h.request('http://10.0.2.2:8083/vtn-webapi/vtns/vtn1/vbridges/vb1/interfaces/if2/portmap/detail', "GET")

# bytes to string
cont = content.decode("utf-8")
print(cont)


