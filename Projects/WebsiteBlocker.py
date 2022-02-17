import time
from datetime import datetime as dt

sites_to_block = [                                  #sites to be blocked
    'www.youtube.com', 'youtube.com',
]

Window_host ="C:\Windows\System32\drivers\etc\hosts"              #path to windows host file
default_hoster = Window_host
redirect = "127.0.0.1"                          

def block_websites(start_hour , end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour):         #checks for the mentioned time slot
            print("Do not waste your time!!")
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.read()                     #add website URLs to the host file and mapping them to the localhost
                for site in  sites_to_block:
                    if site not in hosts:
                       hostfile.write(redirect+' '+site+'\n')
        else:
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)                    #removing from host directory once the working hour is over
                hostfile.truncate()
            print('Enjoy wasting your time')
        time.sleep(3)
if __name__ == '__main__':
    block_websites(3, 7)
    