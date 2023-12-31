"""
Executable MicroPython Code:

Load into microcontroller as:
HwM_E4.py => main.py

Powered by YAKOTT
"""


"""
Disclaimer:
This project is for educational purposes only and should not be used for illegal or malicious activities. YAKOTT is not responsible for misuse of the information or tools provided in the project.
"""


"""
ESP32
WLAN Address Spoofing Attack

https://docs.micropython.org/en/latest/library/network.html
https://mpython.readthedocs.io/en/latest/library/micropython/network.html

Prompt: Write a script in MicroPython to connect to an access points with an ESP32. Change the MAC address of the ESP32. Change the IP address of the ESP32.
"""


# Packages


# Modules
# Network
import network
# uBinaASCII
import ubinascii as binascii
# Time
import utime as time


# Global variables
# Wait time in seconds
wait_time_s = 1


# Functions


# Classes


# Main
print("WLAN Address Spoofing Attack")
print()

# WLAN() => Instantiate a network interface object
#   network.AP_IF => Access point mode
#   network.STA_IF => Station client mode
station = network.WLAN(network.STA_IF)

# Turn on Wi-Fi
print("Turn on Wi-Fi")
# active() => Activate/Deactivate the networt interface
#   True => Activate
#   False => Deactivate
station.active(True)
print()

print("Device Information")
# decode() => Encodes the string to bytes using UTF-8 by default
# hexlify() => Return the hexadecimal representation of the binary data
print("  MAC Address: " + binascii.hexlify(station.config('mac'), ':').decode())
# hostname() => Get or set the hostname that will identify this device on the network
#   parameter
#       name => Hostname
print("  Hostname: " + network.hostname())
# country() => Get or set the two-letter ISO 3166-1 Alpha-2 country code to be used for radio compliance
#   parameter
#       code => "EC"
print("  Country: " + network.country())
# phy_mode() => Get or set the PHY mode. Only with ESP8266
#   parameter
#       network.MODE_11B => IEEE 802.11b,
#       network.MODE_11G => IEEE 802.11g,
#       network.MODE_11N => IEEE 802.11n.
#print("  Mode: " + network.phy_mode())
print()

print("New Device Information")
# https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
# Apple, Inc.           18F643000001    Brian's iPhone
# Cisco Systems, Inc    18E728000001    router
mac_hexadecimal = "18F643000001"
# unhexlify() => Return the binary data representation by the hexadecimal string
mac_binary = binascii.unhexlify(mac_hexadecimal)
# config() => Get/Set general network interface parameters
#   parameter => Standar IP configuration
#       mac/'mac' => BSSID MAC address
#       essid/'essid' => Access point name
#       channel/'channel' => 2.4 GHz band
#           [1:13]
#       hidden/'hidden' => Whether SSID is hidden
#           ["Visible", "Hidden"]
#       authmode/'authmode' => Security protocol
#           ["AUTH_OPEN", "AUTH_WEP", "AUTH_WPA_PSK", "AUTH_WPA2_PSK", "AUTH_WPA_WPA2_PSK", "", "AUTH_MAX"]
#       password/'password' => Password
#       max_clients/'max_clients' => Clients numbers
#       txpower/'txpower' => TX power in dB
station.config(mac=mac_binary)
network.hostname("Unknown")
network.country("EC")
#network.phy_mode(network.MODE_11G))
print("  MAC Address: " + binascii.hexlify(station.config('mac'), ':').decode())
print("  Hostname: " + network.hostname())
print("  Country: " + network.country())
#print("  Mode: " + network.phy_mode())
print()

# connect() => Connect the interface to a network
#   ssid => Access point name
#   password => Password
#   bssid => MAC address AP
ssid = "LABCSec"
password = "LABCSec2023"
station.connect(ssid, password)

print("Connecting ",end="")
# isconnected() => Confirm is the network interface is connected to a Wi-Fi network
while not(station.isconnected()):
    print(".", end="")
    # sleep() => Wait time in seconds
    time.sleep(wait_time_s)
print()
state_option = ["No connected", "Connected"]
state_value = station.isconnected()
state = state_option[state_value]
print(state)
print()

print("Status")
# status() => Query dynamic information of the network interface
#   response
#       1000 => STAT_IDLE
#       1001 => STAT_CONNECTING
#       202 => STAT_WRONG_PASSWORD
#       201 => STAT_NO_AP_FOUND
#       1010 => STAT_GOT_IP
#       203 => STAT_ASSOC_FAIL
#       200 => STAT_BEACON_TIMEOUT
#       204 => STAT_HANDSHAKE_TIMEOUT
#   parameter
#       network.AP_IF
#           'stations' => Devices connected
#       network.STA_IF
#           'rssi' => Signal meter
response_option = {"1000": "STAT_IDLE", "1001": "STAT_CONNECTING", "202": "STAT_WRONG_PASSWORD", "201": "STAT_NO_AP_FOUND", "1010": "STAT_GOT_IP", "203": "STAT_ASSOC_FAIL", "200": "STAT_BEACON_TIMEOUT", "204": "STAT_HANDSHAKE_TIMEOUT"}
response_value = station.status()
print(" ", response_option[str(response_value)])
RSSI = station.status('rssi')
print("  RSSI: ", RSSI)
print()

print("IP Information:")
# ifconfig() => Get/Set IP-level network interface parameters
#   ip => IP address
#   subnet_mask => Subnet mask
#   gateway => Gateway
#   dns_server => DNS server
print("  IP Address: " + station.ifconfig()[0])
print("  Subnet Mask: " + station.ifconfig()[1])
print("  IP Gateway: " + station.ifconfig()[2])
print("  DNS Server: " + station.ifconfig()[3])
print()

print("New IP Information:")
ip = "192.168.1.28"
subnet_mask = station.ifconfig()[1]
gateway = station.ifconfig()[2]
dns_server = station.ifconfig()[3]
station.ifconfig((ip, subnet_mask, gateway, dns_server))
print("  IP Address: " + station.ifconfig()[0])
print("  Subnet Mask: " + station.ifconfig()[1])
print("  IP Gateway: " + station.ifconfig()[2])
print("  DNS Server: " + station.ifconfig()[3])
print()

# Disconnect Wi-Fi
print("Disconnect Wi-Fi")
# disconnect() => Disconnect from network
station.disconnect()
print()

# Turn off Wi-Fi
print("Turn off Wi-Fi")
print()
station.active(False)
