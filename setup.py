﻿from distutils.core import setup
import py2exe

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

setup(
        windows=[dict(
                script='free_rassam.py', 
                other_resources=[(24,1,manifest)]
                )], 
        options=dict(py2exe=dict(optimize=2, compressed=True, dist_dir="free_rassam",
            bundle_files=1)),
        zipfile=None,
        )
