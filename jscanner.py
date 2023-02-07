import socket                                    #Help Us to Connect to the webpage and get the reports
from IPy import IP                               #Converter web url in to ip

def scan(target):                                #this function is used for scanning multiple targets
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)

def check_ip(ip):                                #Converter web url in to ip
    try:
        IP(ip)
        return(ip)
    except ValueError:                           # It (h)elp Us To Store The Address and Help To Convert The link To Ip
        return socket.gethostbyname(ip)

def get_banner(s):                               # Function To scan the service name which it is running
    return s.recv(1024)                          # {we can identify the service and use it as a data}


def scan_port(ipaddress, port):
    try:
        jay = socket.socket()
        jay.settimeout(0.5)                      #Main Line It Help To Speedup The Time Of Scan But It Reduce The Accurace
        jay.connect((ipaddress, port))           #Connect  To the website
        try:
            banner = get_banner(jay)

            print('[+] Open Port' + str(port) + ' :- ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass                                    # IMP command it pass the close ports


targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
#port_num = input('Enter Number Of Port THats You Wat To Scan:  ')
if ',' in targets:                              # if The command found ( , ) then it will  treat the line as multiple targets
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)

