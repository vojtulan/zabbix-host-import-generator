#!/usr/bin/python3

import json
import copy

with open("host_template.json", "r") as f:
     data = json.load(f)
with open("hosts.txt") as g:
     hostsPerLine =  g.read().splitlines()
with open("description.txt") as h:
     descriptions = h.read().splitlines()
with open("ip.txt") as j:
     ips = j.read().splitlines()
     result = ""
     i = 0
     output = ""
     for x in hostsPerLine:
        temp = copy.deepcopy(data)
        nowHost = hostsPerLine[i]
        nowDesc = descriptions[i]
        nowIp = ips[i]
        temp['host'] = nowHost
        temp['name'] = nowHost
        temp['interfaces'][0]['ip'] = nowIp
        temp['description'] = nowDesc
        result = result + json.dumps(temp) + ", "
        i = i + 1

result
with open("final.json", "w") as json_out:
   json_out.write(a)
   print(json_out)
