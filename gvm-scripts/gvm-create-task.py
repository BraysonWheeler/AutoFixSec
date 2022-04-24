from importlib.resources import path
from ipaddress import ip_address
from urllib import response
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print
from lxml import etree
import lxml

connection = UnixSocketConnection(path=None) #Path=None is deafult gvmd.sock location
transform = EtreeTransform()

def create_task():
    with Gmp(connection, transform=transform) as gmp:

        gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')
        name = f"Suspect Host 192.168.1.136" 
        port_list = "4a4717fe-57d2-11e1-9a26-406186ea4fc5" #Default port list ID provided by openvas (generated when installing)
        host_list=["192.168.1.136"] #Must be a list of strings
        

        response = gmp.create_target(name=name, hosts=host_list, port_list_id=port_list)
        print(etree.tostring(response))
        target_id = response.get('id')

        #actual work
        full_and_fast_scan_config_id = 'daba56c8-73ec-11df-a475-002264764cea'
        openvas_scanner_id = '08b69003-5fc2-4037-a479-93b440211c73'

        name = "Scan Suspect Host 192.168.1.136"
        response2 = gmp.create_task(name=name, config_id=full_and_fast_scan_config_id, target_id=target_id, scanner_id=openvas_scanner_id)
        print(etree.tostring(response2))
        print(response2.get('id'))



create_task()