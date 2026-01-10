# 📦 Project 02: EC2 + EBS Persistence & Snapshot

## 📌 Project Overview
This project demonstrates how to attach an Amazon EBS volume to an EC2 instance, mount it on the operating system, verify data persistence after a reboot, and create an EBS snapshot for backup and recovery.

The objective is to understand **persistent storage, data durability, and backup mechanisms** in AWS.

---

## 🛠️ AWS Services Used
- Amazon EC2
- Amazon EBS
- EBS Snapshots
- AWS IAM
- Security Groups

---

## 🏗️ Architecture
EC2 Instance  
↳ Attached EBS Volume  
↳ Mounted at `/mnt/mybackup`  
↳ Snapshot stored and managed by AWS  

---

## ⚙️ Implementation Summary

### 1️⃣ EC2 Instance Setup
- Launched an EC2 instance using **Amazon Linux 2023**
- Instance type: **t3.micro**
- Connected securely using SSH key-based authentication
- Security Group allows:
  - SSH (port 22)
  - HTTP (port 80)

📸 Screenshot:  
`screenshots/ebs-volume-attached-to-ec2.png`

---

### 2️⃣ EBS Volume Attachment
- Created an EBS volume in the same Availability Zone as the EC2 instance
- Attached the volume to the running EC2 instance
- Verified the new disk using `lsblk`

📸 Screenshot:  
`screenshots/lsblk-showing-ebs-disk.png`

---

### 3️⃣ Mounting the EBS Volume
- Created a mount directory `/mnt/mybackup`
- Mounted the EBS volume to the directory
- Verified successful mount using `df -h`

📸 Screenshot:  
`screenshots/ebs-mounted-at-mnt-mybackup.png`

📄 All commands used in this project are documented in **`commands.txt`**

---

### 4️⃣ Persistence Test (Core Objective)
- Created a test file on the mounted EBS volume
- Rebooted the EC2 instance
- Verified that the file still existed after reboot

📸 Screenshot:  
`screenshots/file-exists-after-reboot.png`

✅ This confirms that **EBS data persists independently of the EC2 instance lifecycle**.

---

### 5️⃣ EBS Snapshot (Backup & Recovery)
- Created an EBS snapshot to capture the state of the volume
- Verified snapshot status as **Completed**
- Demonstrates backup and recovery capability

📸 Screenshot:  
`screenshots/ebs-snapshot-created.png`

📸 Optional restore test:  
`screenshots/ebs-volume-created-from-snapshot.png`

---

## 📂 Project Structure
