from setuptools import setup, find_packages
import os

version = u'1.0'

setup(name=u'men.design',
      version=version,
      description="The design package for the nimc project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='theme plone skins template',
      author='Max Brauer',
      author_email='max.brauer@it2009.ba-leipzig.de',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[u'men'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      
      """,
      )
