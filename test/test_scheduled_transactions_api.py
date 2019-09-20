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
from ynab.api.scheduled_transactions_api import ScheduledTransactionsApi  # noqa: E501
from ynab.rest import ApiException


class TestScheduledTransactionsApi(unittest.TestCase):
    """ScheduledTransactionsApi unit test stubs"""

    def setUp(self):
        self.api = ynab.api.scheduled_transactions_api.ScheduledTransactionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_scheduled_transaction_by_id(self):
        """Test case for get_scheduled_transaction_by_id

        Single scheduled transaction  # noqa: E501
        """
        pass

    def test_get_scheduled_transactions(self):
        """Test case for get_scheduled_transactions

        List scheduled transactions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
