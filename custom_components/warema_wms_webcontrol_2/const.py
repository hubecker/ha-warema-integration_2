"""Constants"""
CONF_WEBCONTROL_SERVER_ADDR = "webcontrol_server_addr"
CONF_UPDATE_INTERVAL = "update_interval"

BASE_URL = "http://www.wienerlinien.at/ogd_realtime/monitor?rbl={}"

DEPARTURES = {
    "first": {"key": 0, "name": "{} first departure"},
    "next": {"key": 1, "name": "{} next departure"},
}