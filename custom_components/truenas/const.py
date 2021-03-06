"""Constants for the FreeNAS integration."""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

DOMAIN = "truenas"

DEFAULT_SCAN_INTERVAL_SECONDS = 30

SERVICE_VM_START = "vm_start"
SCHEMA_SERVICE_VM_START = {
    vol.Optional("overcommit"): cv.boolean,
}
SERVICE_VM_STOP = "vm_stop"
SCHEMA_SERVICE_VM_STOP = {
    vol.Optional("force"): cv.boolean,
}
SERVICE_VM_RESTART = "vm_restart"
SCHEMA_SERVICE_VM_RESTART = {}
