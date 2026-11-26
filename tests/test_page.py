#!/usr/bin/env python3
"""Checks that the living transmission page carries the brand signal and no ask."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


class LivingTransmissionPage(unittest.TestCase):
  def setUp(self):
    self.html = INDEX.read_text(encoding="utf-8")

  def test_brand_name_is_present(self):
    self.assertIn("Good Power Infinity", self.html)
    self.assertRegex(self.html, r"<h1[^>]*class=\"brand\"")

  def test_seal_name_is_present(self):
    self.assertIn(
      "Good Power Infinity, So that Evil May Be a Solved Problem, Inc.",
      self.html,
    )
    self.assertRegex(self.html, r"class=\"seal\"")

  def test_globe_is_beside_brand(self):
    self.assertRegex(self.html, r"class=\"globe\"")
    css = (ROOT / "css" / "styles.css").read_text(encoding="utf-8")
    js = (ROOT / "js" / "main.js").read_text(encoding="utf-8")
    self.assertIn("earth-map.jpg", css)
    self.assertIn("align-items: flex-start", css)
    self.assertIn("syncGlobeToBrand", js)
    self.assertTrue((ROOT / "assets" / "earth-map.jpg").is_file())

  def test_byline_and_ticker(self):
    self.assertIn("By Jd Diamari", self.html)
    self.assertIn("$GPI 5T", self.html)
    self.assertRegex(self.html, r"class=\"byline\"")
    self.assertRegex(self.html, r"class=\"ticker\"")

  def test_no_cta_form_or_mailto(self):
    self.assertNotRegex(self.html, r"<form\b", re.I)
    self.assertNotRegex(self.html, r"mailto:", re.I)
    self.assertNotRegex(self.html, r"<input\b", re.I)
    self.assertNotRegex(self.html, r"<button\b", re.I)

  def test_no_corny_taglines(self):
    banned = [
      "Aims the world at the good future",
      "A coalition factory",
      "Keeping the good in power",
    ]
    for line in banned:
      self.assertNotIn(line, self.html)


if __name__ == "__main__":
  unittest.main()
