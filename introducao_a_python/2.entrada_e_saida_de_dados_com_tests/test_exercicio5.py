from exercicio5 import validate_email
import pytest


# username test

def test_username_can_only_contain_letters():
    assert validate_email('test@gmail.com') is None


def test_username_can_contain_letters_and_digits():
    assert validate_email('test123@gmail.com') is None


def test_username_can_contain_letters_digits_and_dashes():
    assert validate_email('te_1st@gmail.com') is None


def test_username_can_contain_letters_digits_dashes_and_underscore():
    assert validate_email('t_e1st@gmail.com') is None


def test_username_should_starts_with_letter():
    assert validate_email('t@gmail.com') is None


def test_username_when_dont_start_with_letter_raise_exception():
    with pytest.raises(ValueError):
        validate_email('1@gmail.com')


def test_username_is_invalid_raise_exception():
    with pytest.raises(ValueError):
        validate_email('t%e@gmail.com')


# website test

def test_website_contain_only_letters_and_digits():
    assert validate_email('test@website123.com') is None


def test_website_invalid_chars_raise_exception():
    with pytest.raises(ValueError):
        validate_email('test@website!123.com')


# extensão test

def test_extension_should_contain_only_three_chars():
    assert validate_email('test@gmail.com') is None


def test_extension_invalid_chats_raise_exception():
    with pytest.raises(ValueError):
        validate_email('test@gmail.python')
