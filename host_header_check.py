'''
This simple script will check for basic Host Header injection by modifying the
value of the Host Header sent in an HTTP request.
If the value recieved in the response for the Location Header is the same value
that we sent to the server, then the application is vulnerable to Host Header
Injection and by extension possibly to HTTP Cache Poisioning attacks that
involve sending a lot of such requests with the value of Host name header
modified such that an intermediary proxy caches the response of these requests
and serves it to victims later. This will result in the victims being redirected
to the attacker's page.
'''

import sys
import requests

def main(url):
    """
    This module check if the URL is vulnerable to Host Header Injection or Not
    """
    print '[+] Checking for Host Header Injection in', url
    msg_is_vuln = '[!] Vulnerable!'
    msg_not_vuln = '[-] Not vulnerable!'

    try:
        response = requests.get(url, headers={"Host":"test.com"}, \
                   allow_redirects=False)
        response_location_hdr = response.headers['Location']

        if "test.com" in response_location_hdr:
            print msg_is_vuln
        else:
            print msg_not_vuln
    except KeyError:
        print msg_not_vuln
    except:
        raise

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print '[!] Usage: python', sys.argv[0], 'http://example.com'
        sys.exit(0)
    main(sys.argv[1])
