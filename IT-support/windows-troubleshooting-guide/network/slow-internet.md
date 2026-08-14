# Slow Internet Connection

## Scenario
A user reports that  websites load very slowly , video calls lag, and file downloads take much longer than expected.
---
## Symptoms
- Websites take a long time to load
- Videos buffer frequently
- Slow file downloads
- High latency during online games or video calls
- internet disconnects occasionally
---
## Possible Causes
- Weak WI-FI signal
- Too many devices using the network
- High network usage by applications
- Background Windows updates
- DNS issues
- Outdated network adapter driver
- Router problem
- ISP network congestion
---
## Troubleshooting Steps
### 1. Check WI-FI Signal Strength
A weak WI-FI signal reduces data transfer speed.
#### Check
- Device far from the router?
- Are there walls or obstacles?
- Does moving closer improve the speed?

**If using Ethernet, ensure the cable is securely connected**

---

### 2. Restart the computer and Router
Restarting clears temporary software issues and refreshes the router's network connections.
---
### 3. Run an Internet Speed Test
Before changing settings , verify whether the internet is actually slow.

#### compare:
- Download Speed
- Upload Speed
- Ping(Latency)

If the speed is much lower than your internet plan, continue troubleshooting.

---
### 4. Check Network Usage
#### Open:
Task Manager --> Processes

#### or
Settings --> Network & Internet --> Data Usage

Applications may be consuming bandwidth,
examples:
- Windows Update
- OneDrive
- Steam
- Cloud backups
- Browser downloads



Close unnecessary applications if they are using significant network bandwidth.

---
### 5. Check IP Configuration
```cmd
ipconfig/all
```
verify that:
- The computer has valid IP address
- DNS servers are configured
- Default Gateway is present
An incorrect network configuration can affect internet performance.

---
### 6. Test Network Latency
```cmd
ping google.com
```
Measures the response time between your computer and Google's server.

#### Example:
```
Reply from 142.x.x.x
time=18ms
```

#### Generally:
- less than 30ms --> Excellent
- 30-70ms --> Good
- 70-150ms --> acceptable
- Above 150ms --> Slow connection

High latency often indicates network congestion or WI-FI issues.

---
### 7. Test Packet Loss
```cmd
ping google.com -n 20
```
Sends 20 packets instead of the default 4.
#### Look for:
```
Lost = 0
```
If packets are lost, the connection is unstable.

#### Possible causes:
- Weak WI-FI signal
- faulty cable
- Router problem
- ISP issue

---
### Flush DNS Cache
```cmd
ipconfig/flushdns
```
Removes outdated or corrupted DNS entries that can delay website loading.

---
### 9. Update Network Adapter Driver
Device Manager -> Network Adapters

An outdated or corrupted driver can reduce network performance or cause instability.

---
### 10. Check Windows Update
Windows may be downloading updates in the background and using a large portion of your bandwidth.

Pause updates temporarily if appropriate.

---
### 11. Test with another Device
Determine whether the problem is with:
- Your computer
- The WI-FI network
- The ISP

If all device are slow, the issue is likely with the router or ISP.

---
### 12. Contact the ISP
If all troubleshooting steps fail and multiple devices experience slow internet, the problem may be outside your local network.

---
## prevention
- Keep router firmware updated.
- Place the router in a central location.
- Limit unnecessary background downloads.
- Restart the router periodically.
- Keep network drivers updated.

---







