import argparse
import dns.resolver

print("Author: iamsurve")

def check_dmarc(domain):
    """
    Check if the DMARC record exists for the given domain.
    """
    try:
        dmarc_record = dns.resolver.resolve('_dmarc.' + domain, 'TXT')
        for record in dmarc_record:
            if 'v=DMARC1' in record.to_text():
                return True
        return False
    except Exception as e:
        print(f"[!] Error checking DMARC record for domain '{domain}': {e}")
        return False

def check_spf(domain):
    """
    Check if the SPF record exists for the given domain.
    """
    try:
        spf_record = dns.resolver.resolve(domain, 'TXT')
        for record in spf_record:
            if 'v=spf1' in record.to_text():
                return True
        return False
    except Exception as e:
        print(f"[!] Error checking SPF record for domain '{domain}': {e}")
        return False

def check_dkim(domain, selector):
    """
    Check if the DKIM record exists for the given domain and selector.
    """
    try:
        dkim_record = dns.resolver.resolve(f'{selector}._domainkey.{domain}', 'TXT')
        for record in dkim_record:
            if 'v=DKIM1' in record.to_text():
                return True
        return False
    except Exception as e:
        print(f"[!] Error checking DKIM record for domain '{domain}' and selector '{selector}': {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Check DMARC, SPF, and DKIM records for multiple domains.')
    parser.add_argument('domains', type=str, nargs='+', help='The domains to check')
    parser.add_argument('--selector', type=str, default='default', help='The DKIM selector to check (default: default)')

    args = parser.parse_args()

    for domain in args.domains:
        print(f"Checking DMARC record for domain '{domain}'...")
        if check_dmarc(domain):
            print("[+] DMARC record exists.")
        else:
            print("[-] DMARC record does not exist.")

        print(f"Checking SPF record for domain '{domain}'...")
        if check_spf(domain):
            print("[+] SPF record exists.")
        else:
            print("[-] SPF record does not exist.")

        print(f"Checking DKIM record for domain '{domain}' and selector '{args.selector}'...")
        if check_dkim(domain, args.selector):
            print("[+] DKIM record exists.")
        else:
            print("[-] DKIM record does not exist.")

if __name__ == "__main__":
    main()
