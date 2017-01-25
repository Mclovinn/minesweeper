from minesweeper import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'Initial State')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')

@then(u'Initial page showed')
def step_impl(context):
	assert 'Minesweeper' in browser.html
