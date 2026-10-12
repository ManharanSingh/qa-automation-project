Windows Blue Screen (BSOD) Troubleshooting

1. Overview

A Blue Screen of Death (BSOD), also known as a stop error or bug check, occurs when Windows encounters a serious problem and stops or restarts to protect the system.

Possible causes include faulty drivers, incompatible software, hardware problems, memory errors, and operating system corruption.

This guide describes how to investigate blue screen errors, collect diagnostic evidence, identify possible causes, and verify corrective actions.

Platform: Windows 10 and Windows 11

Audience: IT Support Engineers and Help Desk Technicians

2. Common Symptoms

Users may report:

- Windows displays a blue screen and restarts.
- The computer crashes repeatedly during normal use.
- A stop code appears on the screen.
- Windows restarts when a particular application is used.
- The problem began after a driver or Windows update.
- The computer crashes during startup.
- The system becomes unstable after new hardware is installed.

Examples of stop codes include:

- "MEMORY_MANAGEMENT"
- "PAGE_FAULT_IN_NONPAGED_AREA"
- "IRQL_NOT_LESS_OR_EQUAL"
- "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED"
- "WHEA_UNCORRECTABLE_ERROR"

These codes provide diagnostic clues. A stop code alone does not necessarily identify the defective component.

3. Initial Information Gathering

Before changing anything, establish the circumstances surrounding the crash.

Ask the user:

- What exact stop code appeared?
- When did the crash begin?
- Does the computer crash repeatedly?
- Does the problem occur during startup or while using a particular application?
- Was new hardware connected recently?
- Was a driver, application, or Windows update installed?
- Does the computer restart successfully after the crash?
- Are important files backed up?

Record the stop code, any displayed "What failed" module name, the time of the crash, and any recent hardware or software changes.

If the computer is repeatedly crashing, prioritize protecting user data and collecting available diagnostic information.

4. Diagnostic Procedure

Step 1: Record the Stop Code

When the blue screen appears, record:

- The stop code.
- Any displayed module or file name.
- The time of the crash.
- The activity being performed immediately before the crash.

For example, a user may report that the system displays "MEMORY_MANAGEMENT" while working with several applications.

This information helps narrow the investigation, but the stop code should not be treated as a confirmed root cause.

Step 2: Determine Whether the Problem Is Reproducible

Establish whether the crashes happen:

- During startup.
- After signing in.
- When using a specific application.
- During intensive CPU, GPU, or memory workloads.
- After connecting a particular device.
- At apparently random times.

Check whether the crash began after a recent system change.

If the same activity consistently triggers the crash, document the steps that reproduce it. Do not repeatedly provoke a crash when doing so could cause data loss or damage an already unstable system.

Step 3: Inspect Reliability Monitor

Open Reliability Monitor by running:

perfmon /rel

Inspect the reliability timeline around the time of the crash.

Look for hardware errors, Windows failures, and application failures that coincide with the reported incident.

Record relevant details and the timing of recurring failures.

Interpretation:

Reliability Monitor can help identify when failures began and whether they correlate with recent changes. A recorded failure does not independently prove which component caused the crash.

Step 4: Inspect Event Viewer

Open Event Viewer:

eventvwr.msc

Navigate to:

Windows Logs → System

Review events around the time of the crash. Look for relevant bug-check, hardware, driver, or system events.

Record:

- Event source.
- Event ID.
- Timestamp.
- Error details.
- Any reported bug-check information.

A "Kernel-Power" event, including Event ID 41, can be recorded when Windows detects that the previous shutdown was not clean.

Important: A Kernel-Power event does not, by itself, establish the original cause of a crash. Correlate it with other available evidence.

Step 5: Check for Crash-Dump Files

Windows may create diagnostic dump files after a system crash, depending on its configuration and whether dump creation succeeds.

Common locations include:

C:\Windows\Minidump

and:

C:\Windows\MEMORY.DMP

Check whether a dump was created around the time of the incident.

Crash dumps can help identify the stop code, the state of the system, and possible driver or software involvement.

The presence of a dump file does not automatically establish the root cause. Advanced dump analysis may be required.

Security note: Memory dumps can contain sensitive information. Do not publish dump files or upload them to public repositories. Use approved analysis tools and organizational procedures.

Step 6: Investigate Recent Driver or Hardware Changes

If the problem began after a driver update or new hardware installation, investigate that change.

Open Device Manager:

devmgmt.msc

Inspect devices associated with the affected hardware or any components referenced in the diagnostic evidence.

Review driver versions, device status, and recent changes.

Where evidence supports it, consider an approved driver update or rollback. If new peripheral hardware appears related to the crashes, follow the manufacturer's safe removal instructions and organizational procedures before testing without it.

Do not update or remove every driver simply because the system has crashed.

Step 7: Test in Safe Mode When Appropriate

If normal Windows startup is unstable, Safe Mode can help investigate whether a third-party driver, service, or startup component contributes to the problem.

Access:

Windows Recovery Environment → Troubleshoot → Advanced options → Startup Settings → Restart

Select Enable Safe Mode after the restart.

For details, consult Microsoft's "Windows Startup Settings documentation" (https://support.microsoft.com/en-us/windows/experience/startup-boot/windows-startup-settings).

Interpretation:

- If the crashes stop in Safe Mode, investigate drivers, services, and components that are not loaded in the same way during normal startup.
- If the crashes continue, investigate other possible causes, including hardware and core operating system problems.

Safe Mode behavior is evidence for narrowing the investigation, not proof of a specific cause.

Step 8: Investigate Memory Errors

If the stop code or other evidence suggests a possible memory problem, consider Windows Memory Diagnostic.

Open the utility by running:

mdsched.exe

Review the available options and save all work before scheduling a test that restarts the computer.

After the diagnostic finishes, review the available results.

Interpretation:

- A reported memory error warrants further investigation.
- A test without reported errors does not rule out every intermittent memory or hardware fault.
- Memory-related stop codes can also result from software and driver problems.

Follow organizational procedures before running hardware diagnostics on a production computer.

Step 9: Investigate System Integrity When Indicated

If evidence points to Windows system-file corruption, consult:

"Windows System File and Repair Troubleshooting" (system-file-repair.md)

That guide covers DISM, SFC, and interpretation of repair results.

These utilities are appropriate for certain system integrity problems. They are not universal solutions for every blue screen.

5. Diagnostic Decision Table

Observation| Investigation direction
Crash began after a driver update| Investigate the affected driver and change history
Crash happens only during one activity| Investigate that workload, application, and related components
Repeated crashes show the same stop code| Correlate the code with logs, dump files, and recent changes
Computer crashes during startup| Use appropriate recovery tools and investigate boot-related evidence
Reliability Monitor records recurring failures| Compare failure times with system changes and other diagnostics
Memory diagnostic reports errors| Investigate memory and associated hardware using an approved process
Several devices fail after a system change| Investigate shared drivers, updates, or system-level changes
Available evidence suggests system-file corruption| Follow the documented system repair procedure

These observations guide further investigation; they do not independently prove the root cause.

6. Resolution

Choose corrective actions based on the diagnostic evidence.

Possible actions include:

- Applying an approved, compatible driver update.
- Rolling back a driver when a recent change is implicated and rollback is available.
- Removing or reconfiguring recently added hardware when evidence supports it.
- Applying appropriate Windows updates.
- Investigating memory or other hardware faults.
- Repairing Windows system files when indicated.
- Using Windows recovery options when startup remains unstable.
- Escalating recurring crashes for advanced dump analysis or hardware diagnostics.

Avoid reinstalling Windows, modifying the registry, changing firmware settings, or replacing hardware as an initial response without a justified diagnosis and recovery plan.

7. Verification

After applying a corrective action:

1. Restart Windows normally.
2. Reproduce the original activity only when safe.
3. Confirm whether the stop error returns.
4. Review reliability and event logs for recurring failures.
5. Check that the affected application and hardware work correctly.
6. Record the outcome and any remaining symptoms.

One successful restart does not prove that an intermittent crash has been permanently resolved. Verification should reflect the original failure pattern and available evidence.

8. Example Incident Record

Incident: A user reports recurring blue screen errors after a driver update.

Initial symptoms: Record the stop code, time of failure, activity being performed, and affected hardware.

Diagnostic evidence: Record relevant Reliability Monitor and Event Viewer findings, driver information, and available crash-dump results.

Root cause: Document only after the evidence supports a conclusion.

Resolution: Record the corrective action actually performed.

Verification: Record subsequent system behavior and whether the original crash can still be reproduced.

This is an incident template, not a claim that a real computer has been diagnosed or repaired.

9. Safety and Escalation

- Protect user data before performing higher-impact recovery operations.
- Do not repeatedly force crashes to reproduce an issue.
- Do not publish memory dumps or sensitive diagnostic logs.
- Use approved driver and hardware diagnostic sources.
- Follow organizational procedures before running invasive hardware tests.
- Escalate repeated unexplained crashes, suspected hardware failure, and cases requiring advanced dump analysis.

10. Key Learning Points

Blue screen troubleshooting is an evidence-driven process.

An effective IT Support Engineer records the stop code, establishes the circumstances of the crash, correlates the failure with logs and recent changes, and investigates possible driver, software, hardware, or system integrity problems.

The objective is to identify the most likely cause, apply a justified corrective action, and verify system stability.

---

Official Reference

Microsoft: "Troubleshooting Windows unexpected restarts and stop code errors" (https://support.microsoft.com/en-us/windows/experience/performance-optimization/troubleshooting-windows-unexpected-restarts-and-stop-code-errors)

---

Project: Windows Troubleshooting Guide
Platform: Windows 10 and Windows 11
Status: Initial documentation draft
