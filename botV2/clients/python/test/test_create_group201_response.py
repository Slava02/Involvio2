# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from random_coffe_client.models.create_group201_response import CreateGroup201Response

class TestCreateGroup201Response(unittest.TestCase):
    """CreateGroup201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateGroup201Response:
        """Test CreateGroup201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateGroup201Response`
        """
        model = CreateGroup201Response()
        if include_optional:
            return CreateGroup201Response(
                id = 56,
                name = ''
            )
        else:
            return CreateGroup201Response(
                id = 56,
                name = '',
        )
        """

    def testCreateGroup201Response(self):
        """Test CreateGroup201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()