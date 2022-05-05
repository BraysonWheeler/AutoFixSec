from importlib.resources import path
from ipaddress import ip_address
from time import sleep
from urllib import response
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print
from lxml import etree
import lxml
import time

connection = UnixSocketConnection(path=None) #Path=None is deafult gvmd.sock location
transform = EtreeTransform()

with Gmp(connection, transform=transform) as gmp:
    gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')
    #CVE-1999-0497
    #Create target to scan
    name = f"Suspect acutal Host 192.168.1.131 test" 
    #port_list = "4a4717fe-57d2-11e1-9a26-406186ea4fc5" #Default port list ID provided by openvas (generated when installing)
    port_list = "730ef368-57e2-11e1-a90f-406186ea4fc5"
    host_list=["192.168.1.131"] #Must be a list of strings
    

    response = gmp.create_target(name=name, hosts=host_list, port_list_id=port_list)
    print(etree.tostring(response))
    targete_id = response.get('id')
    sleep(10)

    #Create Task to scan the Target

    full_and_fast_scan_config_id = 'daba56c8-73ec-11df-a475-002264764cea'
    openvas_scanner_id = '08b69003-5fc2-4037-a479-93b440211c73'

    name = "Scan Suspect acutal Host 192.168.1.131"
    response2 = gmp.create_task(name=name, config_id=full_and_fast_scan_config_id, target_id=targete_id, scanner_id=openvas_scanner_id)
    print(etree.tostring(response2))
    task_id=response2.get('id')
    sleep(10)

    #Start the scan
    time.sleep(30)
    response3 = gmp.start_task(task_id)
    print(etree.tostring(response3))
