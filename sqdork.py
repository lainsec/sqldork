import requests
from cdn import __sdk
import os
from time import sleep

def test_connection():
    try:
        clear_t()
        print('Testing your connection...')
        sleep(0.8)
        requests.get('https://google.com/')
    except:
        clear_t()
        print(__sdk.error)
        sleep(2)
        clear_t()
        exit()

def url_format(url):
    if url.startswith("https://") and url.endswith('/'):
        formatted_url = url
    elif url.startswith("https://") and not url.endswith('/'):
        formatted_url = f'{url}/'
    elif url.startswith("http://") and url.endswith('/'):
        formatted_url = url
    elif url.startswith("http://") and not url.endswith('/'):
        formatted_url = f'{url}/'
    elif not url.startswith("https://") and not url.startswith("http://") and url.endswith('/'):
        formatted_url = "https://" + url
    elif not url.startswith("https://") and not url.startswith("http://") and not url.endswith('/'):
        formatted_url = "https://" + url + '/'
    return formatted_url

def clear_sc():
    try:
        os.system('clear')
        print(__sdk.banner)
    except:
        os.system('cls')
        __sdk.banner

def clear_t():
    try:
        os.system('clear')
    except:
        os.system('cls')

def op1f(url):
    clear_sc()
    print('[!] Brute force started...')
    with open('dorkwl/wl1.txt','r') as wl:
        for line in wl:
            parameter = line.strip()
            try:
                new_url = f"{url}{parameter}"
                found_u = requests.get(f"{url}{parameter}")
                if found_u.status_code == 200:
                    tst_sqli = requests.get(f"{new_url}'")
                    data = tst_sqli.text
                    if 'Fatal'.lower() in data.lower():
                        print('\n[!] The website apear to have SQLi, testing...\n')
                        sleep(3)
                        print(f'[!] Failure found --> {new_url}\n')
                        break
            except Exception as e:
                print(f'[!] sqldork erro: {e}')
            except HTTPSConnectionPool:
                url = f'http://{url}/'
        input('Press enter:')

def opt1():
    clear_sc()
    print(__sdk.op1)
    url = input(__sdk.inputc)
    formated_url = url_format(url)
    op1f(formated_url)
    
def opt2():
    return
    
def option(opt):
    if opt == 1:
       opt1()
    elif opt == 2:
       opt2()
        
def choose():
    clear_sc()
    print(__sdk.options)
    opt = int(input(__sdk.inputc))
    option(opt)

if __name__ == '__main__':
    try:
        test_connection()
    except Exception as e:
        print(e)
        clear_t()
        exit()
    except KeyboardInterrupt:
        clear_t()
        exit()
    while True:
        try:
            choose()
        except Exception as e:
            print(f'[*] sqldork erro: {e}')
        except KeyboardInterrupt:
            clear_t()
            exit()