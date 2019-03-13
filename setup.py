import sys
from cx_Freeze import setup, Executable

includefiles = ['icon.png']
includes = []
packages = ['pygame']

setup(
    name = 'PoemBuilder',
    version = '1.0',
    options = {'build_exe': {'includes':includes,'packages':packages,'include_files':includefiles}},
    executables = [Executable('PoemBuilder.py', icon = 'icon.png')]
)
