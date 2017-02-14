#!/usr/bin/env python

from __future__ import print_function

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/ctcl.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')
from bs4 import BeautifulSoup

default_pathname = "/Users/philpot/ws/ctcl/data/agnes-scott-college"

# contact is <div class="mks_tab_item"><div class="nav">Contact</div>

class College(object):
    def __init__(self, *args, **kwargs):
        pass

    

def scrape(pathname=default_pathname):
    c = College()
    c.pathname = pathname
    with open(pathname, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        c.soup = soup
    return c
    tab_items = [x for x in soup.find_all("div", class_="mks_tab_item")]
    (contact, enrollment, tuition, quick) = tab_items
    contact_children = [x for x in contact.children]
    logging.info("CC {}".format(contact_children))
    c.name = contact_children[1].strip()
    c.street = contact_children[3].strip()
    c.city_state_zip = contact_children[5].strip()
    c.phone = contact_children[7].strip()
    enrollment_children = [x for x in enrollment.children]
    c.enrollment = enrollment_children
    return c

    
