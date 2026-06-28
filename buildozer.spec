[app]
title = Calculator
package.name = calculator
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

osx.python_version = 3
osx.kivy_version = 2.3.0

android.permissions = INTERNET
android.api = 33
android.build_tools_version = 33.0.2
android.accept_android_licenses = True

[buildozer]
log_level = 2
warn_on_root = 1
