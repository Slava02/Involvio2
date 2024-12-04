# coding: utf-8

"""
    api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from random_coffe_client.models.create_event201_response import CreateEvent201Response

class TestCreateEvent201Response(unittest.TestCase):
    """CreateEvent201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateEvent201Response:
        """Test CreateEvent201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateEvent201Response`
        """
        model = CreateEvent201Response()
        if include_optional:
            return CreateEvent201Response(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                id = 56,
                name = '',
                users = [
                    random_coffe_client.models.user.User(
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        city = '', 
                        full_name = '', 
                        gender = '', 
                        goal = '', 
                        groups = [
                            random_coffe_client.models.group.Group(
                                id = 56, 
                                name = '', )
                            ], 
                        id = 56, 
                        interests = '', 
                        photo_url = '', 
                        position = '', 
                        socials = '', 
                        user_name = '', )
                    ]
            )
        else:
            return CreateEvent201Response(
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                id = 56,
                name = '',
                users = [
                    random_coffe_client.models.user.User(
                        birthday = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        city = '', 
                        full_name = '', 
                        gender = '', 
                        goal = '', 
                        groups = [
                            random_coffe_client.models.group.Group(
                                id = 56, 
                                name = '', )
                            ], 
                        id = 56, 
                        interests = '', 
                        photo_url = '', 
                        position = '', 
                        socials = '', 
                        user_name = '', )
                    ],
        )
        """

    def testCreateEvent201Response(self):
        """Test CreateEvent201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()