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

def start_task(task_id):
    with Gmp(connection, transform=transform) as gmp:
        gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')
        response = gmp.start_task(task_id)
        
    print(etree.tostring(response))
    report_id =response.get('report_id') 


start_task("b194139a-7465-40ee-b880-64742ebfb8df")