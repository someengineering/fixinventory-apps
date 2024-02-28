# fixinventory-apps
Fix Inventory Infrastructure Apps

## Usage of `fixinventoryappbundler`

```bash
fixinventoryappbundler --discover --path . > index.json
```

This command discovers all apps in the current directory and writes the index to `index.json`. This file can then be uploaded to a http server like a CDN and used as an app index in Fix Inventory.


## Usage of the `app` command in Fix Inventory

```bash
apps search [pattern] [--index-url https://cdn.some.engineering/fixinventory/apps/index.json]
app info <app_name> [--index-url https://cdn.some.engineering/fixinventory/apps/index.json]
app install <app_name> [--index-url https://cdn.some.engineering/fixinventory/apps/index.json]
app edit <app_name>
app uninstall <app_name>
app update <app_name>|all
apps list
app run <app_name> [--dry-run] [--validate] --config [config_name]
config create <config_name>
config copy <old_config> <new_config>
```
