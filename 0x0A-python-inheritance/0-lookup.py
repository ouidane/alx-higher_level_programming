#!/usr/bin/python3
"""Define an obj atrr"""

def lookup(obj):
    """Use the dir() to get the list"""
    attr_and_methods = dir(obj)
    return (attr_and_methods)
