# Project 04: Static Website Hosting using Amazon S3

## About This Project
In this project, I hosted a static website using Amazon S3.
The website consists of simple HTML files and does not require
any server or backend application.

This project demonstrates how S3 can be used to host static
content in a cost-effective and scalable way.

---

## AWS Services Used
- Amazon S3
- AWS IAM

---

## What I Did
1. Created an S3 bucket
2. Uploaded static website files (index.html and error.html)
3. Enabled static website hosting on the bucket
4. Configured public read access using bucket policy
5. Accessed the website using the S3 website endpoint

Website files are available in the `website` folder.
Screenshots of the setup are available in the `screenshots` folder.

---

## Result
The static website was successfully hosted on Amazon S3 and
was accessible through the S3 website endpoint without using
any EC2 instance or server.

---

## What I Learned
- How S3 stores and serves static content
- Difference between object storage and server-based hosting
- How static website hosting works in AWS
- Basic S3 permissions and public access configuration

---

## Cleanup
After completing the project, the S3 bucket can be deleted
to avoid unnecessary charges.

---

## Author
Rudra Teja
