"""Collection of free APIs that we need to supply the ZenMatch with."""

from lxml import etree as ET
import requests
import json
import xml.dom.minidom

def get_public_ip():
    r = requests.get("https://api.ipify.org")
    return r.text

def get_geo_location():
    xml_file = requests.get(f'http://api.hostip.info?ip={get_public_ip()}').content # XML
    doc = ET.fromstring(xml_file)
    country_name             = doc[3][0][2].text
    country_name_abbreviated = doc[3][0][3].text
    return country_name_abbreviated