#!/usr/bin/python
'''
Author: Aatif Shahdad
Description: Simple script that check for a specific case of CORS misconfig
i.e Reflection of Origin header by the server.
For ex:

If, the Origin header in the HTTP request contains:

Request ---->

GET /home HTTP/1.1
Host: example.com
Cookie: test
Origin: <our value>

Response <--------
200 OK
Access-Control-Allow-Origin: <our value>

This should tell us if there is a possiblity of the remote server being
vulnerable to a SOP(Same-Origin-Policy) bypass by means of abusing this
CORS misconfiguration.

POC for such type of attacks can be found in the repo under the name: exploit.html
'''

import sys
import requests
from termcolor import colored

def main(url):
    '''
    Send an arbitrary value of the Origin Header and check the response
    returned by the server. If it matches our header, it may indicate a
    potential issue.
    '''
    msg_is_vuln  = '[!] Seems Vulnerable!'
    msg_not_vuln = '[+] Not vulnerable!'
    msg_cors_wc  = '[-] The remote server returned a *. Please investigate.'
    msg_no_cors  = '[-] Might not support CORS'

    try:
        response = requests.get(url, headers={"Origin":"arbitraryurl.com"}, \
                   allow_redirects=True)
        response_cors_hdr = response.headers['Access-Control-Allow-Origin']

        if "arbitraryurl" in response_cors_hdr:
            print colored(msg_is_vuln, 'red')
        elif "*" in response_cors_header:
            print colored(msg_cors_wc, 'magenta')
        else:
            print colored(msg_not_vuln, 'green')
            print 'Found: %s' % response_cors_header
    except KeyError:
        print colored(msg_no_cors, 'blue')
        print colored(response.headers, 'green')
    except:
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '[!] Usage: python', sys.argv[0], 'http://example.com'
        sys.exit(-1)

    main(sys.argv[1])
