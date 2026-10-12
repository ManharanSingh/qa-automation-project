Windows Device Driver Troubleshooting

1. Overview

Device drivers allow Windows to communicate with hardware components and peripheral devices. A missing, incompatible, or malfunctioning driver can prevent a device from working correctly.

This guide explains how to investigate driver-related problems using Device Manager, PowerShell, Windows driver properties, and relevant event information.

Platform: Windows 10 and Windows 11

Audience: IT Support Engineers and Help Desk Technicians

2. Common Symptoms

Users may report:

- Wi-Fi or Ethernet is unavailable.
- No sound is produced by the computer.
- A USB device is not detected.
- A printer or scanner does not work correctly.
- A device displays a warning icon in Device Manager.
- Windows reports that a device cannot start.
- A device stopped working after a driver update.
- Windows cannot find a suitable driver for newly connected hardware.
- A device repeatedly disconnects or behaves unpredictably.

These symptoms do not always indicate a driver problem. Hardware faults, cables, power issues, configuration errors, and application problems can produce similar symptoms.

3. Initial Information Gathering

Before changing a driver, establish the scope of the incident.

Ask the user:

- Which device is affected?
- When did the problem begin?
- Does the device appear in Device Manager?
- Is there an error code or warning icon?
- Did Windows Update or a driver installation recently occur?
- Does the problem affect one computer or multiple computers?
- Is the device connected internally, through USB, or over a network?
- Does the manufacturer provide a diagnostic utility?

Record the device name, model where available, Windows version, error details, and recent changes.

4. Diagnostic Procedure

Step 1: Check the Physical Device

Before investigating Windows drivers, inspect the device and its connection.

Examples:

- Check that a USB device is connected properly.
- Check the cable and port when investigating an external device.
- Check the physical Wi-Fi switch or airplane mode setting where applicable.
- Confirm that an external device has power.
- Check whether the hardware displays an error indicator.

If appropriate, test the device using another known-good port or cable.

Interpretation:

If the device is not receiving power or has a physical connection problem, changing its driver may not resolve the issue.

Avoid unnecessary hardware changes before recording the initial symptoms.

Step 2: Inspect Device Manager

Open Device Manager using:

devmgmt.msc

Inspect the category corresponding to the affected hardware.

Look for:

- A yellow warning icon.
- An unknown device.
- A device that is missing from its expected category.
- A disabled device.
- A device that displays an error in its properties.

Open the device's Properties window and inspect the General tab for its device status.

If Windows displays an error code, record the code and accompanying message.

Interpretation:

A warning icon can indicate a device configuration or driver-related problem, but the exact message and error code should guide the investigation.

A missing device may result from a physical connection issue, disabled hardware, firmware configuration, or a detection problem—not simply a missing driver.

Step 3: Identify the Device and Driver

In Device Manager, open the device's Properties window.

Inspect the Driver tab for available information, such as:

- Driver provider.
- Driver date.
- Driver version.
- Digital signer, where displayed.

Where appropriate, inspect the Details tab and select Hardware Ids from the property list.

Hardware IDs can help identify a device when its displayed name is unfamiliar.

Do not assume that the newest available driver is always the correct one. Driver compatibility with the device, Windows version, and hardware revision matters.

Step 4: Inspect Device Information with PowerShell

On supported Windows installations, open PowerShell and run:

Get-PnpDevice -PresentOnly |
    Select-Object Status, Class, FriendlyName, InstanceId

This lists detected Plug and Play devices with selected identifying information.

To investigate a particular device, filter the output by a known part of its display name:

Get-PnpDevice -PresentOnly |
    Where-Object {
        $_.FriendlyName -like "*Wi-Fi*"
    } |
    Select-Object Status, Class, FriendlyName, InstanceId

Replace "Wi-Fi" with a suitable part of the device's actual name.

Interpretation:

- "FriendlyName" is the displayed device name.
- "Class" identifies the device category.
- "InstanceId" identifies a particular device instance.
- "Status" provides the device status reported by Windows.

The exact device name and reported status depend on the hardware and driver. If no device appears, broaden the search rather than concluding that the hardware is defective.

Step 5: Review Driver Installation History

Determine whether the issue began after a driver update, Windows update, or hardware change.

In Device Manager, inspect the driver's version and date and compare them with the known timeline of the incident.

Check Windows Update history or the organization's software deployment records when relevant.

Interpretation:

If the issue began immediately after a driver change, that change is a reasonable investigation target. However, timing alone does not establish causation.

Record the previous driver version if available before making further changes.

Step 6: Check for Relevant Errors

Open Event Viewer:

eventvwr.msc

Inspect relevant entries under Windows Logs → System and any applicable device or driver diagnostic logs available on the computer.

Correlate the event timestamps with the time the device stopped working.

Record:

- Event source and ID.
- Timestamp.
- Device or driver name, where available.
- Error message.
- Any referenced failure code.

Do not assume that every warning or error in Event Viewer is related to the reported device problem. Focus on evidence that correlates with the symptoms.

5. Diagnostic Decision Table

Observation| Investigation direction
Device has a warning icon| Inspect its status message and error code
Device appears as Unknown device| Investigate its hardware IDs and identify the device
Device is missing from Device Manager| Check physical connection, power, firmware configuration, and device detection
Device stopped working after a driver change| Investigate the driver change and compatibility
Device is disabled| Verify why it was disabled before changing its state
Multiple devices fail after an update| Investigate shared system changes and relevant update history
Device appears normal but still fails| Investigate hardware, applications, settings, services, and the device's expected behavior

These observations guide further investigation; they do not independently establish the root cause.

6. Resolution

Select corrective actions based on the collected evidence.

Possible actions include:

- Correcting a physical connection or power issue.
- Enabling a device that was intentionally or unintentionally disabled, where authorized.
- Installing a compatible driver from Windows Update or an approved hardware manufacturer source.
- Using Device Manager's supported driver update or reinstall options.
- Rolling back a driver when evidence indicates that a recent update caused the problem and rollback is available.
- Escalating suspected hardware failure or firmware compatibility problems.

Before changing a driver:

1. Confirm the exact device model.
2. Confirm compatibility with the installed Windows version.
3. Use an approved, trusted driver source.
4. Follow organizational software installation procedures.
5. Record the current driver information when possible.

Do not use random third-party driver download sites or driver updater utilities. Do not remove a working network adapter driver unless you have a suitable recovery method if network connectivity is lost.

7. Verification

After applying a corrective action:

1. Check the device's status in Device Manager.
2. Confirm that the relevant warning or error has been resolved, where applicable.
3. Test the actual device function.
4. Restart the computer if required by the installation procedure.
5. Confirm that the device continues to work after restarting, where appropriate.
6. Ask the user to verify that the original task works.
7. Record the result and any remaining symptoms.

A driver appearing correctly installed does not prove that the hardware works properly. Test the actual function that initially failed.

Examples:

- For Wi-Fi, verify connection to the expected network.
- For audio, test playback and the intended output device.
- For USB hardware, test the required operation.
- For a printer, perform an appropriate test print.

8. Example Incident Record

Incident: User reports that Wi-Fi stopped working after a recent update.

Initial symptoms: Record the device, connection behavior, warning messages, and approximate time the problem began.

Diagnostic evidence: Record Device Manager status, driver provider and version, relevant update history, and any correlated error logs.

Root cause: Document only when the evidence supports a conclusion.

Resolution: Record the corrective action actually performed.

Verification: Confirm that the adapter works and the user can connect to the expected network.

This is an incident template, not a claim that a real device has been diagnosed or repaired.

9. Safety and Escalation

- Avoid unnecessary driver removal.
- Use trusted and approved driver sources.
- Do not bypass device security or organizational installation controls.
- Protect device identifiers and internal system information in published logs.
- Preserve a recovery path before changing critical network or storage drivers.
- Follow organizational change procedures.
- Escalate suspected hardware faults, firmware issues, or repeated driver crashes when further expertise is required.

10. Key Learning Points

Device troubleshooting should distinguish between hardware detection, driver configuration, and actual device functionality.

An effective IT Support Engineer gathers the device's status and error information, investigates recent changes, chooses a compatible corrective action, and tests the original function after the change.

A driver problem should be established through evidence rather than assumed from the symptoms alone.

---

Project: Windows Troubleshooting Guide
Platform: Windows 10 and Windows 11
Status: Initial documentation draft
