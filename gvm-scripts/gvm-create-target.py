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

with Gmp(connection, transform=transform) as gmp:
    gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')
    name = f"Suspect Host 192.168.1.136" 
    port_list = "4a4717fe-57d2-11e1-9a26-406186ea4fc5" #Default port list ID provided by openvas (generated when installing)
    host_list=["192.168.1.136"] #Must be a list of strings
    

    response = gmp.create_target(name=name, hosts=host_list, port_list_id=port_list)
    print(etree.tostring(response))


    '''
    # Retrieve GMP version supported by the remote daemon
    version = gmp.get_version()

    # Prints the XML in beautiful form
    pretty_print(version)

    # Login
    gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')

    # Retrieve all tasks
    tasks = gmp.get_tasks()
    

    # Get names of tasks
    task_names = tasks.('task/name/text()')

    task_id = tasks.xpath('@id')
    print(task_id)
    pretty_print(task_names)
    '''