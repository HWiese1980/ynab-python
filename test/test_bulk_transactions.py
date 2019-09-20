# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ynab
from ynab.models.bulk_transactions import BulkTransactions  # noqa: E501
from ynab.rest import ApiException


class TestBulkTransactions(unittest.TestCase):
    """BulkTransactions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBulkTransactions(self):
        """Test BulkTransactions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ynab.models.bulk_transactions.BulkTransactions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
