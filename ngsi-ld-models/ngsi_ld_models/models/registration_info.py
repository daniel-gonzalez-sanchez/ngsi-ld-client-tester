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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from ngsi_ld_models.models.entity_info import EntityInfo

class RegistrationInfo(BaseModel):
    """
    5.2.10 RegistrationInfo. 
    """
    entities: Optional[conlist(EntityInfo, min_items=1)] = Field(None, description="Describes the entities for which the CSource may be able to provide information. ")
    property_names: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="propertyNames", description="Describes the Properties that the CSource may be able to provide. ")
    relationship_names: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="relationshipNames", description="Describes the Relationships that the CSource may be able to provide. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["entities", "propertyNames", "relationshipNames"]

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
    def from_json(cls, json_str: str) -> RegistrationInfo:
        """Create an instance of RegistrationInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RegistrationInfo:
        """Create an instance of RegistrationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RegistrationInfo.parse_obj(obj)

        _obj = RegistrationInfo.parse_obj({
            "entities": [EntityInfo.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "property_names": obj.get("propertyNames"),
            "relationship_names": obj.get("relationshipNames")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

