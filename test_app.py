import os
from flask import Flask
from flask_wtf.csrf import CsrfProtect
from flask_wtf import FlaskForm

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)