#!/usr/bin/env python

from __future__ import print_function

import sys
import logging
import argparse

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

    

DEFAULT_PARSER = "lxml"

def scrape(pathname=default_pathname, parser=DEFAULT_PARSER):
    c = College()
    whitespace = u'\u22c5 \n\t'
    c.pathname = pathname
    with open(pathname, 'r') as f:
        soup = BeautifulSoup(f, parser)
        c.soup = soup
    c.tab_items = [x for x in soup.find_all("div", class_="mks_tab_item")]
    (contact, enrollment, tuition, quick) = c.tab_items
    contact_lines = list(contact.children)
    c.name = contact_lines[1].strip()
    c.street = contact_lines[3].strip()
    c.city_state_zip = contact_lines[5].strip()
    c.phone = contact_lines[7].strip()

    enroll_lines = list(enrollment.children)
    c.size = enroll_lines[1].strip(whitespace)
    c.ratio = enroll_lines[3].strip(whitespace)

    tuition_lines = list(tuition)
    c.tuition = tuition_lines[1].strip(whitespace)
    c.aid = tuition_lines[3].strip(whitespace)

    quick_lines = list(quick)
    c.aid_link = quick_lines[3]['href']
    return c


# call main() if this is run as standalone

def main(parser):
    return scrape(parser=parser)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--parser", type=str, default=DEFAULT_PARSER)
    args = parser.parse_args()
    c = main(args.parser)

