from distutils.core import setup
import setuptools

setup(
    name='ocad',
    version='0.0.2',
    author='Marius Huerzeler',
    author_email='huerzeler.marius@gmail.com',
    packages=['ocad', 'ocad.test'],
    url='',
    license='MIT',
    description='Module for handling ocad-files',
    long_description=open('README.md').read(),
    python_requires='>=3',
    classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],

)
