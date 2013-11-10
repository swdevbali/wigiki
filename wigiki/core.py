import logging
from wigiki.generator import SiteGenerator
from wigiki.config import ConfigManager
from wigiki.exceptions import *

logging.basicConfig()


def main():
    cm = ConfigManager()
    tpl_dir = cm.config['app']['templates']
    out_dir = cm.config['app']['output']
    base_url = cm.config['app']['baseurl']

    generator = SiteGenerator(tpl_dir, out_dir, base_url,
        cm.config['gists'], cm.config['site'])
    generator.cleanup()
    generator.process()
