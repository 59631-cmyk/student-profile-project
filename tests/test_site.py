
from pathlib import Path

SITE = Path("src/index.html")


def test_homepage_exists():
    assert SITE.exists()


def test_homepage_has_title():
    html = SITE.read_text(encoding="utf-8")
    assert "<title>Student Profile</title>" in html


def test_homepage_has_student_information():
    html = SITE.read_text(encoding="utf-8")
    assert "Student Profile" in html
    assert "Department:" in html
    assert "Semester:" in html


def test_homepage_has_html_structure():
    html = SITE.read_text(encoding="utf-8")
    assert "<html" in html
    assert "</html>" in html
    assert "<body>" in html
    assert "</body>" in html

def test_deliberate_failure():
    assert False, "Demonstration of CI failure"
