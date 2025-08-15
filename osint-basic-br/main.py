import whois as www
import socket as sock
import ipaddress
import phonenumbers as phone
from phonenumbers import geocoder, carrier, timezone, is_valid_number, is_possible_number

def cellphone():
    try:
        entry = input('Enter the phone number with country code, with "+" (example: +5511912345678):')
        if len(entry) > 0:
            okay_number = phone.parse(entry)
            local = geocoder.description_for_number(okay_number, 'pt-br')
            city = str(okay_number.national_number)[:2]
            provider = carrier.name_for_number(okay_number, 'pt-br')
            time_zone = timezone.time_zones_for_number(okay_number)
            number_valid = is_valid_number(okay_number)
            number_possible = is_possible_number(okay_number)
            international_number = phone.format_number(okay_number, phone.PhoneNumberFormat.INTERNATIONAL)
            national_number = phone.format_number(okay_number, phone.PhoneNumberFormat.NATIONAL)

            codigo_area = okay_number.national_number // 10000000

            print(f'Número Completo: {entry}')
            print(f'Número Internacional: {international_number}')
            print(f'Número Nacional: {national_number}')
            print(f'Localização: {local}')
            print(f'Cidade/Local (DDD): {city}')
            print(f'Provedor: {provider}')
            print(f'Fuso Horário: {time_zone}')
            print(f'Número Válido: {number_valid}')
            print(f'Número Possível: {number_possible}')
            print(f'Código de Área: {codigo_area}')
        elif len(entry) == 0:
            return cellphone()
        else:
            return cellphone()
    except Exception as error:
        print(error)

def network_domain():
    try:
        entry = input("Enter IP address : ")
        if  len(entry) > 0:
            ip = ipaddress.IPv4Address(entry)
            print(f"\n\nScanning ports of {ip}...")
        
            for port in range(1, 501):
                client = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
                client.settimeout(0.02)
                if client.connect_ex((str(ip), port)) == 0:
                    print(f"Port {port} is open")
        elif len(entry) == 0:
            print("No data : ")
            return network_domain()
        else:
            return network_domain()

    except Exception as error:
        print(error)

def ip_addr():
    try:
        url = input("Enter the domain address :")
        if len(url) > 0:
            res = sock.gethostbyname(url)
            print(f"\nIP address of {url} : {res}")
        elif len(url) == 0:
            print("No data ! ")
            return ip_addr()
        else:
            return ip_addr()
    except Exception as error:
        print(error)
        exit()

def domain_addr():
    try:
        entry = input(" Entry domain please : ")
        if len(entry) > 0:
            res = www.whois(entry)
            print(f"{res} \n\n Sucess full ! ")
        elif len(entry) == 0:
            print("No data ! ")
            return domain_addr()
        else:
            return domain_addr()

    except Exception as error:
        print(error)
        exit()

def menu():
    while True:
        print("\n============ Main Menu H-HELP ============\n")
        print("1. IP Address")
        print("2. Domain")
        print("3. Network")
        print("4. Cellphone")
        print("5. Exit")
        
        option = input("Choose an option (1, 2, 3, 4, or 5): ").strip()

        if option == '1':
            ip_addr()
        elif option == '2':
            domain_addr()
        elif option == '3':
            network_domain()
        elif option == '4':
            cellphone()
        elif option == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    menu()
