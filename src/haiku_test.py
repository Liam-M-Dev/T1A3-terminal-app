import haiku_poem

import syllapy
from sys import stdin
import io
import pytest


def test_haiku_title_returns_string(monkeypatch):
    title = haiku_poem.haiku_creator()
    assert isinstance(title, str)