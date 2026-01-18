# Project 06 – AWS VPC Basics

## Overview
This project demonstrates the creation of a custom Amazon VPC with a public subnet and launching an EC2 instance inside it.

The goal of this project is to understand how networking components in AWS work together to provide internet access to resources.

---

## Architecture Components
- Custom VPC
- Public Subnet
- Internet Gateway
- Route Table
- EC2 Instance with Public IP

---

## Steps Performed

1. Created a custom VPC with CIDR block `10.0.0.0/16`
2. Created a public subnet inside the VPC
3. Created and attached an Internet Gateway to the VPC
4. Created a route table and added a route to the Internet Gateway
5. Associated the public subnet with the route table
6. Launched an EC2 instance inside the public subnet
7. Verified that the EC2 instance received a public IP address

---

## Verification
- EC2 instance is running in a public subnet
- Public IPv4 address is assigned
- Instance is reachable via the internet

---

## Screenshots
All step-by-step screenshots are available in the `screenshots/` folder.

---

## Key Learnings
- Difference between public and private subnets
- How route tables control traffic flow
- Role of Internet Gateway in enabling internet access
- How EC2 networking depends on subnet and routing
