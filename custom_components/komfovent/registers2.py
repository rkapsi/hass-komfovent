"""
Modbus register definitions for Komfovent devices.

This module contains the register addresses and register sets used for communicating
with Komfovent ventilation units via Modbus TCP.
"""

from enum import Enum, IntEnum
from __future__ import annotations

#
# The access mode of a Komfovent Modbus register
class Access(Enum):
    READ_ONLY = 0
    READ_WRITE = 1

#
# The datatype of a Komfovent Modbus register
class Datatype(Enum):
    boolean = 0
    int8 = 1
    uint8 = 2
    int16 = 3
    uint16 = 4
    int32 = 5
    uint32 = 6

#
# Base class for Kmfovent Modbus registers
class Registers(IntEnum):
    def __init__(self, value: int, datatype: Datatype, access: Access):
        self._value = value
        self.datatype = datatype
        self.access = access

#
# List of Komfovent C4 Modbus registers
#
class C4_Registers(Registers):
    # General
    POWER                       = (1000, Datatype.int8, Access.READ_WRITE)
    SEASON                      = (1001, Datatype.int8, Access.READ_WRITE)
    TIME                        = (1002, Datatype.uint16, Access.READ_WRITE)
    DAY_OF_THE_WEEK             = (1003, Datatype.int8, Access.READ_WRITE)
    MONTH_DAY                   = (1004, Datatype.uint16, Access.READ_ONLY)
    YEAR                        = (1005, Datatype.int8, Access.READ_WRITE)
    MODBUS_ADDRESS              = (1006, Datatype.int8, Access.READ_WRITE)
    ALARM_STATUS_WARNINGS       = (1007, Datatype.boolean, Access.READ_ONLY)
    ALARM_STATUS_STOP_FLAGS     = (1008, Datatype.boolean, Access.READ_ONLY)
    ALARM_STATUS_STOP_CODE      = (1009, Datatype.boolean, Access.READ_ONLY)
    RECUPERATOR_LEVEL           = (1010, Datatype.int8, Access.READ_ONLY)
    ELECTRIC_HEATER_LEVEL       = (1011, Datatype.int8, Access.READ_ONLY)
    WATER_HEATING_LEVEL         = (1012, Datatype.int8, Access.READ_ONLY)
    WATER_COOLING_LEVEL         = (1013, Datatype.int8, Access.READ_ONLY)

    # Ventilation
    VENTILATION_LEVEL_MANUAL    = (1100, Datatype.int8, Access.READ_WRITE)
    VENTILATION_LEVEL_CURRENT   = (1101, Datatype.int8, Access.READ_ONLY)
    MODE                        = (1102, Datatype.int8, Access.READ_WRITE)
    
    INTAKE_VENTILATION_LEVEL1   = (1103, Datatype.int8, Access.READ_WRITE)
    INTAKE_VENTILATION_LEVEL2   = (1104, Datatype.int8, Access.READ_WRITE)
    INTAKE_VENTILATION_LEVEL3   = (1105, Datatype.int8, Access.READ_WRITE)
    INTAKE_VENTILATION_LEVEL4   = (1106, Datatype.int8, Access.READ_WRITE)
    
    EXHAUST_VENTILATION_LEVEL1  = (1107, Datatype.int8, Access.READ_WRITE)
    EXHAUST_VENTILATION_LEVEL2  = (1108, Datatype.int8, Access.READ_WRITE)
    EXHAUST_VENTILATION_LEVEL3  = (1109, Datatype.int8, Access.READ_WRITE)
    EXHAUST_VENTILATION_LEVEL4  = (1110, Datatype.int8, Access.READ_WRITE)
    
    OVR_ENABLE                  = (1111, Datatype.int8, Access.READ_WRITE)
    OVR_TIME_SET                = (1112, Datatype.int8, Access.READ_WRITE)
    OVR_TIME_GET                = (1113, Datatype.int8, Access.READ_ONLY)
    AHU_FAN_STATUS              = (1114, Datatype.boolean, Access.READ_ONLY)
    SUPPLY_FAN_LEVEL            = (1115, Datatype.int8, Access.READ_ONLY)
    EXHAUST_FAN_LEVEL           = (1116, Datatype.int8, Access.READ_ONLY)

    # Temperature
    SUPPLY_AIR_TEMP             = (1200, Datatype.int8, Access.READ_ONLY)
    SETPOINT_TEMP               = (1201, Datatype.int8, Access.READ_WRITE)
    TEMP_CORRECTION             = (1202, Datatype.int8, Access.READ_WRITE)
    TEMP_CORRECTION_START_TIME  = (1203, Datatype.int16, Access.READ_WRITE)
    TEMP_CORRECTION_STOP_TIME   = (1204, Datatype.int16, Access.READ_WRITE)
    WATER_TEMP                  = (1203, Datatype.int8, Access.READ_ONLY)

    # Scheduling
    MONDAY_START_TIME1          = (1300, Datatype.uint16, Access.READ_WRITE)
    MONDAY_STOP_TIME1           = (1301, Datatype.uint16, Access.READ_WRITE)
    MONDAY_START_TIME2          = (1302, Datatype.uint16, Access.READ_WRITE)
    MONDAY_STOP_TIME2           = (1303, Datatype.uint16, Access.READ_WRITE)
    MONDAY_START_TIME3          = (1304, Datatype.uint16, Access.READ_WRITE)
    MONDAY_STOP_TIME3           = (1305, Datatype.uint16, Access.READ_WRITE)

    TUESDAY_START_TIME1         = (1306, Datatype.uint16, Access.READ_WRITE)
    TUESDAY_STOP_TIME1          = (1307, Datatype.uint16, Access.READ_WRITE)
    TUESDAY_START_TIME2         = (1308, Datatype.uint16, Access.READ_WRITE)
    TUESDAY_STOP_TIME2          = (1309, Datatype.uint16, Access.READ_WRITE)
    TUESDAY_START_TIME3         = (1310, Datatype.uint16, Access.READ_WRITE)
    TUESDAY_STOP_TIME3          = (1311, Datatype.uint16, Access.READ_WRITE)

    WEDNESDAY_START_TIME1       = (1312, Datatype.uint16, Access.READ_WRITE)
    WEDNESDAY_STOP_TIME1        = (1313, Datatype.uint16, Access.READ_WRITE)
    WEDNESDAY_START_TIME2       = (1314, Datatype.uint16, Access.READ_WRITE)
    WEDNESDAY_STOP_TIME2        = (1315, Datatype.uint16, Access.READ_WRITE)
    WEDNESDAY_START_TIME3       = (1316, Datatype.uint16, Access.READ_WRITE)
    WEDNESDAY_STOP_TIME3        = (1317, Datatype.uint16, Access.READ_WRITE)

    THURSDAY_START_TIME1        = (1318, Datatype.uint16, Access.READ_WRITE)
    THURSDAY_STOP_TIME1         = (1319, Datatype.uint16, Access.READ_WRITE)
    THURSDAY_START_TIME2        = (1320, Datatype.uint16, Access.READ_WRITE)
    THURSDAY_STOP_TIME2         = (1321, Datatype.uint16, Access.READ_WRITE)
    THURSDAY_START_TIME3        = (1322, Datatype.uint16, Access.READ_WRITE)
    THURSDAY_STOP_TIME3         = (1323, Datatype.uint16, Access.READ_WRITE)

    FRIDAY_START_TIME1          = (1324, Datatype.uint16, Access.READ_WRITE)
    FRIDAY_STOP_TIME1           = (1325, Datatype.uint16, Access.READ_WRITE)
    FRIDAY_START_TIME2          = (1326, Datatype.uint16, Access.READ_WRITE)
    FRIDAY_STOP_TIME2           = (1327, Datatype.uint16, Access.READ_WRITE)
    FRIDAY_START_TIME3          = (1328, Datatype.uint16, Access.READ_WRITE)
    FRIDAY_STOP_TIME3           = (1329, Datatype.uint16, Access.READ_WRITE)

    SATURDAY_START_TIME1        = (1330, Datatype.uint16, Access.READ_WRITE)
    SATURDAY_STOP_TIME1         = (1331, Datatype.uint16, Access.READ_WRITE)
    SATURDAY_START_TIME2        = (1332, Datatype.uint16, Access.READ_WRITE)
    SATURDAY_STOP_TIME2         = (1333, Datatype.uint16, Access.READ_WRITE)
    SATURDAY_START_TIME3        = (1334, Datatype.uint16, Access.READ_WRITE)
    SATURDAY_STOP_TIME3         = (1335, Datatype.uint16, Access.READ_WRITE)

    SUNDAY_START_TIME1          = (1336, Datatype.uint16, Access.READ_WRITE)
    SUNDAY_STOP_TIME1           = (1337, Datatype.uint16, Access.READ_WRITE)
    SUNDAY_START_TIME2          = (1338, Datatype.uint16, Access.READ_WRITE)
    SUNDAY_STOP_TIME2           = (1339, Datatype.uint16, Access.READ_WRITE)
    SUNDAY_START_TIME3          = (1340, Datatype.uint16, Access.READ_WRITE)
    SUNDAY_STOP_TIME3           = (1341, Datatype.uint16, Access.READ_WRITE)

    MONDAY_VENTILATION_LEVEL1   = (1342, Datatype.int8, Access.READ_ONLY)
    MONDAY_VENTILATION_LEVEL2   = (1343, Datatype.int8, Access.READ_ONLY)
    MONDAY_VENTILATION_LEVEL3   = (1344, Datatype.int8, Access.READ_ONLY)

    TUESDAY_VENTILATION_LEVEL1  = (1345, Datatype.int8, Access.READ_ONLY)
    TUESDAY_VENTILATION_LEVEL2  = (1346, Datatype.int8, Access.READ_ONLY)
    TUESDAY_VENTILATION_LEVEL3  = (1347, Datatype.int8, Access.READ_ONLY)

    WEDNESDAY_VENTILATION_LEVEL1 = (1348, Datatype.int8, Access.READ_ONLY)
    WEDNESDAY_VENTILATION_LEVEL2 = (1349, Datatype.int8, Access.READ_ONLY)
    WEDNESDAY_VENTILATION_LEVEL3 = (1350, Datatype.int8, Access.READ_ONLY)

    THURSDAY_VENTILATION_LEVEL1 = (1351, Datatype.int8, Access.READ_ONLY)
    THURSDAY_VENTILATION_LEVEL2 = (1352, Datatype.int8, Access.READ_ONLY)
    THURSDAY_VENTILATION_LEVEL3 = (1353, Datatype.int8, Access.READ_ONLY)

    FRIDAY_VENTILATION_LEVEL1   = (1354, Datatype.int8, Access.READ_ONLY)
    FRIDAY_VENTILATION_LEVEL2   = (1355, Datatype.int8, Access.READ_ONLY)
    FRIDAY_VENTILATION_LEVEL3   = (1356, Datatype.int8, Access.READ_ONLY)

    SATURDAY_VENTILATION_LEVEL1 = (1357, Datatype.int8, Access.READ_ONLY)
    SATURDAY_VENTILATION_LEVEL2 = (1358, Datatype.int8, Access.READ_ONLY)
    SATURDAY_VENTILATION_LEVEL3 = (1359, Datatype.int8, Access.READ_ONLY)

    SUNDAY_VENTILATION_LEVEL1   = (1360, Datatype.int8, Access.READ_ONLY)
    SUNDAY_VENTILATION_LEVEL2   = (1361, Datatype.int8, Access.READ_ONLY)
    SUNDAY_VENTILATION_LEVEL3   = (1362, Datatype.int8, Access.READ_ONLY)

#
# List of C6 Modbus registers
#
class C6_Registers(Registers):
    # Modbus registers - Basic Control
    REG_POWER = (1, Datatype.uint16, Access.READ_WRITE) # ON/OFF status
    REG_AUTO_MODE_CONTROL = (2, Datatype.uint16, Access.READ_WRITE) # Auto mode control
    REG_ECO_MODE = (3, Datatype.uint16, Access.READ_WRITE) # ECO mode
    REG_AUTO_MODE = (4, Datatype.uint16, Access.READ_WRITE) # AUTO mode
    REG_OPERATION_MODE = (5, Datatype.uint16, Access.READ_WRITE) # Operation mode
    REG_SCHEDULER_MODE = (6, Datatype.uint16, Access.READ_WRITE) # Scheduler operation mode
    REG_NEXT_MODE = (7, Datatype.uint16, Access.READ_WRITE) # Next mode
    REG_NEXT_MODE_TIME = (8, Datatype.uint16, Access.READ_WRITE) # Next mode start time
    REG_NEXT_MODE_WEEKDAY = (9, Datatype.uint16, Access.READ_WRITE) # Next mode weekday
    REG_BEFORE_MODE_MASK = (10, Datatype.uint16, Access.READ_WRITE) # Before been mode mask
    
    # Temperature and Flow control
    REG_TEMP_CONTROL = (11, Datatype.uint16, Access.READ_WRITE) # Temperature control
    REG_FLOW_CONTROL = (12, Datatype.uint16, Access.READ_WRITE) # Flow control
    REG_MAX_SUPPLY_FLOW = (13, Datatype.uint32, Access.READ_WRITE) # Maximum supply flow (32-bit)
    REG_MAX_EXTRACT_FLOW = (15, Datatype.uint32, Access.READ_WRITE) # Maximum extract flow (32-bit)
    REG_MAX_SUPPLY_PRESSURE = (17, Datatype.uint16, Access.READ_WRITE) # Max supply pressure
    REG_MAX_EXTRACT_PRESSURE = (18, Datatype.uint16, Access.READ_WRITE) # Max extract pressure
    REG_ROOM_SENSOR = (39, Datatype.uint16, Access.READ_WRITE) # Room sensor (Panel 1 = 0, Panel 2 = 1; undocumented for C6)
    
    # Control sequence
    REG_STAGE1 = (19, Datatype.uint16, Access.READ_WRITE) # Control stage 1
    REG_STAGE2 = (20, Datatype.uint16, Access.READ_WRITE) # Control stage 2
    REG_STAGE3 = (21, Datatype.uint16, Access.READ_WRITE) # Control stage 3
    REG_EXTERNAL_COIL_TYPE = (22, Datatype.uint16, Access.READ_WRITE) # External coil type
    REG_ICING_PROTECTION = (40, Datatype.uint16, Access.READ_WRITE) # Icing protection (Off = 0, On = 1, External coil = 2)
    REG_INDOOR_HUMIDITY = (41, Datatype.uint16, Access.READ_WRITE) # Indoor humidity (Auto = -1, Manual = 10-90%RH)
    
    # Connectivity
    REG_DHCP = (35, Datatype.uint16, Access.READ_WRITE) # DHCP (Off = 0, On = 1)
    REG_IP = (23, Datatype.uint32, Access.READ_WRITE) # IP address (32-bit)
    REG_MASK = (25, Datatype.uint32, Access.READ_WRITE) # Network mask (32-bit)
    REG_GATEWAY = (36, Datatype.uint32, Access.READ_WRITE) # Network gateway (32-bit)
    REG_BACNET_ID = (38, Datatype.uint32, Access.READ_WRITE) # Bacnet ID (32-bit)
    REG_BACNET_PORT = (44, Datatype.uint16, Access.READ_WRITE) # Bacnet port
    
    # Settings
    REG_LANGUAGE = (27, Datatype.uint16, Access.READ_WRITE) # Language
    REG_FLOW_UNIT = (28, Datatype.uint16, Access.READ_WRITE) # Flow unit
    REG_FIRE_ALARM_RESTART = (42, Datatype.uint16, Access.READ_WRITE) # Fire alarm restart (Off = 0, On = 1)
    
    # Time and date 
    REG_TIME = (29, Datatype.uint16, Access.READ_WRITE) # Time HH:MM
    REG_YEAR = (30, Datatype.uint16, Access.READ_WRITE) # Year
    REG_MONTH_DAY = (31, Datatype.uint16, Access.READ_WRITE) # Month/Day
    REG_WEEK_DAY = (32, Datatype.uint16, Access.READ_WRITE) # Week day
    REG_EPOCH_TIME = (33, Datatype.uint32, Access.READ_WRITE) # Time since 1970 (32-bit)
    
    # Away mode registers
    REG_AWAY_FAN_SUPPLY = (100, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_AWAY_FAN_EXTRACT = (102, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_AWAY_TEMP = (104, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_AWAY_HEATER = (105, Datatype.uint16, Access.READ_WRITE) # Electric heater
    
    # Normal mode registers
    REG_NORMAL_FAN_SUPPLY = (106, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_NORMAL_FAN_EXTRACT = (108, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_NORMAL_SETPOINT = (110, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_NORMAL_HEATER = (111, Datatype.uint16, Access.READ_WRITE) # Electric heater
    
    # Intensive mode registers
    REG_INTENSIVE_FAN_SUPPLY = (112, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_INTENSIVE_FAN_EXTRACT = (114, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_INTENSIVE_TEMP = (116, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_INTENSIVE_HEATER = (117, Datatype.uint16, Access.READ_WRITE) # Electric heater
    
    # Boost mode registers
    REG_BOOST_FAN_SUPPLY = (118, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_BOOST_FAN_EXTRACT = (120, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_BOOST_TEMP = (122, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_BOOST_HEATER = (123, Datatype.uint16, Access.READ_WRITE) # Electric heater
    
    # Kitchen mode registers
    REG_KITCHEN_SUPPLY = (124, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_KITCHEN_EXTRACT = (126, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_KITCHEN_TEMP = (128, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_KITCHEN_HEATER = (129, Datatype.uint16, Access.READ_WRITE) # Electric heater
    REG_KITCHEN_TIMER = (130, Datatype.uint16, Access.READ_WRITE) # Timer time
    
    # Fireplace mode registers
    REG_FIREPLACE_SUPPLY = (131, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_FIREPLACE_EXTRACT = (133, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_FIREPLACE_TEMP = (135, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_FIREPLACE_HEATER = (136, Datatype.uint16, Access.READ_WRITE) # Electric heater
    REG_FIREPLACE_TIMER = (137, Datatype.uint16, Access.READ_WRITE) # Timer time
    
    # Override mode registers
    REG_OVERRIDE_SUPPLY = (138, Datatype.uint32, Access.READ_WRITE) # Supply flow (32-bit)
    REG_OVERRIDE_EXTRACT = (140, Datatype.uint32, Access.READ_WRITE) # Extract flow (32-bit)
    REG_OVERRIDE_TEMP = (142, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_OVERRIDE_HEATER = (143, Datatype.uint16, Access.READ_WRITE) # Electric heater
    REG_OVERRIDE_ACTIVATION = (144, Datatype.uint16, Access.READ_WRITE) # Activation mode
    REG_OVERRIDE_TIMER = (145, Datatype.uint16, Access.READ_WRITE) # Timer time
    REG_OVERRIDE_DELAY_START = (157, Datatype.uint16, Access.READ_WRITE) # Delayed start time (0-10 minutes)
    REG_OVERRIDE_DELAY_STOP = (158, Datatype.uint16, Access.READ_WRITE) # Delayed stop time (0-30 minutes)
    
    # Holiday mode registers
    REG_HOLIDAYS_MICRO_VENT = (146, Datatype.uint16, Access.READ_WRITE) # Micro-ventilation
    REG_HOLIDAYS_TEMP = (147, Datatype.int16, Access.READ_WRITE) # Setpoint
    REG_HOLIDAYS_HEATER = (148, Datatype.uint16, Access.READ_WRITE) # Electric heater
    REG_HOLIDAYS_FROM = (149, Datatype.uint32, Access.READ_WRITE) # From Day/Month
    REG_HOLIDAYS_UNTIL = (151, Datatype.uint32, Access.READ_WRITE) # Until Day/Month
    REG_HOLIDAYS_YEAR_FROM = (153, Datatype.uint16, Access.READ_WRITE) # Year, from
    REG_HOLIDAYS_DATE_FROM = (154, Datatype.uint16, Access.READ_WRITE) # Month/Day, from
    REG_HOLIDAYS_YEAR_TILL = (155, Datatype.uint16, Access.READ_WRITE) # Year, until
    REG_HOLIDAYS_DATE_TILL = (156, Datatype.uint16, Access.READ_WRITE) # Month/Day, until
    
    # ECO settings
    REG_ECO_MIN_TEMP = (200, Datatype.uint16, Access.READ_WRITE) # Minimum supply air temperature
    REG_ECO_MAX_TEMP = (201, Datatype.uint16, Access.READ_WRITE) # Maximum supply air temperature
    REG_ECO_FREE_HEAT_COOL = (202, Datatype.uint16, Access.READ_WRITE) # Free heating/cooling
    REG_ECO_HEATER_BLOCKING = (203, Datatype.uint16, Access.READ_WRITE) # Heating denied
    REG_ECO_COOLER_BLOCKING = (204, Datatype.uint16, Access.READ_WRITE) # Cooling denied
    REG_ECO_HEAT_RECOVERY = (217, Datatype.uint16, Access.READ_WRITE) # Heat recovery control mode
    
    # Air quality settings
    REG_AQ_IMPURITY_CONTROL = (205, Datatype.uint16, Access.READ_WRITE) # Impurity control
    REG_AQ_TEMP_SETPOINT = (206, Datatype.int16, Access.READ_WRITE) # Temperature setpoint
    REG_AQ_IMPURITY_SETPOINT = (207, Datatype.uint16, Access.READ_WRITE) # CO2/VOC setpoint
    REG_AQ_HUMIDITY_SETPOINT = (208, Datatype.uint16, Access.READ_WRITE) # Humidity setpoint
    REG_AQ_MIN_INTENSITY = (209, Datatype.uint16, Access.READ_WRITE) # Air quality minimum intensity
    REG_AQ_MAX_INTENSITY = (210, Datatype.uint16, Access.READ_WRITE) # Air quality maximum intensity
    REG_AQ_ELECTRIC_HEATER = (211, Datatype.uint16, Access.READ_WRITE) # Air quality electric heater
    REG_AQ_CHECK_PERIOD = (212, Datatype.uint16, Access.READ_WRITE) # Air quality check period
    REG_AQ_SENSOR1_TYPE = (213, Datatype.uint16, Access.READ_WRITE) # Air quality sensor 1 type
    REG_AQ_SENSOR2_TYPE = (214, Datatype.uint16, Access.READ_WRITE) # Air quality sensor 2 type
    REG_AQ_HUMIDITY_CONTROL = (215, Datatype.uint16, Access.READ_WRITE) # Humidity control (undocumented for C6)
    REG_AQ_OUTDOOR_HUMIDITY = (216, Datatype.uint16, Access.READ_WRITE) # Outdoor humidity sensor (undocumented for C6)
    
    # Alarm registers
    REG_ACTIVE_ALARMS_COUNT = (600, Datatype.uint16, Access.READ_WRITE) # Active alarms count (write 0x99C6 to reset and restore previous mode)
    REG_ACTIVE_ALARM1 = (601, Datatype.uint16, Access.READ_WRITE) # Active alarm 1 code
    REG_ACTIVE_ALARM2 = (602, Datatype.uint16, Access.READ_WRITE) # Active alarm 2 code
    REG_ACTIVE_ALARM3 = (603, Datatype.uint16, Access.READ_WRITE) # Active alarm 3 code
    REG_ACTIVE_ALARM4 = (604, Datatype.uint16, Access.READ_WRITE) # Active alarm 4 code
    REG_ACTIVE_ALARM5 = (605, Datatype.uint16, Access.READ_WRITE) # Active alarm 5 code
    REG_ACTIVE_ALARM6 = (606, Datatype.uint16, Access.READ_WRITE) # Active alarm 6 code
    REG_ACTIVE_ALARM7 = (607, Datatype.uint16, Access.READ_WRITE) # Active alarm 7 code
    REG_ACTIVE_ALARM8 = (608, Datatype.uint16, Access.READ_WRITE) # Active alarm 8 code
    REG_ACTIVE_ALARM9 = (609, Datatype.uint16, Access.READ_WRITE) # Active alarm 9 code
    REG_ACTIVE_ALARM10 = (610, Datatype.uint16, Access.READ_WRITE) # Active alarm 10 code
    
    # Sensor registers
    # Unit status bitmask values:
    # Starting=0, Stopping=1, Fan=2, Rotor=3, Heating=4, Cooling=5,
    # HeatingDenied=6, CoolingDenied=7, FlowDown=8, FreeHeating=9,
    # FreeCooling=10, AlarmF=11, AlarmW=12
    REG_STATUS = (900, Datatype.uint16, Access.READ_WRITE) # Unit status bitmask
    REG_HEATING_CONFIG = (901, Datatype.uint16, Access.READ_WRITE) # Heating/cooling config
    REG_SUPPLY_TEMP = (902, Datatype.int16, Access.READ_WRITE) # Supply air temperature (x10 °C)
    REG_EXTRACT_TEMP = (903, Datatype.int16, Access.READ_WRITE) # Extract air temperature (x10 °C)
    REG_OUTDOOR_TEMP = (904, Datatype.int16, Access.READ_WRITE) # Outdoor air temperature (x10 °C)
    REG_WATER_TEMP = (905, Datatype.int16, Access.READ_WRITE) # Water temperature (x10 °C)
    REG_SUPPLY_FLOW = (906, Datatype.uint32, Access.READ_WRITE) # Supply air flow (32-bit)
    REG_EXTRACT_FLOW = (908, Datatype.uint32, Access.READ_WRITE) # Extract air flow (32-bit)
    REG_SUPPLY_FAN = (910, Datatype.uint16, Access.READ_WRITE) # Supply fan speed
    REG_EXTRACT_FAN = (911, Datatype.uint16, Access.READ_WRITE) # Extract fan speed
    REG_HEAT_EXCHANGER = (912, Datatype.uint16, Access.READ_WRITE) # Heat exchanger signal
    REG_ELECTRIC_HEATER = (913, Datatype.uint16, Access.READ_WRITE) # Electric heater signal (x10 %)
    REG_WATER_HEATER = (914, Datatype.uint16, Access.READ_WRITE) # Water heater signal
    REG_WATER_COOLER = (915, Datatype.uint16, Access.READ_WRITE) # Water cooler signal
    REG_DX_UNIT = (916, Datatype.int16, Access.READ_WRITE) # DX unit signal
    REG_FILTER_CLOGGING = (917, Datatype.uint16, Access.READ_WRITE) # Filter clogging
    REG_AIR_DAMPERS = (918, Datatype.uint16, Access.READ_WRITE) # Air dampers
    REG_SUPPLY_PRESSURE = (919, Datatype.uint16, Access.READ_WRITE) # Supply pressure
    REG_EXTRACT_PRESSURE = (920, Datatype.uint16, Access.READ_WRITE) # Extract pressure
    REG_EXTRACT_AQ_1 = (952, Datatype.uint16, Access.READ_WRITE) # Air quality sensor 1 value
    REG_EXTRACT_AQ_2 = (953, Datatype.uint16, Access.READ_WRITE) # Air quality sensor 2 value
    REG_HEAT_EXCHANGER_TYPE = (955, Datatype.uint16, Access.READ_WRITE) # Heat exchanger type
    REG_INDOOR_ABS_HUMIDITY = (956, Datatype.uint16, Access.READ_WRITE) # Indoor absolute humidity (undocumented for C6)
    REG_OUTDOOR_ABS_HUMIDITY = (957, Datatype.uint16, Access.READ_WRITE) # Outdoor absolute humidity (undocumented for C6)
    REG_EXHAUST_TEMP = (961, Datatype.int16, Access.READ_WRITE) # Exhaust temperature
    
    # Efficiency status
    REG_POWER_CONSUMPTION = (921, Datatype.uint16, Access.READ_WRITE) # Power consumption
    REG_HEATER_POWER = (922, Datatype.uint16, Access.READ_WRITE) # Heater power
    REG_HEAT_RECOVERY = (923, Datatype.uint16, Access.READ_WRITE) # Heat recovery
    REG_HEAT_EFFICIENCY = (924, Datatype.uint16, Access.READ_WRITE) # Heat exchanger efficiency
    REG_ENERGY_SAVING = (925, Datatype.uint16, Access.READ_WRITE) # Energy saving
    REG_SPI = (926, Datatype.uint16, Access.READ_WRITE) # Specific power input
    
    # Consumption registers
    REG_AHU_DAY = (927, Datatype.uint32, Access.READ_WRITE) # AHU consumption Day (32-bit)
    REG_AHU_MONTH = (929, Datatype.uint32, Access.READ_WRITE) # AHU consumption Month (32-bit)
    REG_AHU_TOTAL = (931, Datatype.uint32, Access.READ_WRITE) # AHU consumption Total (32-bit)
    REG_HEATER_DAY = (933, Datatype.uint32, Access.READ_WRITE) # Additional heater Day (32-bit)
    REG_HEATER_MONTH = (935, Datatype.uint32, Access.READ_WRITE) # Additional heater Month (32-bit)
    REG_HEATER_TOTAL = (937, Datatype.uint32, Access.READ_WRITE) # Additional heater Total (32-bit)
    REG_RECOVERY_DAY = (939, Datatype.uint32, Access.READ_WRITE) # Recovered energy Day (32-bit)
    REG_RECOVERY_MONTH = (941, Datatype.uint32, Access.READ_WRITE) # Recovered energy Month (32-bit)
    REG_RECOVERY_TOTAL = (943, Datatype.uint32, Access.READ_WRITE) # Recovered energy Total (32-bit)
    REG_SPI_DAY = (945, Datatype.uint16, Access.READ_WRITE) # SPI per day
    
    # Panel sensor registers
    REG_PANEL1_TEMP = (946, Datatype.int16, Access.READ_WRITE) # Panel 1 temperature
    REG_PANEL1_RH = (947, Datatype.int16, Access.READ_WRITE) # Panel 1 relative humidity
    REG_PANEL1_AQ = (948, Datatype.uint16, Access.READ_WRITE) # Panel 1 air quality
    REG_PANEL2_TEMP = (949, Datatype.int16, Access.READ_WRITE) # Panel 2 temperature
    REG_PANEL2_RH = (950, Datatype.int16, Access.READ_WRITE) # Panel 2 relative humidity
    REG_PANEL2_AQ = (951, Datatype.uint16, Access.READ_WRITE) # Panel 2 air quality
    REG_CONNECTED_PANELS = (954, Datatype.uint16, Access.READ_WRITE) # Connected panels
    
    # Digital Outputs
    REG_DO_ALARM = (958, Datatype.uint16, Access.READ_WRITE) # Digital Output: Alarm
    REG_DO_HEATING = (959, Datatype.uint16, Access.READ_WRITE) # Digital Output: Heating
    REG_DO_COOLING = (960, Datatype.uint16, Access.READ_WRITE) # Digital Output: Cooling
    
    # Firmware registers
    REG_FIRMWARE = (1000, Datatype.uint32, Access.READ_WRITE) # Firmware version (32-bit)
    REG_PANEL1_FW = (1002, Datatype.uint32, Access.READ_WRITE) # Panel 1 firmware version (32-bit)
    REG_PANEL2_FW = (1004, Datatype.uint32, Access.READ_WRITE) # Panel 2 firmware version (32-bit)
    
    # Reset register
    REG_RESET_SETTINGS = (1050, Datatype.uint16, Access.READ_WRITE) # Reset settings
    REG_CLEAN_FILTERS = (1051, Datatype.uint16, Access.READ_WRITE) # Clean filters calibration