# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Some key classes are available directly in the ``composer`` namespace."""

from composer._version import __version__
from composer.core import (
    Algorithm,
    Callback,
    DataSpec,
    Engine,
    Evaluator,
    Event,
    State,
    Time,
    Timestamp,
    TimeUnit,
)
from composer.loggers import Logger
from composer.models import ComposerModel

try:
    from composer.trainer import Trainer
except ImportError:
    # Trainer depends on optional heavy dependencies; avoid raising on package import
    Trainer = None

__all__ = [
    "Algorithm",
    "Callback",
    "DataSpec",
    "Engine",
    "Evaluator",
    "Event",
    "State",
    "Time",
    "Timestamp",
    "TimeUnit",
    "Logger",
    "ComposerModel",
    "Trainer",
]
