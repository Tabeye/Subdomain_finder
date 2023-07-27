import requests
from colorama import Fore, Style

def find_subdomains(domain):
    url = f"https://dnsdumpster.com/"
    data = {'targetip': domain}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    with requests.Session() as s:
        response = s.post(url, data=data, headers=headers)

        subdomains = []
        if response.status_code == 200:
            for sd in response.text.split():
                if domain in sd:
                    subdomains.append(sd.strip())

        return subdomains

if __name__ == "__main__":
    target_domain = "example.com"
    subdomains = find_subdomains(target_domain)

    if subdomains:
        print(f"{Fore.GREEN}Subdomains found for {target_domain}:{Style.RESET_ALL}")
        for subdomain in subdomains:
            print(f"{Fore.CYAN}{subdomain}{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}No subdomains found for {target_domain}.{Style.RESET_ALL}")
