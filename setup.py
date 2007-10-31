from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='fassembler',
      version=version,
      description="Builder for TOPP",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ian Bicking',
      author_email='ianb@openplans.org',
      url='http://openplans.org/projects/fassembler',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'ScriptTest',
        'PasteScript',
      ],
      entry_points="""
      [console_scripts]
      fassembler = fassembler.command:main
      """,
      )
