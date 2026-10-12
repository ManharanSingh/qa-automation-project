# Network Connectivity Troubleshooting — Windows

## 1. Overview

This guide provides a structured procedure for diagnosing network connectivity problems on Windows 10 and Windows 11 computers.

It covers network configuration, local network connectivity, external IP connectivity, DNS resolution, and basic TCP port testing.

**Audience:** IT Support Engineers and Help Desk Technicians

**Scope:** Windows client network troubleshooting

## 2. Common Symptoms

- The computer reports "No Internet."
- Websites do not load.
- The computer cannot reach other devices on the local network.
- Websites fail by hostname but may work by IP address.
- Some network services work while others fail.
- The computer has an invalid or unexpected IP configuration.

## 3. Initial Information Gathering

Before changing any settings, establish the scope of the incident.

Ask the user:

- When did the issue begin?
- Is the problem affecting one application, one website, or all network activity?
- Are other devices on the same network affected?
- Is the computer connected through Wi-Fi or Ethernet?
- Is a VPN currently connected?
- Were any network, application, or system settings recently changed?

Record relevant details, including the affected device, network connection type, error messages, and troubleshooting results.

## 4. Diagnostic Procedure

### Step 1: Check the Network Connection

Verify that the Ethernet cable is connected or that the computer is associated with the correct Wi-Fi network.

Check the Windows network status and look for visible warnings.

Do not assume that a connected Wi-Fi icon proves internet access. A device can connect to a local network without having working internet connectivity.

### Step 2: Inspect the IP Configuration

Open Command Prompt and run:

```cmd
ipconfig /all
```

Review the active network adapter and identify:

- IPv4 address
- Subnet mask
- Default gateway
- DNS servers
- DHCP status

**Interpretation:**

- An IPv4 address beginning with `169.254` often indicates that Windows did not obtain an IPv4 address from a DHCP server.
- A missing default gateway may prevent access to other networks.
- An incorrect DNS server may prevent hostname resolution.
- A valid IP configuration does not automatically prove that the network or internet is working.

Record the results before changing the configuration.

### Step 3: Test the Local TCP/IP Stack

Run:

```cmd
ping 127.0.0.1
```

This tests the computer's local IPv4 loopback path.

**Interpretation:**

A successful response indicates that the local TCP/IP stack can respond to the loopback test. It does not verify the physical network adapter, Wi-Fi connection, router, or internet access.

### Step 4: Test the Default Gateway

Use `ipconfig` to identify the **Default Gateway** address.

Run the following command, replacing the example address with the gateway shown on the affected computer:

```cmd
ping 192.168.1.1
```

**Interpretation:**

- A successful response indicates that the gateway responded to ICMP echo requests.
- A timeout does not always prove that the gateway is unreachable; ICMP traffic may be blocked.
- If the gateway cannot be reached, investigate the local connection, IP configuration, VLAN, wireless access point, or gateway before moving to external connectivity tests.

### Step 5: Test External IP Connectivity

Run:

```cmd
ping 1.1.1.1
```

This tests whether the computer can receive ICMP replies from a public IP address.

**Interpretation:**

- A successful response confirms reachability to that IP address using ICMP at the time of the test.
- A timeout may indicate a connectivity issue, but the destination or a firewall may simply block ICMP.
- A successful ping does not prove that DNS resolution, HTTPS, or every internet service is working.

Use other appropriate tests when ICMP is blocked or when an application-specific issue is suspected.

### Step 6: Test DNS Resolution

Run:

```cmd
nslookup www.microsoft.com
```

Review the DNS server displayed in the output and whether the hostname resolves to an IP address.

**Interpretation:**

- A returned IP address indicates that the DNS query received a usable answer.
- A timeout or resolution error may indicate a DNS server, network, policy, or configuration problem.
- Successful resolution does not prove that the website is reachable over HTTPS.

On a corporate network, do not replace the configured DNS servers with public DNS servers without authorization. Internal systems may depend on the organization's DNS configuration.

### Step 7: Test TCP Connectivity to HTTPS

Open PowerShell and run:

```powershell
Test-NetConnection www.microsoft.com -Port 443
```

Review the `TcpTestSucceeded` value and the destination address.

**Interpretation:**

- `TcpTestSucceeded : True` indicates that a TCP connection to the destination on port 443 was established.
- `TcpTestSucceeded : False` means the connection was not established. Possible causes include DNS failure, routing issues, firewall rules, proxy requirements, or a destination service problem.

This test does not verify the entire browser session or prove that all HTTPS websites are accessible.

## 5. Diagnostic Decision Table

| Observation | Possible direction for investigation |
|---|---|
| IPv4 address starts with `169.254` | Investigate DHCP and network configuration |
| Gateway is missing | Check adapter configuration and DHCP settings |
| Gateway does not respond | Check local connectivity and gateway reachability; consider ICMP filtering |
| Public IP ping succeeds but hostname resolution fails | Investigate DNS resolution |
| DNS resolves but TCP port 443 fails | Investigate routing, firewall, proxy, and destination service |
| Only one application fails | Investigate application-specific settings and dependencies |
| Multiple devices are affected | Investigate shared network infrastructure or service outages |

These observations narrow down possible causes; they do not independently establish the root cause.

## 6. Resolution and Verification

Choose a corrective action based on the diagnostic evidence.

Examples include:

- Reconnect to the correct Wi-Fi network or reseat the Ethernet cable.
- Correct a confirmed IP configuration issue using the organization's approved procedure.
- Escalate a suspected DHCP, DNS, gateway, or firewall problem to the responsible team.
- Correct application-specific network settings when supported by evidence.

Avoid resetting the network stack or changing DNS settings as a first response without a reason.

After a corrective action:

1. Repeat the relevant failed diagnostic test.
2. Confirm that the original application or resource works.
3. Ask the user to verify normal operation.
4. Document the action taken and the outcome.

## 7. Example Incident Record

**Incident:** User reports that websites do not load.

**Initial evidence:** To be completed using actual diagnostic results.

**Tests performed:** Record the IP configuration, gateway test, external reachability test, DNS query, and relevant TCP connectivity test.

**Root cause:** Do not assign a root cause until the evidence supports it.

**Resolution:** Document the actual corrective action taken.

**Verification:** Record which tests passed and whether the user confirmed the service was restored.

*This example is a template, not a claim that an incident has been tested or resolved.*

## 8. Safety and Escalation

- Start with diagnostic commands before making configuration changes.
- Do not share public screenshots containing internal IP details, hostnames, usernames, or other sensitive network information without reviewing them.
- Do not disable firewalls or endpoint security as a routine troubleshooting step.
- Follow organizational change and escalation procedures.
- Escalate when the issue requires access or permissions that the technician does not have.

## 9. Key Learning Points

Effective network troubleshooting separates several distinct questions:

- Does the computer have a valid network configuration?
- Can it reach its local gateway?
- Can it reach an external destination?
- Can DNS resolve a hostname?
- Can the required application port be reached?

**A good troubleshooting process uses evidence to narrow down the cause, applies a justified fix, and verifies the result.**

---

**Project:** Windows Troubleshooting Guide  
**Platform:** Windows 10 and Windows 11  
