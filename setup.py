from cx_Freeze import setup, Executable


exe = Executable(script='strantegus.py',
                 base='Win32Gui',
                 icon='gfx/ant.ico')
includefiles = [
    'gfx',
    'fonts']
includes = []
excludes = []
packages = []
bin_path_excludes = []
setup(version='PreAlpha6',
      description='Grand Strategy Game with Ants',
      author='PhelanBavaria',
      name='Strantegus',
      options={'build_exe': {'compressed': False,
                             'excludes': excludes,
                             'packages': packages,
                             'include_files': includefiles,
                             'bin_excludes': bin_path_excludes}},
      executables=[exe])
