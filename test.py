import certifi
import requests
import os

try:
    print('Checking connection to Github...')
    test = requests.get('https://api.github.com',
                        verify=False)
    print('Connection to Github OK.')
except requests.exceptions.SSLError as err:
    print('SSL Error. Adding custom certs to Certifi store...')
    cafile = certifi.where()
    with open('certificate.pem', 'rb') as infile:
        customca = infile.read()
    with open(cafile, 'ab') as outfile:
        outfile.write(customca)
    print('That might have worked.')
