from setuptools import setup

setup(name='snapdclient',
      version='0.1',
      description='Client to interact with the snapd rest api',
      url='http://github.com/sbaldassin/python-snapdclient',
      author='Santiago Baldassin',
      author_email='santiago.baldassin@canonical.com',
      license='GPLv3',
      packages=['snapdclient, snapdclient.v2, snapdclient.v2.snaps'],
      zip_safe=False)
