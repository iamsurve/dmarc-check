dmarccheck

Project Description
To check the DMARC records for multiple domains at once,This script accepts multiple domains as arguments and checks for the existence of DMARC, SPF, and DKIM records for each domain. To run this script, you'll need to provide the domains as arguments when calling the script from the command line.

Checks
- Check SPF record in a domain name.
- Check DMARC record in a domain name.
- In case that SPF & DMARC is not configured, send a test email

To run this script, you'll need to have the argparse and dnspython libraries installed. You can install them using pip:

pip install argparse dnspython

![image](https://github.com/iamsurve/dmarcheck/assets/75905952/b041ce93-a032-4d85-a36f-e1690942c749)

This will check the DMARC records for example.com, example2.com, and example3.com.

Usage:
python dmarccheck.py example.com example2.com example3.com
![image](https://github.com/iamsurve/dmarcheck/assets/75905952/01de9392-fa05-40ea-8249-3aac13ff7e44)

Available options

<img width="308" alt="image" src="https://github.com/iamsurve/dmarccheck/assets/75905952/7d1516a5-40cd-4200-b9d2-86be3c0c8a60">

Check & test domain name

![image](https://github.com/iamsurve/dmarccheck/assets/75905952/53d1e2c2-8248-4c84-8207-abf4609b52a7)





