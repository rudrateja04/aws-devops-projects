# Project 06 – DynamoDB CRUD Operations

## Overview
This project demonstrates the basic usage of Amazon DynamoDB,
a fully managed NoSQL database service provided by AWS.

The goal of this project is to understand how DynamoDB stores data
and how basic CRUD (Create, Read, Update, Delete) operations work
using the AWS Management Console.

---

## AWS Services Used
- Amazon DynamoDB
- AWS IAM

---

## Table Design
- Table Name: UsersTable
- Partition Key: UserId (String)

---

## What I Did
- Created a DynamoDB table using on-demand capacity mode
- Inserted an item into the table
- Retrieved the item using the partition key
- Updated an existing attribute of the item
- Deleted the item from the table

All operations were performed using the AWS Management Console.

---

## Verification
Each CRUD operation was verified directly in the DynamoDB console.
Screenshots showing table creation, item retrieval, and deletion
are available in the screenshots folder.

---

## Learning Outcome
- Understanding of NoSQL and key-value data models
- Hands-on experience with DynamoDB
- Difference between relational databases and DynamoDB
- Working with serverless database services in AWS

---

## Cleanup
After completing the project, the DynamoDB table was deleted
to avoid unnecessary charges.
