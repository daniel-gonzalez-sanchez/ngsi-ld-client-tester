# coding: utf-8

"""
    NGSI-LD metamodel and Sensor NGSI-LD custom model

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API; NGSI-LD metamodel and Sensor NGSI-LD custom model.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class NotUpdatedDetails(BaseModel):
    """
    5.2.19 represents additional information provided by an implementation when an Attribute update did not happen. 
    """
    attribute_name: StrictStr = Field(..., alias="attributeName", description="Attribute name. ")
    reason: StrictStr = Field(..., description="Reason for not having changed such Attribute. ")
    registration_id: Optional[StrictStr] = Field(None, alias="registrationId", description="Registration Id corresponding to a failed distributed operation (optional). ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["attributeName", "reason", "registrationId"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NotUpdatedDetails:
        """Create an instance of NotUpdatedDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotUpdatedDetails:
        """Create an instance of NotUpdatedDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotUpdatedDetails.parse_obj(obj)

        _obj = NotUpdatedDetails.parse_obj({
            "attribute_name": obj.get("attributeName"),
            "reason": obj.get("reason"),
            "registration_id": obj.get("registrationId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

