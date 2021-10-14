#!/usr/bin/env python3

import os.path
import sys
import subprocess

# from conans import ConanFile
print(sys.path);

import conanfile

print(conanfile)

class KatanaEnterpriseConanExtra(conanfile.KatanaEnterpriseConan):
    # Several packages are installed via APT:
    #  - arrow
    #  - llvm
    requires = (
            conanfile.KatanaEnterpriseConan.requires + 
        ("arrow/5.0.0",)
    )

