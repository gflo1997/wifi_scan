import subprocess

# Execute the netsh command to scan for WiFi networks
result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True)
output = result.stdout.decode('utf-8')

# Extract the SSIDs from the output and print them
ssids = [line.split(':')[1].strip() for line in output.split('\n') if 'SSID' in line]
for ssid in ssids:
    print(ssid)