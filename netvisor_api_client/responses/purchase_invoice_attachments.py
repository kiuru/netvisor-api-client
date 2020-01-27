"""
    netvisor.responses.purchase_invoice_attachments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import PurchaseInvoiceAttachmentListSchema

class GetPurchaseInvoiceAttachmentResponse(Response):
    schema_cls = PurchaseInvoiceAttachmentListSchema
    tag_name = 'attachments'
