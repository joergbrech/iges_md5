from setuptools import setup

setup(
    name='iges_md5',
    version='0.1.0',
    packages=['iges_md5'],
    entry_points={
        'console_scripts': [
            'iges_md5 = iges_md5.iges_md5:main'
        ]
    })
