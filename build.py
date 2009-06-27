"""
    A Build script that relies on py2exe
"""
from optparse import OptionParser

# This is used to preserve XP/Vista look and feel
# Don't ask me why, but without this, it will look ugly
manifest = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="0.64.1.0"
    processorArchitecture="*"
    name="Python"
    type="win32"
/>
<description>Python Interpreter</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
"""

main = 'free_rassam.py'
dest = 'free_rassam'

def do_exe():
 setup(
        windows=[dict(
                script=main, 
                other_resources=[(24,1,manifest)]
                )], 
        options=dict(py2exe=dict(optimize=2, compressed=True, dist_dir=dest,
            bundle_files=1)),
        zipfile=None,
        )   

import sys
sys.argv = [sys.argv[0]] + ["py2exe"]

from distutils.core import setup
import py2exe

print "Arabic build: "
print "--------------------"
do_exe()

print "\n"
print "English build: "
print "--------------------"
main = 'free_rassam_eng.py'
do_exe()

import os
print "\n"
print "Creating 7z archive: "
print "--------------------"
os.system("7za a free_rassam.7z free_rassam")

