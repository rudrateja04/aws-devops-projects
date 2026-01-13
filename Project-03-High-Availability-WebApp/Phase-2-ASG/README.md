Phase 2: Auto Scaling Group (ASG)

In this phase, I implemented an Auto Scaling Group to make
the application scalable and fault-tolerant.

A launch template was created with a user data script that
automatically installs Apache and configures the web server.

The Auto Scaling Group creates and manages EC2 instances
and attaches them to the existing Application Load Balancer.
When an instance is terminated, a new instance is created
automatically.

This demonstrates scalability and self-healing in AWS.
