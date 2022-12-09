import haiku_poem

import syllapy
import pytest


def test_haiku_title_returns_string():
    title = haiku_poem.haiku_creator()
    assert isinstance(title, str)