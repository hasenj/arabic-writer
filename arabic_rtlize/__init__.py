"""
    Author: Hasen il Judy
    License: GPL v2 or LGPL v2.1

    general recommended usage:

        from arabic_rtlize import rtlize
        ...
        rtlize(your_string)

    You can also import `un_rtlize` which restores the text to its original form.
"""

import arabic_rtlize.process

rtlize = process.rtlize
un_rtlize = process.restore

