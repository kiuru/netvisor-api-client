"""
    netvisor.schemas.purchase_invoice_attachments.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load

from ..common import DateSchema, DecimalSchema, StringSchema
from ..fields import Boolean, Decimal, List

class AttachmentSchema(Schema):
    key = fields.Integer(load_from='attachment_netvisor_key')
    page_number = fields.Integer(load_from='attachment_page_number')
    file_name = fields.String(load_from='file_name')
    file_type = fields.String(load_from='file_type')
    content = fields.String(load_from='content')

class PurchaseInvoiceAttachmentListSchema(Schema):
    attachments = List(
        fields.Nested(AttachmentSchema),
        load_from='attachment'
    )

    @post_load
    def preprocess_attachment_list(self, input_data):
        return input_data['attachments'] if input_data else []
