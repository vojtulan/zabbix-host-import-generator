#!/usr/bin/python3

import json
import copy

print("Script has started")

with open("host_template.json", "r") as f:
     data = json.load(f)
with open("names.txt") as g:
     names =  g.read().splitlines()
with open("descriptions.txt") as h:
     descriptions = h.read().splitlines()
with open("ips.txt") as j:
     ips = j.read().splitlines()

numHost = sum(1 for line in open('names.txt'))
numDesc = sum(1 for line in open('descriptions.txt'))
numIp = sum(1 for line in open('ips.txt'))

print("Number of names: ", numHost)
print("Number of descriptions: ", numDesc)
print("Number of ips: ", numIp)

result = ""
output = ""
i = 0
for x in names:
   temp = copy.deepcopy(data)
   host = names[i]
   desc = descriptions[i]
   ip = ips[i]
   temp['host'] = host
   temp['name'] = host
   temp['interfaces'][0]['ip'] = ip
   temp['description'] = desc
   result = result + json.dumps(temp) + ", "
   i = i + 1

result = result[:-2]   #remove space and last  comma
with open("import.json", "w") as json_out:
   json_out.write(result)

print("Script has finished")
