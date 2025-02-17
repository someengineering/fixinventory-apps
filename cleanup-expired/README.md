# cleanup-expired
Fix Inventory app for cleanup of expired resources

This app looks for resources with the tags `expiration` or `fix:expires` and flags them for cleanup if they are expired.

## Tag format

| Tag              | Format                      | Description                                          |
| ---------------- | --------------------------- | ---------------------------------------------------- |
| `fix:expires`    | `2019-09-05T10:40:11+00:00` | ISO 8601 Timestamp                                   |
| `expiration`     | `24h`                       | A timedelta relative to the resource's creation time |

Example of valid units for the `expiration` tag:

```
weeks
days
hours
minutes
```

Each of them can be abbreviated down to one letter. E.g. `7d`, `24h`, `60m`, etc. A space in between the numeric and the unit is optional, meaning `7d` and `7 days` are equivalent.
