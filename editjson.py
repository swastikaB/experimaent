import json
from collections import OrderedDict


customername = "petsmart"
certname = "pets1"

#new_content contains the modified file in string format

fp = open('test1.json', 'r')
#convert json file to python equivalent object. In this case a ordered dict
file_content =  json.load(fp, object_pairs_hook=OrderedDict)
#parse through file till the domains block is encountered

for key, value in file_content.items():
    if key == "domains":
        #In JSON domains block is a list/array, so loop through the list
        num_domains = len(value)
        #print(num_domains)
        for i in range(num_domains):
            domain = value[i]
            print(domain["id"])
            #print(json.dumps(domain, indent=2, sort_keys=False))
            ssl_block = domain["action"]["edge"]["ssl"]
            #print(json.dumps(ssl_block, indent=2, sort_keys=False))
            if ssl_block["enable"]:
                #print("-----------------------------Before modification--------------------------")
                #print(json.dumps(ssl_block, indent=2, sort_keys=False))
                if ssl_block["sni_cert"] and ssl_block["sni_cert"]["customer_name"] == customername and ssl_block["sni_cert"]["cert_name"] == certname:
                    ssl_block["sni_cert"]["customer_name"] = "instartops"
                    ssl_block["sni_cert"]["cert_name"] = "003"
                if 'non_sni_certs' in ssl_block and ssl_block["non_sni_certs"][0]["customer_name"] == customername and ssl_block["non_sni_certs"][0]["cert_name"] == certname:
                    ssl_block["non_sni_certs"][0]["customer_name"] = "instartops"
                    ssl_block["non_sni_certs"][0]["cert_name"] = "003"
            #print("-----------------------------After modification--------------------------")
            #print(json.dumps(ssl_block, indent=2, sort_keys=False))
#print(json.dumps(file_content, indent=2, sort_keys=False))

fp.close()
fw = open('test1.json', 'w')
json.dump(file_content, fw, indent=2, sort_keys=False)
