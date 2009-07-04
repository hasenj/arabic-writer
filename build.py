"""
    A Build script that relies on py2exe
"""
import os

# Magic value, don't touch
__build__ = 52

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

main = 'free_ressam.py'
dest = 'free_ressam'
dest_7z = 'free_ressam_build_%d.7z' % __build__

def do_exe():
 setup(
        windows=[dict(
                script = main, 
                other_resources = [(24,1,manifest)]
                )], 
        options=dict(
            py2exe=dict(
                optimize=2, 
                includes=['sip'],
                # compressed=True, 
                dist_dir=dest,
                # bundle_files=3
                )),
        # zipfile = None,
        data_files = [ 
            ('docs', ['docs/logo.png']),
            ('docs', ['docs/help_arabic.html']),
            ('docs', ['docs/help_english.html']),
            ('docs', ['docs/technical_arabic.html']),
            ('docs', ['docs/technical_english.html']),
            ('art', ['art/icon.png']),
            ('art', ['art/help.png']),
            ('art', ['art/clear.png']),
            ('art', ['art/copy.png']),
            ('art', ['art/restore.png']),
            ('art', ['art/quit.png']),
            ],
        )   

import sys
sys.argv = [sys.argv[0], "py2exe"]

from distutils.core import setup
import py2exe

print "Buiding The Free Ressam (Er Ressam il Hur)"
print "Build", __build__
print "\n"
print "Cleaning previous build"
print "--------------------"
os.system("rm -rf " + dest) 

print "\n"
print "Arabic build: "
print "--------------------"
do_exe()

print "\n"
print "English build: "
print "--------------------"
main = 'free_ressam_eng.py'
do_exe()


print "\n"
print "Exporting Source Code"
print "--------------------"
os.system("git checkout-index -a -f --prefix=" + dest + "/src/")

print "\n"
print "Creating 7z archive: "
print "--------------------"
os.system("7za a " + dest_7z + " " + dest)

print "\n"
print "Cleaning build files"
print "--------------------"
os.system("rm -rf build")
