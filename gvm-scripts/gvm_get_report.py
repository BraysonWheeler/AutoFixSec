from importlib.resources import path
from ipaddress import ip_address
from urllib import response
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print
from lxml import etree
import lxml
from pathlib import Path
import sys
from base64 import b64decode
import os


connection = UnixSocketConnection(path=None) #Path=None is deafult gvmd.sock location
transform = EtreeTransform()

def get_report():
    with Gmp(connection, transform=transform) as gmp:
        pdf_report_format_id = "c1645568-627a-11e3-a660-406186ea4fc5"

        gmp.authenticate('admin', '02169f70-676c-4789-8bad-8242fe85bd33')


        response = gmp.get_report(
            report_id="127f533c-d9a5-471c-bae0-78768e7eacea", report_format_id=pdf_report_format_id, filter_string='apply_overrides=0 levels=html rows=100 min_qod=70 first=1 sort-reverse=severity'
        )

        report_element = response.find("report")
        # get the full content of the report element
        content = report_element.find("report_format").tail

        if not content:
            print(
                'Requested report is empty. Either the report does not contain any '
                ' results or the necessary tools for creating the report are '
                'not installed.',
                file=sys.stderr,
            )
            sys.exit(1)

        # convert content to 8-bit ASCII bytes
        binary_base64_encoded_pdf = content.encode('ascii')

        # decode base64
        binary_pdf = b64decode(binary_base64_encoded_pdf)

        # write to file and support ~ in filename path
        pdf_path = Path("Automated_export.csv").expanduser()

        pdf_path.write_bytes(binary_pdf)

        print('[+]Done. PDF created: ' + str(pdf_path))

get_report()