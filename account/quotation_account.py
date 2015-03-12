import xmlrpclib
import csv
from datetime import datetime

username = 'verp@it-corner.net' #the user
pwd = 'Crystal_5000'      #the password of the user
dbname = 'db_live'    #the database
# 
# # Connection String ........
# 
sock_common = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)
sock = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')

reader = csv.reader(open('quotation_account.csv', "rb"), delimiter=';')
index = 0
count = 0
vals = {}
name = ''
for row in reader:
    if len(row) == 3:
        dict = {}
        order_id = sock.execute(dbname, uid, pwd, 'sale.order', 'search', [('name', '=', row[0])])
        if len(order_id) != 0:
            partner_id = sock.execute(dbname, uid, pwd, 'res.partner', 'search', [('ref', '=', row[2])])
            if len(partner_id) != 0:
                
                sock.execute(dbname, uid, pwd, 'sale.order', 'write', order_id[0],{'partner_id':partner_id[0]})
            else:
                index = index + 1
                print row[2],row[0]
        else: 
            row[0]
            count+=1

print "index = >", index
print "Count ==>", count
print " Ending Query ... "
