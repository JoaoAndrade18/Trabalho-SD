# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_city.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10smart_city.proto\x12\x11smartcity.devices\"Z\n\x10\x44iscoveryRequest\x12\x12\n\ngateway_ip\x18\x01 \x01(\t\x12\x18\n\x10gateway_tcp_port\x18\x02 \x01(\x05\x12\x18\n\x10gateway_udp_port\x18\x03 \x01(\x05\"\xca\x02\n\nDeviceInfo\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.smartcity.devices.DeviceType\x12\x12\n\nip_address\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x36\n\rinitial_state\x18\x05 \x01(\x0e\x32\x1f.smartcity.devices.DeviceStatus\x12\x13\n\x0bis_actuator\x18\x06 \x01(\x08\x12\x11\n\tis_sensor\x18\x07 \x01(\x08\x12\x45\n\x0c\x63\x61pabilities\x18\x08 \x03(\x0b\x32/.smartcity.devices.DeviceInfo.CapabilitiesEntry\x1a\x33\n\x11\x43\x61pabilitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdb\x03\n\x0c\x44\x65viceUpdate\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.smartcity.devices.DeviceType\x12\x37\n\x0e\x63urrent_status\x18\x03 \x01(\x0e\x32\x1f.smartcity.devices.DeviceStatus\x12J\n\x14temperature_humidity\x18\x04 \x01(\x0b\x32*.smartcity.devices.TemperatureHumidityDataH\x00\x12\x38\n\x0b\x61ir_quality\x18\x05 \x01(\x0b\x32!.smartcity.devices.AirQualityDataH\x00\x12>\n\x0e\x63urrent_sensor\x18\x06 \x01(\x0b\x32$.smartcity.devices.CurrentSensorDataH\x00\x12/\n\x06\x63\x61mera\x18\x07 \x01(\x0b\x32\x1d.smartcity.devices.CameraDataH\x00\x12\x35\n\x0c\x61\x63_ir_status\x18\x08 \x01(\x0b\x32\x1d.smartcity.devices.ACIRStatusH\x00\x12\x1c\n\x14\x63ustom_config_status\x18\x14 \x01(\tB\x06\n\x04\x64\x61ta\"@\n\x17TemperatureHumidityData\x12\x13\n\x0btemperature\x18\x01 \x01(\x01\x12\x10\n\x08humidity\x18\x02 \x01(\x01\"+\n\x0e\x41irQualityData\x12\x19\n\x11\x61ir_quality_index\x18\x01 \x01(\x01\"D\n\x11\x43urrentSensorData\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\x01\x12\x0f\n\x07voltage\x18\x02 \x01(\x01\x12\r\n\x05power\x18\x03 \x01(\x01\"4\n\nCameraData\x12\x12\n\nresolution\x18\x01 \x01(\t\x12\x12\n\nframe_rate\x18\x02 \x01(\x05\"`\n\nACIRStatus\x12\r\n\x05\x62rand\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\t\x12\x13\n\x0btemperature\x18\x03 \x01(\x05\x12\r\n\x05power\x18\x04 \x01(\x08\x12\x11\n\tfan_speed\x18\x05 \x01(\t\"|\n\rDeviceCommand\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.smartcity.devices.DeviceType\x12\x14\n\x0c\x63ommand_type\x18\x03 \x01(\t\x12\x15\n\rcommand_value\x18\x04 \x01(\t\"\xfe\x01\n\rClientRequest\x12:\n\x04type\x18\x01 \x01(\x0e\x32,.smartcity.devices.ClientRequest.RequestType\x12\x18\n\x10target_device_id\x18\x02 \x01(\t\x12\x31\n\x07\x63ommand\x18\x03 \x01(\x0b\x32 .smartcity.devices.DeviceCommand\"d\n\x0bRequestType\x12\x13\n\x0fUNKNOWN_REQUEST\x10\x00\x12\x10\n\x0cLIST_DEVICES\x10\x01\x12\x15\n\x11GET_DEVICE_STATUS\x10\x02\x12\x17\n\x13SEND_DEVICE_COMMAND\x10\x03\"\xce\x02\n\x0fGatewayResponse\x12=\n\x04type\x18\x01 \x01(\x0e\x32/.smartcity.devices.GatewayResponse.ResponseType\x12\x0f\n\x07message\x18\x02 \x01(\t\x12.\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32\x1d.smartcity.devices.DeviceInfo\x12\x36\n\rdevice_status\x18\x04 \x01(\x0b\x32\x1f.smartcity.devices.DeviceUpdate\x12\x16\n\x0e\x63ommand_status\x18\x05 \x01(\t\"k\n\x0cResponseType\x12\x14\n\x10UNKNOWN_RESPONSE\x10\x00\x12\x0f\n\x0b\x44\x45VICE_LIST\x10\x01\x12\x18\n\x14\x44\x45VICE_STATUS_UPDATE\x10\x02\x12\x0f\n\x0b\x43OMMAND_ACK\x10\x03\x12\t\n\x05\x45RROR\x10\x04*\xae\x01\n\nDeviceType\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x00\x12\n\n\x06\x43\x41MERA\x10\x01\x12\x08\n\x04POST\x10\x02\x12\x11\n\rTRAFFIC_LIGHT\x10\x03\x12\x16\n\x12\x41IR_QUALITY_SENSOR\x10\x04\x12\x16\n\x12TEMPERATURE_SENSOR\x10\x05\x12\t\n\x05\x41LARM\x10\x06\x12\x12\n\x0e\x43URRENT_SENSOR\x10\x07\x12\x14\n\x10\x41\x43_IR_CONTROLLER\x10\x08*h\n\x0c\x44\x65viceStatus\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02\x12\x08\n\x04IDLE\x10\x03\x12\n\n\x06\x41\x43TIVE\x10\x04\x12\t\n\x05\x45RROR\x10\x05\x12\x07\n\x03RED\x10\x06\x12\t\n\x05GREEN\x10\x07\x42\x0fZ\r./smartcitypbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smart_city_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\r./smartcitypb'
  _DEVICEINFO_CAPABILITIESENTRY._options = None
  _DEVICEINFO_CAPABILITIESENTRY._serialized_options = b'8\001'
  _DEVICETYPE._serialized_start=1996
  _DEVICETYPE._serialized_end=2170
  _DEVICESTATUS._serialized_start=2172
  _DEVICESTATUS._serialized_end=2276
  _DISCOVERYREQUEST._serialized_start=39
  _DISCOVERYREQUEST._serialized_end=129
  _DEVICEINFO._serialized_start=132
  _DEVICEINFO._serialized_end=462
  _DEVICEINFO_CAPABILITIESENTRY._serialized_start=411
  _DEVICEINFO_CAPABILITIESENTRY._serialized_end=462
  _DEVICEUPDATE._serialized_start=465
  _DEVICEUPDATE._serialized_end=940
  _TEMPERATUREHUMIDITYDATA._serialized_start=942
  _TEMPERATUREHUMIDITYDATA._serialized_end=1006
  _AIRQUALITYDATA._serialized_start=1008
  _AIRQUALITYDATA._serialized_end=1051
  _CURRENTSENSORDATA._serialized_start=1053
  _CURRENTSENSORDATA._serialized_end=1121
  _CAMERADATA._serialized_start=1123
  _CAMERADATA._serialized_end=1175
  _ACIRSTATUS._serialized_start=1177
  _ACIRSTATUS._serialized_end=1273
  _DEVICECOMMAND._serialized_start=1275
  _DEVICECOMMAND._serialized_end=1399
  _CLIENTREQUEST._serialized_start=1402
  _CLIENTREQUEST._serialized_end=1656
  _CLIENTREQUEST_REQUESTTYPE._serialized_start=1556
  _CLIENTREQUEST_REQUESTTYPE._serialized_end=1656
  _GATEWAYRESPONSE._serialized_start=1659
  _GATEWAYRESPONSE._serialized_end=1993
  _GATEWAYRESPONSE_RESPONSETYPE._serialized_start=1886
  _GATEWAYRESPONSE_RESPONSETYPE._serialized_end=1993
# @@protoc_insertion_point(module_scope)
