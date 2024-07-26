# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.exceptions import UserError, AccessError
from odoo.osv import expression
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)

class Lead(models.Model):
    _inherit = "crm.lead"

    admission_id = fields.Char('Mã hồ sơ', tracking=True)