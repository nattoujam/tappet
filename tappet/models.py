from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass
class RequestSet:
    name: str
    method: str
    url: str
    headers: Dict[str, str]
    body: Optional[Dict[str, Any]]
    description: Optional[str] = ""
    file_path: Optional[Path] = None

    def is_same_file(self, other: Optional[RequestSet]) -> bool:
        if other is None:
            return False
        if self.file_path is not None and other.file_path is not None:
            return self.file_path == other.file_path
        return self == other


@dataclass
class Response:
    status_code: Optional[int] = None
    reason: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    body: str = ""
    elapsed_ms: Optional[float] = None
    error: Optional[str] = None
    note: Optional[str] = None
