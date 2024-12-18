import logging

from odoo.http import request
from win32comext.adsi.demos.search import print_attribute

from odoo import http

_logger = logging.getLogger(__name__)


class PropertyResale(http.Controller):
    def create():
        pass