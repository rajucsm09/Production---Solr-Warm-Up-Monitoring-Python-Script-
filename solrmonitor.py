


#!/usr/bin/python

'''
 Jul 10, 2018
'''

import subprocess, os, socket, sys, datetime, time, threading
from random import shuffle



#********************** Properties to edit - Start ********************

genNumber = 'provide solr generation ID / or whaterver you call it'
targetHostnames = [
'host1',
'host2',
'host3',
'host4',
'host5',
'host6',
'host7',
'host8'
]

#********************** Properties to edit - End  *********************



def runCurl(ip, cmd, logfile):
  errFile = open(logfile,'a+')
  start = time.time()

  cmd = 'curl --silent --fail -X GET "http://'+ip+ cmd
  print cmd
  returnValue = subprocess.call(cmd, shell=True, stderr=errFile)

  if returnValue ==  0:
    errFile.write("CURL STATUS OK FOR :: "+ip)
  else:
    errFile.write("CURL STATUS FAILED FOR :: "+ip)
  errFile.write("\nTIME TAKEN : "+str(round(time.time() - start,3))+" Secs \n\n")
  errFile.write("**********************************************************************************************\n")
  errFile.close()



emailrecipients = "abc@abc.com, xyz@xyz.com"
companycmd = ':7575/solr/solr_endpoint'+ genNumber +'_shard1_replica1/select?q=*:*&collection=solr shard your are looking for here'+ genNumber +', your solr shard'+ genNumber + '"'
contactcmd = ':7575/solr/solr_endpoint'+ genNumber +'_shard1_replica1/select?q=*:*&collection=solr shard your are looking for here' + genNumber + '"'
outfile = '/tmp/curlOut.txt'



###### Triggering contact collection checks
with open(outfile,'a+') as f:
 f.write('                             CONTACT RESULTS         \n\n')
shuffle(targetHostnames)
[runCurl(host,contactcmd,outfile) for host in targetHostnames]


###### Triggering company collection checks
with open(outfile,'a+') as f:
 f.write('\n\n\n\n\n')
 f.write('                             COMPANY RESULTS          \n\n')
shuffle(targetHostnames)
[runCurl(host,companycmd, outfile) for host in targetHostnames]


###### Sending email
#emailcmd = "mail -r datacenter-zone-solr-monitor@abc.com -s \"Solr CURL Query Status from datacenter zone @ $(date)\" abc@abc.com " + emailrecipients + "  < " + outfile
#ret = subprocess.call(emailcmd, shell=True)
os.remove(outfile)


