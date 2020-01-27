"""
    netvisor.requests.purchase_invoice_attachment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Request
from ..responses.purchase_invoice_attachments import GetPurchaseInvoiceAttachmentResponse

class GetPurchaseInvoiceAttachmentRequest(Request):
    method = 'GET'
    uri = 'getattachments.nv'
    response_cls = GetPurchaseInvoiceAttachmentResponse