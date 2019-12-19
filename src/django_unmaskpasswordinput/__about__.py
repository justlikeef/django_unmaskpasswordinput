# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__", "__author__",
    "__email__", "__license__", "__copyright__","__requirements__"
]

__requirements__ = ["Django"]
__title__ = "django_unmaskpasswordinput"
__summary__ = "Provides an input field that is hidden by default but can be unmasked by clicking on an icon"
__uri__ = "https://git01.pfsfhq.com/Operations/django_unmaskpasswordinput/homepage/"
__version__ = "1.0.0a0"
__author__ = "Primerica Network Team"
__email__ = "networkteam@primerica.com"
__license__ = "BSD or Apache License, Version 2.0"
__copyright__ = "Copyright 2019 {}".format(__author__)
__includedata__ = True
__includedatafiles__ = {'' : ['templates/forms/widgets/unmaskpassword.html','static/django_unmaskpasswordinput/css/*','static/django_unmaskpasswordinput/js/*','static/django_unmaskpasswordinput/svgs/regular/*','static/django_unmaskpasswordinput/svgs/solid/*','static/django_unmaskpasswordinput/webfonts/*']}
__excludedatafiles__ = {}
