# resoto-apps
Resoto Infrastructure Apps

## Usage of `resotoappbundler`

```bash
resotoappbundler --discover --path . > index.json
```

This command discovers all apps in the current directory and writes the index to `index.json`. This file can then be uploaded to a http server like a CDN and used as an app index in Resoto.


## Usage of the `app` command in Resoto

```bash
apps search [pattern] [--index-url https://cdn.some.engineering/resoto/apps/index.json]
app info <app_name> [--index-url https://cdn.some.engineering/resoto/apps/index.json]
app install <app_name> [--index-url https://cdn.some.engineering/resoto/apps/index.json]
app edit <app_name>
app uninstall <app_name>
app update <app_name>|all
apps list
app run <app_name> [--dry-run] [--validate] --config [config_name]
config create <config_name>
config copy <old_config> <new_config>
```

[Design Doc](https://docs.google.com/document/d/1tHZpPAWKh1XMLqsoapAKibAkLnnqH0edCIC6Li-W2b8/edit?usp=sharing)
