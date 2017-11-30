#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Tests for `myratings` package."""


import unittest
from click.testing import CliRunner

from myratings import myratings
from myratings import cli
from myratings.codechef import obtainRating as ccor
from myratings.codeforces import obtainRating as cfor
from myratings.hackerearth import obtainRating as hkor


class TestMyratings(unittest.TestCase):
    """Tests for `myratings` package."""
    
    def test_codechef_on_proper_input(self):
        """Tests codechef's obtainRating method behaviour on proper input."""        
        self.assertTrue(ccor("http://www.codechef.com/users/kgarun") != "NA")
    
    def test_codechef_on_improper_input(self):
        """Tests codechef's obtainRating method behaviour on improper input."""
        self.assertTrue(ccor("http://www.codechef.com/users/abc12sffnkk") == "NA")
    
    def test_codeforces_on_proper_input(self):
        """Tests codeforces's obtainRating method behaviour on proper input."""        
        self.assertTrue(cfor("http://www.codeforces.com/profile/kgarun50") != "NA")
    
    def test_codeforces_on_improper_input(self):
         """Tests codeforces's obtainRating method behaviour on improper input."""
         self.assertTrue(cfor("http://www.codeforces.com/profile/kgarunaffgwgs50") == "NA")
    
    def test_hackerearth_on_proper_input(self):
        """Tests hackerearth's obtainRating method behaviour on proper input."""        
        self.assertTrue(hkor("https://www.hackerearth.com/@kgarun50") != "NA")
    
    def test_hackerearth_on_improper_input(self):
        """Tests hackerearth's obtainRating method behaviour on improper input.""" 
        self.assertTrue(hkor("https://www.hackerearth.com/@kgarundgdhhhhh50") == "NA")

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'myratings.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
