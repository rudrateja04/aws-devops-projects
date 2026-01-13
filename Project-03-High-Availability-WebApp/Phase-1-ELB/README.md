Project 3 – Phase 1: Application Load Balancer (ELB)

In this project, I implemented a highly available web application
using an Application Load Balancer (ALB).

Two EC2 instances were launched with a user data script that
automatically installs Apache and creates a web page displaying
the instance hostname.

The Application Load Balancer distributes traffic across both
instances. Refreshing the browser shows different hostnames,
proving successful load balancing.

Screenshots are available in the screenshots folder.
