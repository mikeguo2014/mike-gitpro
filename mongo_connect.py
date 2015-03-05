# encoding=utf-8
# __author__ = 'mike'

import pymongo

conn = pymongo.Connection("ec2-54-165-63-201.compute-1.amazonaws.com", 17018)

#连接库
db = conn['customer-production']

#用户认证
db.authenticate('yplatformprod', 'IRmIeXo7JI')

#打印所有数据
#search_c1 = '"domainNames.hostName":{$exists:true}},{"originServers.portNumber":{$exists:true}'
c_all = db.adns.find()

c1 = db.adns.find({"domainNames.active": True})

for i in c1:
    print i
    all_os = i["originServers"]
    for d in i["domainNames"]:
        if i["active"]:
            print d["target"]["idref"]
            for os in all_os:
                if os["_id"] == d["target"]["idref"]:
                    print os["ipAddress"]





#for key in content[0]:
#    print key
#    print content[0][key]

#print type(content[2]["domainNames"])
#print content[2]["domainNames"]

#t1 = dict(content[0]["domainNames"])

#print type(t1)
