"""Outline only: configuration and session control.

This file only explains what the control part of Multisource HL Copy is
responsible for. The production implementation is not public, and the names
here are illustrative, not a callable public API. Every method body raises
NotImplementedError("实现未公开") on purpose.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class ChangeTier(Enum):
    """How a configuration change takes effect while running."""

    INSTANT = "instant"  # next order onward, no pause
    REBUILD = "rebuild"  # cancel own orders, keep positions, resume
    SWITCH = "switch"    # source change; requires flat account, no orders


class ChangeOutcome(Enum):
    APPLIED = "applied"
    REFUSED = "refused"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"


@dataclass(frozen=True)
class SourceSpec:
    """A followed source wallet and its proportional ratio (illustrative)."""

    address: str
    ratio: float


class Operator(ABC):
    """Local entry point. Sensitive actions require explicit human approval."""

    @abstractmethod
    def plan(self, instance: str) -> str:
        """Build a full pre-start checklist for a human to review; returns its hash."""

    @abstractmethod
    def start(self, instance: str, plan_hash: str) -> None:
        """Start only if the server re-checks the same checklist."""

    @abstractmethod
    def stop(self, instance: str, flatten: bool = False) -> None:
        """Stop adding, cancel own orders; keep positions unless flatten is asked."""


class SessionControl(ABC):
    """Applies changes to a running session."""

    def preview(self, change: dict) -> ChangeTier:
        raise NotImplementedError("实现未公开")

    def apply(self, change: dict) -> ChangeOutcome:
        raise NotImplementedError("实现未公开")

    def switch_sources(self, sources: list[SourceSpec]) -> ChangeOutcome:
        raise NotImplementedError("实现未公开")
