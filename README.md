ttkSimpleDialog
===============

This module allows the developer to use simple dialog boxes such as
- askint: ask the user for an integer
- askfloat: ask the user for a float
- askstring: ask the user for a string

Example
-------

    from ttkSimpleDialog import ttkSimpleDialog

    user_response = ttkSimpleDialog.askinteger(title="hello", prompt="Enter a number")

Please note you must call it using the `from __ import __` syntax!