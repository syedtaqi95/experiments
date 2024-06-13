# Hey Emacs, this is -*- coding: utf-8; mode: python -*-

import json
from pathlib import Path

from pydantic import BaseModel


class DspConfig(BaseModel):
    service_root: str
    data_stream_name: str
    data_stream_message_type: str


config_json_path = (
    Path(__file__).parent.resolve(strict=True) / "dsp-config.json"
)


def load() -> DspConfig:
    with Path.open(
        config_json_path,
        mode="r",
        encoding="utf8",
        errors="surrogateescape",
    ) as file:
        return DspConfig.model_validate(json.load(file))


def main() -> None:
    config = load()
    print(repr(config))


if __name__ == "__main__":
    main()
