# cleanup-aws-vpcs
AWS VPC Cleanup App for Fix Inventory

This app marks all VPC dependencies for cleanup. The VPC must have been previously marked for cleanup by another cleanup plugin.

The following resources are currently being marked for cleanup

- AWS VPC Peering Connections
- AWS EC2 Network ACLs
- AWS EC2 Network Interfaces
- AWS ELB
- AWS ALB
- AWS ALB Target Groups
- AWS EC2 Subnets
- AWS EC2 Security Groups
- AWS EC2 Internet Gateways
- AWS EC2 NAT Gateways
- AWS EC2 Route Tables

## Usage

```
cleanup_aws_vpcs:
  # Dictionary of key cloud with list of account IDs for which the plugin should be active as value
  cloud_and_accounts:
    aws:
      - '1234567'
      - '567890'
```
