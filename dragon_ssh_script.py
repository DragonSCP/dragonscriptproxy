import random
import os
import sys
import socket
import requests
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Ignorar avisos de certificados não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

allowed_words = set([
    "http", "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH",
    "wikipedia.org", "youtube.com", "google.com", "bing.com", "vivo.com.br", 
    "plus.google.com", "myspace.com", "spotify.com", "playwaze.com",
])

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def filter_text(text):
    words = set(text.split())
    if not words.isdisjoint(allowed_words):
        return text
    return None

def test_proxy(ip, port):
    try:
        proxy_url = f"http://{ip}:{port}" if port == 80 or port == 8080 else f"https://{ip}:{port}"
        proxy_dict = {
            'http': proxy_url,
            'https': proxy_url
        }
        response = requests.get('http://icanhazip.com', proxies=proxy_dict, timeout=5, verify=False)
        response_text = response.text.strip()
        filtered_text = filter_text(response_text)
        if filtered_text:
            print(f"Proxy {ip}:{port} - {filtered_text}")
            return True, filtered_text
        elif '403 Forbidden' in response_text:
            print(f"Proxy {ip}:{port} - Acesso negado.")
            return False, None
        else:
            external_ip = response_text
            print(f"Proxy {ip}:{port} - IP Externo: {external_ip}")
            return True, external_ip
    except requests.exceptions.RequestException as e:
        print(f"Proxy {ip}:{port} - Falha na conexão: {e}")
        return False, None

def generate_ip_range(base_ip, count):
    base_parts = base_ip.split('.')
    base_prefix = '.'.join(base_parts[:-1])
    start = int(base_parts[-1])
    return [f"{base_prefix}.{i}" for i in range(start, start + count)]

def display_results(successful_proxies):
    if successful_proxies:
        print("\nProxies conectados com sucesso:")
        for ip, port, external_ip in successful_proxies:
            print(f"Proxy {ip}:{port} - IP Externo: {external_ip}")
    else:
        print("\nNenhum proxy conseguiu conectar.")

def generate_payloads():
    methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
    custom_strings = [
        "http/ \n\n",
        "°#http/ \n\n/",
        "CONNECT [host]:[port] HTTP/1.1[crlf]GET /path HTTP/1.1[crlf]Host: [host][crlf][crlf]",
    ]
    domains = ["wikipedia.org/about", "youtube.com/about", "google.com/", "bing.com/search"]
    method = random.choice(methods)
    custom_string = random.choice(custom_strings)
    domain = random.choice(domains)
    payload = f"{method} {domain} {custom_string}"
    print(f"Payload gerado: {payload}")

def main_menu():
    successful_proxies = []
    common_ports = [80, 8080, 443]
    while True:
        clear_screen()
        print("Dragon SSH Script Generator")
        print("1. Gerar e Testar Proxies a partir de um IP Base")
        print("2. Gerar Payloads")
        print("3. Testar Proxies Individuais")
        print("4. Gerar e Testar Proxies por Operadora e IP")
        print("5. Desinstalar Script")

        choice = input("Escolha uma opção: ").strip()
        if choice == '':
            break
        elif choice == '1':
            ip_base = input("Informe o IP base (e.g., 192.168.1.0): ")
            num_ips = int(input("Quantos IPs deseja gerar? "))
            ips = generate_ip_range(ip_base, num_ips)
            for ip in ips:
                for port in common_ports:
                    result, external_ip = test_proxy(ip, port)
                    if result:
                        successful_proxies.append((ip, port, external_ip))
            display_results(successful_proxies)
        elif choice == '2':
            generate_payloads()
        elif choice == '3':
            ips_input = input("Informe os Proxy IPs para testar (separados por '#'): ")
            ips = ips_input.split('#')
            for ip in ips:
                for port in common_ports:
                    result, external_ip = test_proxy(ip.strip(), port)
                    if result:
                        successful_proxies.append((ip, port, external_ip))
            display_results(successful_proxies)
        elif choice == '4':
            ip_base = input("Informe o IP base (e.g., 192.168.1.0): ")
            num_ips = int(input("Quantos IPs deseja gerar? "))
            operadora = input("Informe a operadora: ")
            ips = generate_ip_range(ip_base, num_ips)
            for ip in ips:
                for port in common_ports:
                    print(f"Testando IP: {ip} Porta: {port} Operadora: {operadora}")
                    result, external_ip = test_proxy(ip, port)
                    if result:
                        successful_proxies.append((ip, port, external_ip))
            display_results(successful_proxies)
        elif choice == '5':
            try:
                os.remove("dragon_ssh_script.py")
                sys.exit("Script desinstalado com sucesso.")
            except OSError as e:
                sys.exit(f"Erro ao desinstalar script: {e}")
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
