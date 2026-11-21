"""Outline only: turning state into summaries and reports.

This file only explains what the observability part of Multisource HL Copy is
responsible for. The production implementation is not public, and the names
here are illustrative, not a callable public API. Every method body raises
NotImplementedError("实现未公开") on purpose.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum


class RiskAction(Enum):
    """The three visible outcomes of a risk event."""

    PAUSE_ADDS = "pause_adds"
    CANCEL_KEEP_POSITIONS = "cancel_keep_positions"
    FLATTEN = "flatten"


class EventKind(Enum):
    OPEN = "open"
    RESIZE = "resize"
    CLOSE = "close"
    MARGIN = "margin"
    DRAWDOWN = "drawdown"
    FOLLOW_ISSUE = "follow_issue"


@dataclass
class ReportSection:
    title: str
    lines: list[str] = field(default_factory=list)


class Guard(ABC):
    """Independent process that re-checks the account against the same rules."""

    @abstractmethod
    def check(self) -> RiskAction | None:
        """Return an action when a rule is broken, otherwise None."""


class Reporter:
    """Periodic report: replication, deviation, latency, P&L, things to look at."""

    def build(self, period_hours: int) -> list[ReportSection]:
        raise NotImplementedError("实现未公开")

    def attention(self) -> ReportSection:
        raise NotImplementedError("实现未公开")


class EventFeed:
    """Real-time trade events, merged and rate-limited before sending."""

    def publish(self, kind: EventKind, text: str) -> None:
        raise NotImplementedError("实现未公开")
