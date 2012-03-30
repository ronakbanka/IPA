#!/usr/bin/python

import base64
import urllib
import httplib
import json
import os
from urlparse import urlparse

apitoken = "a9a59cbd-a68f-473d-a6df-33c44fa2c485"

## Connection Parameter  ##
compute_endpoint = "192.168.163.20:8774"
body = ""
headers2 = {"X-Auth-Token": apitoken, "Content-Type": "application/json"}

Create_Server_Body = '{"server":{"name": "Server-name", "imageRef": "http://192.168.163.20:8774/v1.1/4/images/2", "flavorRef": "http://192.168.163.20:8774/v1.1/4/flavors/1", "metadata": {"My Server Name": "Servername-meta"}, "personality": {"path": "/etc/banner.txt", "contents": "I am a text in a banner"} }}'

## Create Server Request ##
connection2 = httplib.HTTPConnection(compute_endpoint)
connection2.request("POST", "/v1.1/4/servers", Create_Server_Body, headers2)


# HTTP response
response = connection2.getresponse()
data = response.read()
print data

connection2.close()
