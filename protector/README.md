# protector
Protector App for Fix Inventory

This app protects important resources from deletion by Fix Inventory.

## Usage

```
protector:
  config:
    aws:
      '110465657741':
        us-east-1:
          aws_ec2_instance:
            - 'i-0fcbe8974615bfd37'
```

The format of the `config` section is as follows:

```
cloud.id:
  account.id:
    region.id:
      kind:
        - resource.id
```

### Implementation details

Each Fix Inventory resource has an attributed `/metadata.protected` which takes a boolean value. By default it is set to `false`. Each Fix Inventory resource inherits BaseResource which contains two methods for cleaning up a resource, `cleanup()` and `delete()`. Both those methods will refuse to manipulate a resource once the `protected` attribute has been set to `true`. Meaning if a resource is marked as protected but has also been flagged for cleanup the cleanup will fail because protected resources cannot be deleted.
