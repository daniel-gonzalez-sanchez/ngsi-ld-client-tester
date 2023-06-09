# coding: utf-8

"""
    NGSI-LD metamodel and Sensor NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API; NGSI-LD metamodel and Sensor NGSI-LD custom model.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import ngsi_ld_models
from ngsi_ld_models.models.property_notification_output import PropertyNotificationOutput  # noqa: E501
from ngsi_ld_models.rest import ApiException

class TestPropertyNotificationOutput(unittest.TestCase):
    """PropertyNotificationOutput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PropertyNotificationOutput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertyNotificationOutput`
        """
        model = ngsi_ld_models.models.property_notification_output.PropertyNotificationOutput()  # noqa: E501
        if include_optional :
            return PropertyNotificationOutput(
                type = 'Property', 
                value = None, 
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                unit_code = '', 
                dataset_id = '', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                instance_id = '', 
                previous_value = None
            )
        else :
            return PropertyNotificationOutput(
                type = 'Property',
                value = None,
        )
        """

    def testPropertyNotificationOutput(self):
        """Test PropertyNotificationOutput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
