from minesweeper import *
from behave import *
from splinter import Browser

browser = Browser('flask',app=app)


@given(u'Initial page')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')


@then(u'Initial page showed')
def step_impl(context):
	assert 'Minesweeper' in browser.html


@then(u'The game board is showed')
def step_impl(context):
    assert browser.find_by_id('game_board')


@then(u'The 3x3 game board is showed')
def step_impl(context):
    for x in range(0, 3):
        for y in range(0, 3):
            assert browser.find_by_id('({}, {})'.format(x, y))

@when(u'press button with position {position}')
def step_impl(context, position):
    browser.find_by_id(position)[0].click()

@then(u'NOT_BOMB is showed')
def step_impl(context):
    assert 'NOT_BOMB' in browser.html

@then(u'BOMB is showed')
def step_impl(context):
    assert 'BOMB' in browser.html
