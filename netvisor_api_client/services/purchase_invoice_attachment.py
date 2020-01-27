"""
    netvisor.services.purchase_invoice_attachment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.purchase_invoice_attachment import GetPurchaseInvoiceAttachmentRequest

class PurchaseInvoiceAttachmentService(Service):
    def get(self, key):
        request = GetPurchaseInvoiceAttachmentRequest(
            self.client,
            params={
                'attachmentsource': 'purchaseinvoice',
                'NetvisorKey': key
            }
        )
        return request.make_request()
