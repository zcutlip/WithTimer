from __future__ import absolute_import
from setuptools import setup
about = {}
with open("withtimer/__about__.py") as fp:
    exec(fp.read(), about)

setup(name=about["__title__"],
      version=about["__version__"],
      description=about["__summary__"],
      url="TBD",
      packages=['withtimer'],
      python_requires='>=2.7',
      install_requires=[],
      package_data={'withtimer': ['config/*']},
      )
