import pytest

from tests.utils import get_response_content


class TestPurchaseInvoiceAttachmentService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetAttachments.nv?attachmentsource=purchaseinvoice&NetvisorKey=30',
            body=get_response_content('GetAttachments.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        attachments = netvisor.purchase_invoice_attachments.get(30)
        assert attachments == [
            {
                'key': 30,
                'page_number': 1,
                'file_name': u'5520_001.pdf',
                'file_type': u'application/pdf',
                'content' : u'test'
            },
            {
                'key': 40,
                'page_number': 1,
                'file_name': u'5540_001.pdf',
                'file_type': u'application/pdf',
                'content' : u'test'
            }
        ]
