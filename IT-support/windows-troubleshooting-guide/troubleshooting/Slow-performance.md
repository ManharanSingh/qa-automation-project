Windows Slow Performance Troubleshooting

1. Overview

This guide describes how to investigate slow Windows performance using built-in diagnostic tools and PowerShell.

The objective is to identify resource bottlenecks, investigate possible causes, apply an appropriate corrective action, and verify whether performance improves.

Platform: Windows 10 and Windows 11

Audience: IT Support Engineers and Help Desk Technicians

2. Common Symptoms

Users may report:

- Windows takes a long time to start.
- Applications open slowly.
- The computer freezes or becomes unresponsive.
- The mouse or keyboard responds with a delay.
- CPU usage remains unusually high.
- Available memory is low.
- Disk activity remains unusually high.
- Performance deteriorates after opening multiple applications.

3. Initial Information Gathering

Before making changes, establish the scope of the problem.

Ask the user:

- When did the slowdown begin?
- Is the computer slow immediately after startup or only during certain tasks?
- Does the problem affect one application or the entire system?
- Did the user recently install software, drivers, or updates?
- Does the slowdown occur consistently or intermittently?
- How much free storage space is available?

Record the symptoms and any recent changes.

4. Diagnostic Procedure

Step 1: Inspect Resource Usage

Open Task Manager using:

"Ctrl + Shift + Esc"

Select the Processes tab and review:

- CPU
- Memory
- Disk
- Network

Sort each column to identify processes consuming significant resources.

Interpretation:

- High CPU usage may indicate intensive computation, a malfunctioning application, or a background task.
- High memory usage may indicate memory pressure caused by applications or background processes.
- High disk activity may indicate heavy file operations, updates, indexing, or storage-related problems.
- High network usage may indicate downloads, synchronization, or other network activity.

A high value is not automatically evidence of a fault. Determine which process is responsible and whether the usage is sustained and unusual for the workload.

Step 2: Investigate CPU Usage with PowerShell

Open PowerShell and run:

Get-Process |
    Sort-Object CPU -Descending |
    Select-Object -First 10 Name, Id, CPU

This lists processes with the highest accumulated CPU time among the returned process objects.

Important: The "CPU" property represents accumulated processor time in seconds, not the current CPU usage percentage. A process with a high value may have been running for a long time.

Use Task Manager or Performance Monitor to investigate current CPU utilization.

Step 3: Investigate Memory Consumption

Run:

Get-Process |
    Sort-Object WorkingSet64 -Descending |
    Select-Object -First 10 Name, Id, WorkingSet64

The "WorkingSet64" property reports the amount of physical memory currently in a process's working set, in bytes.

Interpretation:

- A large working set identifies a process using substantial physical memory.
- Multiple processes can collectively create memory pressure.
- High memory consumption alone does not prove a memory leak.

If needed, compare the results with Task Manager's overall memory usage and available memory.

Step 4: Check Available Storage

Open File Explorer, select This PC, and inspect the free space on the Windows drive.

Alternatively, use PowerShell:

Get-Volume |
    Select-Object DriveLetter, FileSystemLabel,
        @{Name="SizeGB";Expression={[math]::Round($_.Size / 1GB, 2)}},
        @{Name="FreeGB";Expression={[math]::Round($_.SizeRemaining / 1GB, 2)}}

Interpretation:

- Very low free space can interfere with updates, temporary files, and normal system operations.
- Adequate free space does not rule out a storage performance problem.

Do not delete system files simply to free storage. Identify safe cleanup opportunities first.

Step 5: Review Startup Applications

Open Task Manager and select Startup apps.

Review applications that launch automatically when the user signs in.

Investigate applications that are unnecessary for the user's work and have a meaningful startup impact.

Disable a startup application only after confirming that it is not required for security, management, or business operations.

Step 6: Check for Relevant Errors

Open Event Viewer by running:

eventvwr.msc

Inspect relevant entries under Windows Logs → System and Windows Logs → Application around the time the slowdown occurred.

Look for repeated errors that correlate with the reported symptoms.

Interpretation:

An event's severity alone does not establish the cause of a performance issue. Correlate its timestamp, source, details, and recurrence with other evidence.

5. Diagnostic Decision Table

Observation| Investigation direction
Sustained high CPU usage| Identify the process and investigate its workload or errors
Memory usage remains high| Inspect process memory consumption and overall memory pressure
Disk activity remains high| Investigate active processes, storage response, and disk health where appropriate
Windows drive has very little free space| Identify safe cleanup opportunities and review storage requirements
Slow startup| Investigate startup applications, services, updates, and relevant events
Only one application is slow| Investigate that application, its dependencies, and its resource usage
Slowdown began after a change| Investigate the recent change and its relationship to the symptoms

These observations guide further investigation; they do not independently establish a root cause.

6. Resolution

Choose corrective actions based on the evidence.

Possible actions include:

- Close unnecessary applications after confirming that their work can be safely stopped.
- Restart an unresponsive application when appropriate.
- Reduce unnecessary startup applications.
- Free storage using approved Windows cleanup tools.
- Apply approved application or Windows updates.
- Escalate suspected hardware, driver, or storage failures for further investigation.

Do not terminate unknown processes, disable security software, or change system services merely because they consume resources.

7. Verification

After applying a corrective action:

1. Repeat the relevant resource-usage checks.
2. Reproduce the task that was previously slow.
3. Confirm that the affected application responds normally.
4. Check whether the original symptoms persist.
5. Record the before-and-after observations.

A successful resolution should be supported by measurable results or confirmation from the affected user.

8. Example Incident Record

Incident: User reports that the computer becomes slow after signing in.

Initial observations: Record the affected applications, startup behavior, and resource usage.

Diagnostic evidence: Record relevant CPU, memory, disk, startup, and event-log findings.

Root cause: Document only after sufficient evidence supports the conclusion.

Resolution: Record the corrective action actually performed.

Verification: Record the subsequent measurements and the user's confirmation.

This is an incident template, not a claim that a real computer has been tested or repaired.

9. Safety and Escalation

- Begin with observation and non-invasive diagnostics.
- Do not terminate unfamiliar processes without understanding their purpose.
- Avoid deleting files from Windows system directories.
- Protect sensitive information in screenshots and logs.
- Escalate suspected hardware faults, recurring system crashes, or unexplained resource exhaustion when further investigation is required.

10. Key Learning Points

Windows performance troubleshooting requires more than identifying the process with the highest resource usage.

An effective IT Support Engineer correlates user symptoms with system measurements, investigates the likely cause, applies a justified correction, and verifies the outcome.

---

Project: Windows Troubleshooting Guide
Platform: Windows 10 and Windows 11
Status: Initial documentation draft
