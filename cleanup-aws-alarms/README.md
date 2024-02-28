# cleanup-aws-alarms
AWS Cloudwatch Alarms Cleanup Plugin for Fix Inventory

This plugin marks all orphaned AWS CloudWatch Instance Alarms for cleanup.

The following resources are currently being marked for cleanup:
- Instance Alarms

## Usage

```
cleanup_aws_alarms:
  # Dictionary of key cloud with list of account IDs for which the plugin should be active as value
  clouds_and_accounts:
    aws:
      - '1234567'
      - '567890'
```
