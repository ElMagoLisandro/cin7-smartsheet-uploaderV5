from setuptools import setup

APP = ['cin7_smartsheet_uploader_v5.py']
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'packages': ['pandas', 'smartsheet', 'openpyxl', 'numpy'],
    'includes': [
        'tkinter',
        'tkinter.scrolledtext',
        'tkinter.ttk',
        'pandas._libs.tslibs.base',
        'pandas._libs.tslibs.timedeltas',
        'pandas._libs.tslibs.np_datetime',
        'pandas._libs.tslibs.offsets',
        'smartsheet.models',
        'smartsheet.util',
        'openpyxl.workbook',
        'openpyxl.worksheet',
        'openpyxl.cell',
        'queue',
        'threading',
        'json',
        'logging',
        'pathlib',
        'tempfile',
        'platform',
        're',
        'traceback',
    ],
    'excludes': [
        'matplotlib',
        'scipy',
        'IPython',
        'jupyter',
        'notebook',
        'pytest',
        'PIL',
    ],
    'plist': {
        'CFBundleName': 'Cin7 Smartsheet Uploader',
        'CFBundleDisplayName': 'Cin7 Smartsheet Uploader v5.0',
        'CFBundleShortVersionString': '5.0.0',
        'CFBundleVersion': '5.0.0',
        'CFBundleIdentifier': 'com.futuratrailers.cin7uploader',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.14.0',
        'NSRequiresAquaSystemAppearance': False,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    name='Cin7 Smartsheet Uploader',
    version='5.0.0',
    description='Professional inventory upload tool for Futura Trailers',
    author='Futura Trailers',
    python_requires='>=3.8',
)