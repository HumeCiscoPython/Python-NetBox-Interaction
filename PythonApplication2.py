from netbox import NetBox
from pprint import pprint
import textfsm
from netmiko import ConnectHandler



token = '0123456789abcdef0123456789abcdef01234567'
netbox = NetBox (host= 'netboxsv01.com', port= 32770, use_ssl= False, auth_token = token)
manufacturers = ['Cisco', 'Aruba', 'Dell', 'HP','Netgear']
device_info = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.99',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'ciscocancer'
    }
session = ConnectHandler(**device_info)

def get_hostname(self):
    output = self.find_prompt().replace(">"," ")
    pprint(output)

def get_vlans (self):
    output = self.send_command("show vlan",use_textfsm=True)
    for count,output[count] in enumerate(output):
        vlan_number = output[count]['vlan_id']
        vlan_name = output[count]['name']
        netbox.ipam.create_vlan(vlan_number,vlan_name)




 


#add_manufacturers(netbox,manufacturers)
def add_manufacturers(self,manufac):
    self.list = list
    for count,manufacturer in enumerate(manufac):
        try:
            netbox.dcim.create_manufacturer(name= manufacturer, slug=manufacturer)
            pprint("Manufacturer number {0} added...".format(count))
        except netbox.exceptions.CreateException as error:
            pprint(error)

#get_hostname(session)
get_vlans(session)





    




 
  
    
    
    
    













        
        
        
        


    















