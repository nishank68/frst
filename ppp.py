#!/usr/bin/python
import re
import httplib2
try:
   import simplejson as json
except ImportError:
   import json

URL_PREFIX = 'http://buildapi.eng.vmware.com'

client = httplib2.Http()

def get_resource(url, verbose=True):
   url = '%s%s' % (URL_PREFIX, url)
   if verbose:
      print 'Fetching %s ...' % url
   response, content = client.request(url)
   status = int(response['status'])
   data = json.loads(content)
   if verbose:
      print '[HTTP status %d]' % status
      if status != 200:
         print 'Error: %s' % data['http_response_code']['message']
   return status, data

if __name__ == "__main__":


   print '-' * 80
   print 'Example2: Look up a build by id, then print all it''s attributes:'

   n=raw_input('Enter build no . ')
   status, build = get_resource('/ob/build/' + n)
   if status == 200:
      for key in sorted(build.keys()):
         print "%s : %s" % (key, build[key])

   print '-' * 80
   print 'Example3: Follow the _deliverables_url link and print the deliverables:'
   status, data = get_resource(build['_deliverables_url'])
   if status == 200:
      deliverable=data['_list']
      for d in deliverable :
		 #print '%s %d' % (d['_download_url'], d['size_in_mb'])
		 lis=re.search(r'.rpm',d['_download_url'])
      		 if lis:
			print d['_download_url'] 
   ip=raw_input("enter host ip")
   u=raw_input("enter username")
   p=raw_input("enter password")
   
