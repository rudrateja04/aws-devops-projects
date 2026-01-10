# Project 02: EC2 with EBS Persistence

## About This Project
In this project, I worked with Amazon EC2 and Amazon EBS to understand how
persistent storage works in AWS.

I attached an additional EBS volume to an EC2 instance, mounted it,
stored data on it, rebooted the instance, and verified that the data
was still available. I also created an EBS snapshot as a backup.

---

## AWS Services Used
- Amazon EC2
- Amazon EBS
- EBS Snapshots
- AWS IAM
- Security Groups

---

## What I Did
1. Launched an EC2 instance using Amazon Linux
2. Created and attached an EBS volume to the EC2 instance
3. Mounted the EBS volume to /mnt/mybackup
4. Created a file on the mounted volume
5. Rebooted the EC2 instance
6. Verified that the file still existed after reboot
7. Created an EBS snapshot for backup

All commands used are available in commands.txt.  
Screenshots of each step are available in the screenshots folder.

---

## Result
The data stored on the EBS volume remained intact even after rebooting
the EC2 instance. This confirms that EBS provides persistent storage
independent of the EC2 lifecycle.

---

## What I Learned
- How to attach and mount EBS volumes
- Difference between EC2 lifecycle and EBS lifecycle
- How data persistence works in AWS
- How to create backups using EBS snapshots

---

## Cleanup
After completing the project, all resources were stopped or terminated
to avoid unnecessary AWS charges.

---

## Author
Rudra Teja
