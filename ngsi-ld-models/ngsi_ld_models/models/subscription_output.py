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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictStr, confloat, conint, conlist, validator
from ngsi_ld_models.models.entity_selector import EntitySelector
from ngsi_ld_models.models.geo_query import GeoQuery
from ngsi_ld_models.models.notification_params import NotificationParams
from ngsi_ld_models.models.temporal_query import TemporalQuery

class SubscriptionOutput(BaseModel):
    """
    SubscriptionOutput
    """
    id: StrictStr = Field(..., description="Subscription identifier (JSON-LD @id). ")
    type: StrictStr = Field(..., description="JSON-LD @type. ")
    subscription_name: Optional[StrictStr] = Field(None, alias="subscriptionName", description="A (short) name given to this Subscription. ")
    description: Optional[StrictStr] = Field(None, description="Subscription description. ")
    entities: conlist(EntitySelector, min_items=1) = Field(..., description="Entities subscribed. ")
    notification_trigger: Optional[conlist(StrictStr)] = Field(None, alias="notificationTrigger", description="The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted. ")
    q: Optional[StrictStr] = Field(None, description="Query that shall be met by subscribed entities in order to trigger the notification. ")
    geo_q: Optional[GeoQuery] = Field(None, alias="geoQ")
    csf: Optional[StrictStr] = Field(None, description="Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions. ")
    is_active: Optional[StrictBool] = Field(True, alias="isActive", description="Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered. ")
    notification: NotificationParams = Field(...)
    expires_at: Optional[datetime] = Field(None, alias="expiresAt", description="Expiration date for the subscription. ")
    temporal_q: Optional[TemporalQuery] = Field(None, alias="temporalQ")
    scope_q: Optional[StrictStr] = Field(None, alias="scopeQ", description="Scope query. ")
    lang: Optional[StrictStr] = Field(None, description="Language filter to be applied to the query (clause 4.15). ")
    time_interval: Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)] = Field(..., alias="timeInterval", description="Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached. ")
    watched_attributes: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="watchedAttributes", description="Watched Attributes (Properties or Relationships). If not defined it means any Attribute. ")
    throttling: Optional[Union[confloat(ge=1, strict=True), conint(ge=1, strict=True)]] = Field(None, description="Minimal period of time in seconds which shall elapse between two consecutive notifications. ")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was entered into an NGSI-LD system. ")
    modified_at: Optional[datetime] = Field(None, alias="modifiedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was last modified in an NGSI-LD system, e.g. in order to correct a previously entered incorrect value. ")
    deleted_at: Optional[datetime] = Field(None, alias="deletedAt", description="Is defined as the temporal Property at which the Entity, Property or Relationship was deleted from an NGSI-LD system.  Entity deletion timestamp. See clause 4.8 It is only used in notifications reporting deletions and in the Temporal Representation of Entities (clause 4.5.6), Properties (clause 4.5.7), Relationships (clause 4.5.8) and LanguageProperties (clause 5.2.32). ")
    status: Optional[StrictStr] = Field(None, description="Read-only. Provided by the system when querying the details of a subscription. ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "type", "subscriptionName", "description", "entities", "notificationTrigger", "q", "geoQ", "csf", "isActive", "notification", "expiresAt", "temporalQ", "scopeQ", "lang", "timeInterval", "watchedAttributes", "throttling", "createdAt", "modifiedAt", "deletedAt", "status"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Subscription'):
            raise ValueError("must be one of enum values ('Subscription')")
        return value

    @validator('notification_trigger')
    def notification_trigger_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted'):
                raise ValueError("each list item must be one of ('entityCreated', 'entityUpdated', 'entityDeleted', 'attributeCreated', 'attributeUpdated', 'attributeDeleted')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('active', 'paused', 'expired'):
            raise ValueError("must be one of enum values ('active', 'paused', 'expired')")
        return value

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
    def from_json(cls, json_str: str) -> SubscriptionOutput:
        """Create an instance of SubscriptionOutput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of geo_q
        if self.geo_q:
            _dict['geoQ'] = self.geo_q.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notification
        if self.notification:
            _dict['notification'] = self.notification.to_dict()
        # override the default output from pydantic by calling `to_dict()` of temporal_q
        if self.temporal_q:
            _dict['temporalQ'] = self.temporal_q.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionOutput:
        """Create an instance of SubscriptionOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionOutput.parse_obj(obj)

        _obj = SubscriptionOutput.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "subscription_name": obj.get("subscriptionName"),
            "description": obj.get("description"),
            "entities": [EntitySelector.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None,
            "notification_trigger": obj.get("notificationTrigger"),
            "q": obj.get("q"),
            "geo_q": GeoQuery.from_dict(obj.get("geoQ")) if obj.get("geoQ") is not None else None,
            "csf": obj.get("csf"),
            "is_active": obj.get("isActive") if obj.get("isActive") is not None else True,
            "notification": NotificationParams.from_dict(obj.get("notification")) if obj.get("notification") is not None else None,
            "expires_at": obj.get("expiresAt"),
            "temporal_q": TemporalQuery.from_dict(obj.get("temporalQ")) if obj.get("temporalQ") is not None else None,
            "scope_q": obj.get("scopeQ"),
            "lang": obj.get("lang"),
            "time_interval": obj.get("timeInterval"),
            "watched_attributes": obj.get("watchedAttributes"),
            "throttling": obj.get("throttling"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "deleted_at": obj.get("deletedAt"),
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

