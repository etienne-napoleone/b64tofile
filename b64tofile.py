#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import base64
import os
import sys


def parse_env(name: str) -> List[str]:
    value = os.getenv(name)
    if not value:
        print(f"{name} is empty", file=sys.stderr)
        sys.exit(1)
    values = value.split(",")
    return values


def write(path: str, base64_content: str) -> None:
    base64_content_bytes = base64_content.encode("utf8")
    content_bytes = base64.decodebytes(base64_content_bytes)
    content = content_bytes.decode()
    with open(path, "w") as f:
        f.write(content)
        print(f"Created file {path}")


if __name__ == "__main__":
    files_paths = parse_env("FILES_PATHS")
    files_base64 = parse_env("FILES_BASE64")
    if len(files_paths) == len(files_base64):
        for index, path in enumerate(files_paths):
            write(path, files_base64[index])
    else:
        print(
            "FILE_PATHS and FILE_BASE64 should have the same number of elements",
            file=sys.stderr,
        )
        sys.exit(1)
