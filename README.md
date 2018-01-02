# Some AppSec scripts to try and automate basic stuff


**Currently Contains:**

1. Script to check if an URL is vulnerable to Host Header Injection.
2. Script to check if an URL is vulnerable to CORS misconfiguration (only reflection and wildcard based).


**Dependencies for host_header_check.py:**

1. pip install requests 

**Dependencies for cors_misconfig.py:**
2. pip install requests termcolor


**To Run:**

~$ python host_header_check.py http://example.com

~$ python cors_misconfig.py http://example.com
