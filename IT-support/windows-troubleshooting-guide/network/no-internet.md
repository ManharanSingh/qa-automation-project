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
- 
## 3. Restart the router.
## 4. check the IP configuration.
```cmd
ipconfig/all
```
5. Renew the IP address
   ```cmd
   ipconfig/release
   ipconfig/renew
   ```
 6. Flush the DNS cache
    ```cmd
    ipconfig/flushdns
    ```
 7. Test connectivity
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
