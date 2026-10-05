# Active Directory Home Lab

## Overview

This project is my hands-on Active Directory lab built to understand how Windows domains are actually managed from an IT Support perspective.

I built the environment in a virtual machine using Windows Server 2025. Instead of only reading about Active Directory, I used the lab to practice common help-desk and junior system administration tasks such as creating users, organizing OUs, managing groups, applying security policies, resetting passwords, unlocking accounts, and working with file permissions.

The main goal of this project is simple: **learn how an IT support engineer would actually manage and troubleshoot users and computers in a Windows domain.**

---

## Lab Environment

| Component | Details |
|---|---|
| Server OS | Windows Server 2025 |
| Role | Active Directory Domain Services (AD DS) |
| Domain | `adlab.test` |
| NetBIOS name | `ADLAB` |
| Virtualization | VMware |
| Domain Controller | `DC01` |
| Client machines | Planned for a later stage |

> This is a learning environment, not a production Active Directory deployment.

---

## What I Built

I started with a normal Windows Server virtual machine and promoted it to a Domain Controller by installing and configuring **Active Directory Domain Services (AD DS)**.

After promotion, I created my test domain and started building an organizational structure that represents a small company.

The basic structure looks like this:

```text
ADLAB (Domain)
└── TechCorp (OU)
    ├── Users (OU)
    │   ├── Alice
    │   └── Bob
    │
    ├── Groups (OU)
    │   ├── IT
    │   ├── HR
    │   └── Finance
    │
    └── Computers (OU)
        ├── Servers (OU)
        └── Workstations (OU)
```

The idea behind this structure is to keep objects organized instead of leaving everything in the default containers.

---

# 1. Installing and Promoting the Server

The first step was preparing Windows Server for Active Directory.

I installed the **Active Directory Domain Services** role and then promoted the server to a Domain Controller.

During the promotion process I configured:

- A new Active Directory forest
- The domain name `adlab.test`
- NetBIOS name `ADLAB`
- DNS as part of the domain controller setup
- A Directory Services Restore Mode (DSRM) password

After promotion, the server restarted and became the Domain Controller for the lab.

### What I learned

A Windows Server machine does not automatically become a Domain Controller just because AD DS is installed. The server has to be promoted into the domain/forest, after which Active Directory and related services such as DNS become part of the domain infrastructure.

---

# 2. Creating the Organizational Unit Structure

After the domain was working, I created an OU called **TechCorp**.

Inside TechCorp I created separate OUs for:

- Users
- Groups
- Computers

I then created additional OUs under Computers for:

- Servers
- Workstations

This gave me a basic structure that resembles how a real organization might separate different types of objects.

### Why OUs matter

OUs are useful for more than organization. They also provide a place where **Group Policy Objects (GPOs)** can be linked and where administrative control can be delegated.

For example, a company could apply one policy to workstations and a different policy to servers.

---

# 3. Creating Users

I created test user accounts such as:

- `Alice`
- `Bob`

These accounts were used to practice normal user-management tasks.

The purpose was to understand what an IT support engineer may need to do when a user reports an account or login problem.

### User-management tasks practiced

- Creating user accounts
- Organizing users inside the correct OU
- Adding users to security groups
- Resetting a user's password
- Unlocking a locked account
- Working with account lockout behavior

---

# 4. Creating Department Groups

I created groups representing different departments:

- IT
- HR
- Finance

The idea was to manage access through groups rather than assigning permissions independently to every user.

For example:

```text
IT Group
├── Alice
└── Bob
```

A real organization could then assign permissions to the IT group instead of manually configuring access for Alice and Bob one by one.

This introduced me to an important Active Directory principle:

> **Manage access through groups whenever possible.**

---

# 5. Account Lockout Policy

I practiced configuring an **account lockout policy**.

The purpose of this policy is to help protect domain accounts from repeated failed authentication attempts.

The policy can control things such as:

- Account lockout threshold
- Account lockout duration
- Resetting the failed-attempt counter

I also tested the practical side of the policy by working with locked accounts.

### Support scenario

A user says:

> "I know my password is correct, but Windows says my account is locked."

An IT support engineer would need to identify whether the account is actually locked and then unlock it according to the organization's procedures.

I practiced this type of task in the lab.

---

# 6. Password Reset Practice

I practiced resetting a user's domain password from Active Directory Users and Computers.

This is one of the common support tasks in a Windows domain environment.

Typical support workflow:

```text
User reports login problem
        ↓
Verify the user account
        ↓
Check whether the account is locked/disabled
        ↓
Reset password if required
        ↓
Unlock account if required
        ↓
Test authentication
```

A production environment would also require following the company's identity-verification procedure before resetting another person's password.

---

# 7. Group Policy Practice

I also started working with **Group Policy**.

I practiced understanding how GPOs are linked to organizational locations and how a policy can affect computers or users in an OU.

For example, I worked with a workstation security policy and observed the relationship between:

```text
Domain
  ↓
OU
  ↓
GPO Link
  ↓
User / Computer
  ↓
Policy Applied
```

I also practiced moving a GPO link to the appropriate workstation OU and removing an unnecessary link from the higher-level OU.

The main lesson was that **creating a GPO is not enough**. The location where the GPO is linked matters.

---

# 8. File and Folder Permissions Practice

I also practiced Windows file permissions using Active Directory security groups.

Example lab folder:

```text
C:\CompanyData\IT
```

I created a security rule that gave the following group access:

```text
ADLAB\IT-Support
```

Permission used:

```text
Modify
```

The permission was configured to inherit to files and subfolders.

The idea was to simulate a real company file-share permission model where access is granted to a department group instead of individual users.

### Example

```text
IT-Support Group
        ↓
C:\CompanyData\IT
        ↓
Modify permission
        ↓
Members inherit access
```

This helped me connect **Active Directory groups** with **Windows NTFS permissions**.

---

# 9. Concepts I Practiced

During the lab I worked with the following Active Directory concepts:

### Domain

The domain provides a central identity and management boundary for users, computers, groups, and policies.

### Domain Controller

The Domain Controller is the Windows Server responsible for Active Directory authentication and directory services.

### Active Directory Domain Services

AD DS stores and manages directory objects such as users, groups, and computers and provides authentication for the domain.

### Organizational Unit

OUs are containers used to organize objects and provide a scope where policies and administrative delegation can be applied.

### Security Group

Security groups are used to manage permissions and access for multiple users or computers.

### Group Policy

Group Policy provides centralized configuration and security settings for domain users and computers.

### DNS

DNS is an important part of a Windows Active Directory environment because domain clients use DNS to locate domain services.

---

# 10. IT Support Scenarios Practiced

I used the lab to think about Active Directory from a support engineer's point of view rather than only learning definitions.

### Scenario 1 - User cannot log in

Things to check:

1. Is the username correct?
2. Is the account disabled?
3. Is the account locked?
4. Has the password expired?
5. Is the computer connected to the domain network?
6. Is DNS working correctly?
7. Can the client communicate with the Domain Controller?

### Scenario 2 - User forgot the password

Typical support action:

```text
Verify user
   ↓
Reset password
   ↓
Unlock account if necessary
   ↓
Test login
```

### Scenario 3 - User belongs to the wrong department

Instead of giving individual permissions manually, the user's group membership should be reviewed and corrected.

### Scenario 4 - User cannot access a company folder

Check:

- Active Directory group membership
- NTFS permissions
- Share permissions (when using a network share)
- Inheritance
- Whether the user is actually authenticating with the domain account

### Scenario 5 - Computer receives the wrong policy

Check:

- Which OU contains the computer
- Which GPOs are linked to that OU
- GPO inheritance
- Security filtering
- Whether the policy has refreshed on the client

---

# 11. Troubleshooting Knowledge I Am Building

The lab is also helping me connect different parts of Windows infrastructure.

For example, an Active Directory login problem may not actually be caused by the user account.

It could be:

```text
User
 ↓
Windows Client
 ↓
Network
 ↓
DNS
 ↓
Domain Controller
 ↓
Active Directory
```

A problem anywhere in that chain can cause authentication or access issues.

This is important from an IT support perspective because troubleshooting should not immediately assume that the account itself is broken.

---

# 12. Next Practice Tasks

These are the parts I plan to practice next as I continue expanding the lab.

## Active Directory Administration

- Create and remove users
- Enable and disable accounts
- Move users between OUs
- Create, rename, and delete groups
- Add and remove group members
- Compare security groups and distribution groups
- Practice group scopes
- Practice nested group membership
- Find inactive or disabled accounts
- Review user account properties
- Set account expiration dates
- Configure password-related settings
- Understand password policy inheritance

## Computer Management

- Join a Windows client to the domain
- Move computers into the correct OU
- Rename a domain computer
- Remove a computer from the domain
- Disable an old computer account
- Re-enable a computer account
- Troubleshoot a failed domain join
- Test domain login from a client

## Group Policy

- Create GPOs
- Link GPOs to specific OUs
- Configure password policies
- Configure workstation security settings
- Apply user policies
- Apply computer policies
- Learn GPO inheritance
- Learn block inheritance
- Learn enforced GPOs
- Understand security filtering
- Use `gpupdate`
- Use `gpresult` to troubleshoot policy application

## File Access

- Create shared folders
- Configure share permissions
- Compare share permissions with NTFS permissions
- Test access using different domain users
- Practice least-privilege access
- Create department-based file permissions

## Help Desk / Troubleshooting

- Locked account troubleshooting
- Password reset workflow
- Disabled-account troubleshooting
- Domain login troubleshooting
- DNS-related authentication problems
- Domain join troubleshooting
- GPO troubleshooting
- Permission troubleshooting
- User profile troubleshooting
- Basic event-log investigation

## PowerShell

Later I also plan to automate common Active Directory support tasks using PowerShell, such as:

```powershell
Get-ADUser
Get-ADGroup
Get-ADComputer
Add-ADGroupMember
Unlock-ADAccount
Set-ADUser
```

The goal is to move from doing tasks manually in the GUI to understanding how the same work can be performed through PowerShell.

---

# 13. Planned Lab Architecture

When the laptop resources allow it, I plan to add a Windows client VM.

The expanded lab will look roughly like this:

```text
                 Windows Server 2025
                       DC01
                        │
             ┌──────────┴──────────┐
             │                     │
       Active Directory          DNS
             │
             │
        adlab.test
             │
      ┌──────┴──────┐
      │             │
 Users/Groups    Computers
                    │
              ┌─────┴─────┐
              │           │
         Workstations   Servers
              │
         Windows Client
```

The client machine will allow me to test the environment more realistically because I will be able to join a workstation to the domain, log in as different users, receive GPOs, and test permissions from an actual domain client.

---

# 14. What I Learned From This Project

The biggest thing I learned is that Active Directory is not just about creating users.

It connects several pieces of Windows infrastructure together:

```text
Users
  +
Groups
  +
Computers
  +
OUs
  +
Group Policy
  +
DNS
  +
Permissions
        ↓
Centralized Windows management
```

I also learned that many common IT support problems can be investigated through a combination of **identity, policy, networking, and permissions**.

For me, the most useful part of the lab was being able to make changes, break things intentionally, and then troubleshoot them instead of only reading theory.

---

# 15. Skills Demonstrated

This project currently demonstrates hands-on practice with:

- Windows Server 2025
- Active Directory Domain Services
- Domain Controller setup
- DNS fundamentals in an AD environment
- Organizational Units
- User account management
- Security groups
- Group membership
- Account lockout policies
- Password reset procedures
- Unlocking user accounts
- Group Policy fundamentals
- NTFS permissions
- Permission inheritance
- Department-based access control
- Basic Windows authentication troubleshooting
- Basic IT support troubleshooting methodology

---

# 16. Screenshots

I will add screenshots here as the lab grows.

Suggested screenshots:

- Domain Controller / Server Manager
- Active Directory Users and Computers
- TechCorp OU structure
- Users OU
- Groups OU
- Computers OU
- Example user account
- Group membership
- Account lockout policy
- GPO configuration
- File permissions
- PowerShell / command-line testing
- Domain-joined Windows client

---

# Conclusion

This Active Directory lab is a work in progress. I built it to develop practical Windows administration and IT support skills rather than simply memorizing Active Directory terminology.

I started with one Windows Server, promoted it to a Domain Controller, created a test domain, organized users and computers into OUs, created department groups, practiced account management, tested lockout and password-reset scenarios, worked with Group Policy, and connected Active Directory groups with Windows file permissions.

The next stage is to add a domain-joined Windows client and use the environment to practice realistic support and troubleshooting scenarios.

**Lab status: In progress**
