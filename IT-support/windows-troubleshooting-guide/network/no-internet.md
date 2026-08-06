# NO Internet Connection

## Scenario
A user reports that they cannot access any websites even though they are connected to WI-FI.

## Symptoms
- No websites open
- WI-FI connected but no internet
- Yellow warning icon
- "No Internet" message

## Possible Causes
- Router issue
- incorrect IP configuration
- DNS issue
- ISP outage
- Network adapter problem

## Troubleshooting Steps
## 1. Verify the WI-FI or Ethernet connection
Many network issues are caused by simple physical problems, not software.
for example:
- WI-FI off
- Ethernet cable not plugged in properly
- Router power off

## 2. Restart the computer
Restarting clears temporary network issues such as:
- Stuck network services
- Driver glitches
- Temporary software bugs
  
## 3. Restart the router
Restarting it can fix:
- DHCP failures
- Frozen router software
- temporary ISP connection problems
  
## 4. check the IP configuration.
```cmd
ipconfig/all
```
This command displays the computer's network configuration.
It shows:
- IP Address
- Subnet Mask
- Default Gateway
- DNS Servers
- MAC Address
- DHCP status
  
## 5. Renew the IP address
   ```cmd
   ipconfig/release
   ipconfig/renew
   ```
   ipconfig/release command releases the current IP address.
   ipcofig/renew command requests a new IP address from the DHCP server(usually router).
   it fixes problems like:
   - Expired DHCP lease
   - incorrect IP configuration
   - IP conflicts
   - APIPA (169.254.x.x)
     
 ##7. Flush the DNS cache
    ```cmd
    ipconfig/flushdns
    ```
    If the cache is outdated or corrupted , Flushing the cache deletes the old entries so windows requests fresh DNS information.
    
 ## 9. Test connectivity
    ```cmd
    ping 8.8.8.8
    ping google.com
    ```
## Resolution
Renewing the IP address restored internet connectivity.

## Prevention
- Keep network drivers updated.
- Restart the router occasionally.
- Avoid incorrect manual IP settings.

## Related Commands
- ipconfig
- ping
- tracert
- nslookup
