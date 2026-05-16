import asyncio
from typing import Any
from zigpy.quirks.v2 import EntityPlatform, EntityType
from zigpy.quirks.v2.homeassistant import LIGHT_LUX, UnitOfLength, UnitOfTime
from zigpy.quirks.v2.homeassistant.binary_sensor import BinarySensorDeviceClass
from zigpy.quirks.v2.homeassistant.sensor import SensorDeviceClass, SensorStateClass
import zigpy.types as t
from zigpy.zcl.clusters.measurement import OccupancySensing
from zigpy.zcl.clusters.security import IasZone
from zhaquirks.tuya import TuyaLocalCluster
from zhaquirks.tuya.builder import TuyaQuirkBuilder


class TuyaOccupancySensing(OccupancySensing, TuyaLocalCluster):
    """Tuya local OccupancySensing cluster."""

(
    TuyaQuirkBuilder("_TZE200_vuqzj1ej", "TS0601")
    .tuya_dp(
        dp_id=1,
        ep_attribute=TuyaOccupancySensing.ep_attribute,
        attribute_name=OccupancySensing.AttributeDefs.occupancy.name,
        converter=lambda x: x == 1,
    )
    .adds(TuyaOccupancySensing)
    .tuya_number(
        dp_id=12,
        attribute_name="detection_time",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        min_value=1,
        max_value=3600,
        step=1,
        multiplier=1,
        translation_key="detection_time",
        fallback_name="Detection time",
    )
    .tuya_sensor(
        dp_id=19,
        attribute_name="target_distance",
        type=t.uint16_t,
        state_class=SensorStateClass.MEASUREMENT,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.CENTIMETERS,
        entity_type=EntityType.STANDARD,
        translation_key="target_distance",
        fallback_name="Target distance",
    )
    .tuya_illuminance(dp_id=20)
    .tuya_number(
        dp_id=101,
        attribute_name="presence_sensitivity",
        type=t.uint16_t,
        min_value=0,
        max_value=10,
        step=1,
        translation_key="presence_sensitivity",
        fallback_name="Sensitivity",
    )
    .tuya_number(
        dp_id=102,
        attribute_name="fading_time",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        min_value=5,
        max_value=3600,
        step=1,
        translation_key="fading_time",
        fallback_name="Fading time",
    )
    .tuya_number(
        dp_id=111,
        attribute_name="detection_distance_min",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.CENTIMETERS,
        min_value=0,
        max_value=1000,
        step=50,
        translation_key="detection_distance_min",
        fallback_name="Minimum range",
    )
    .tuya_number(
        dp_id=112,
        attribute_name="detection_distance_max",
        type=t.uint16_t,
        device_class=SensorDeviceClass.DISTANCE,
        unit=UnitOfLength.CENTIMETERS,
        min_value=50,
        max_value=1000,
        step=50,
        translation_key="detection_distance_max",
        fallback_name="Maximum range",
    )
    .skip_configuration()
    .add_to_registry()
)