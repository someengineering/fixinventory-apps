# cleanup-volumes
Volume cleanup app for Fix Inventory

This app cleans up unused storage volumes that have reached a certain age threshold.

## Usage

```
cleanup_volumes:
  # Minimum age of unused volumes to cleanup
  min_age: 14d
```

The default volume age is 14 days. Meaning if a volume is not in use and has not had any read or write IOPS within the last 14 days it will be deleted.

Optionally change the age cutoff value using the `min_age` option.

Example of valid age units:

```
weeks
days
hours
minutes
```

Each of them can be abbreviated down to one letter. E.g. `7d`, `24h`, `60m`, etc. A space in between the numeric and the unit is optional, meaning `7d` and `7 days` are equivalent.
