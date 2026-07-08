#!/usr/bin/env python3
"""Validate that every blueprint under blueprints/ is syntactically valid YAML."""

import sys
from pathlib import Path

import yaml


def input_constructor(loader, node):
    return {"!input": loader.construct_scalar(node)}


yaml.SafeLoader.add_constructor("!input", input_constructor)

REQUIRED_TOP_LEVEL_KEYS = {"blueprint"}


def validate(path: Path) -> str | None:
    try:
        with path.open() as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        return f"invalid YAML: {exc}"

    if not isinstance(data, dict):
        return "top level is not a mapping"

    missing = REQUIRED_TOP_LEVEL_KEYS - data.keys()
    if missing:
        return f"missing required key(s): {', '.join(sorted(missing))}"

    if "domain" not in data.get("blueprint", {}):
        return "blueprint.domain is missing"

    return None


def main() -> int:
    root = Path(__file__).resolve().parent.parent / "blueprints"
    files = sorted(root.rglob("*.yaml")) + sorted(root.rglob("*.yml"))

    if not files:
        print("No blueprint files found under blueprints/")
        return 0

    failed = False
    for path in files:
        error = validate(path)
        rel = path.relative_to(root.parent)
        if error:
            print(f"FAIL {rel}: {error}")
            failed = True
        else:
            print(f"OK   {rel}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
