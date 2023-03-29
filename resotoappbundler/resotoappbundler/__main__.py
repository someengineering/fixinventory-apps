import sys
import yaml
import json
import base64
from pathlib import Path
from resotolib.logger import log, setup_logger, add_args as logging_add_args
from resotolib.args import ArgumentParser
from .app import add_args as app_add_args

def main() -> None:
    setup_logger("resotoappbundler")

    arg_parser = ArgumentParser(description="Resoto Infrastructure Apps Bundler")
    app_add_args(arg_parser)
    logging_add_args(arg_parser)
    arg_parser.parse_args()

    app_path = Path(arg_parser.args.app_path)
    app_manifest = app_path / "app.yaml"
    app_readme = app_path / "README.md"
    app_source = app_path / "app.jinja2"
    app_icon = app_path / "app.svg"
    for file in [app_manifest, app_readme, app_source, app_icon]:
        if not file.exists():
            log.error(f"Path {file} does not exist")
            sys.exit(1)

    source = app_source.read_text()
    manifest = yaml.load(app_manifest.read_text(), Loader=yaml.FullLoader)
    readme = app_readme.read_text()
    icon = "data:image/svg+xml;base64," + base64.b64encode(app_icon.read_bytes()).decode("utf-8")

    manifest["readme"] = readme
    manifest["icon"] = icon
    manifest["source"] = source

    print(json.dumps(manifest, indent=4))

    sys.exit(0)



if __name__ == "__main__":
    main()
