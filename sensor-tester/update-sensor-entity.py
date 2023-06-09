import logging
import logging.config
import os
import json
import yaml

import ngsi_ld_client
from ngsi_ld_models.models.sensor_all_of import SensorAllOf

from ngsi_ld_client.models.entity_input import EntityInput
from ngsi_ld_client.models.entity_output import EntityOutput
from ngsi_ld_models.models.temperature_all_of import TemperatureAllOf

from ngsi_ld_client.models.property_input import PropertyInput
from ngsi_ld_client.models.property_fragment_input import PropertyFragmentInput

from ngsi_ld_client.models.relationship_input import RelationshipInput

from ngsi_ld_client.models.entity_fragment_input import EntityFragmentInput
from fastapi import FastAPI, Request, status
from ngsi_ld_client.api_client import ApiClient as NGSILDClient
from ngsi_ld_client.configuration import Configuration as NGSILDConfiguration
from ngsi_ld_client.exceptions import ApiException
from ngsi_ld_client.models.replace_attrs_request import ReplaceAttrsRequest

#assuming the log config file name is logging.yaml
with open('logging.yaml', 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)

#read the file to logging config
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# NGSI-LD Context Broker
BROKER_URI = os.getenv("BROKER_URI", "http://localhost:1026/v2")
# Context Catalog
CONTEXT_CATALOG_URI = os.getenv("CONTEXT_CATALOG_URI",
                                "http://localhost:8080/context.jsonld")


# Init NGSI-LD Client
configuration = NGSILDConfiguration(host=BROKER_URI)
configuration.debug = True
ngsi_ld = NGSILDClient(configuration=configuration)

ngsi_ld.set_default_header(
    header_name="Link",
    header_value='<{0}>; '
                 'rel="http://www.w3.org/ns/json-ld#context"; '
                 'type="application/ld+json"'.format(CONTEXT_CATALOG_URI)
)

ngsi_ld.set_default_header(
    header_name="Accept",
    header_value="application/json"
)

sensor = SensorAllOf(
    name={"type":"Property", "value": "IoT-sensor"},
    description={"type": "Property", "value": "IoT sensor for temperature and humidity."},
    temperature={"type": "Property", "value": 20},
    humidity={"type": "Property", "value": 30}
)

api_instance = ngsi_ld_client.ContextInformationProvisionApi(ngsi_ld)

entity_input = sensor.to_dict()

logger.info("Sensor object representation: %s\n" % entity_input)

logger.info("EntityFragmentInput object representation: %s\n" % EntityFragmentInput.from_dict(entity_input))

try:
    # Update NGSI-LD Entity by id: PATCH /entities/{entityId}/attrs
    api_instance.update_entity(entity_id='urn:ngsi-ld:iot:Sensor:1', entity_fragment_input=EntityFragmentInput.from_dict(entity_input))
except Exception as e:
    logger.exception("Exception when calling ContextInformationProvisionApi->update_entity: %s\n" % e)

