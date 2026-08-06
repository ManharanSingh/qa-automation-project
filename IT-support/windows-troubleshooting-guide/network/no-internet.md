# NO Internet Connection

## Problem:
User cannot access the internet.

## Symptoms:
- No websites open
- WI-FI connected but no internet
- yellow warning icon
- no internet

## Possible causes
- Loose Ethernet cable
- router issue
- incorrect IP configuration
- DNS issue
- ISP outage

## Troubleshooting Steps
1. Verify the WI-FI or Ethernet connection.
2. Restart the computer.
3. Restart the router.
4. check the IP configuration.
```cmd
ipconfig/all
5. Renew the IP address
   ```cmd
   ipconfig/release
   ipconfig/renew
 6. Flush the DNS cache
    ```cmd
    ipconfig/flushdns
 7. Test connectivity
    ```cmd
    ping 8.8.8.8
    ping google.com

## Expected Result
The user regains internet connectivity and can access websites successfully.

## Root Cause
The issue was caused by an expired DHCP lease.
Renewing the IP address resolved the problem.
         
