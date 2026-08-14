"""OpenMM-CpH: Constant pH simulation for OpenMM
"""

from setuptools import setup, find_packages
DOCLINES = __doc__.split("\n")

########################
__version__ = '1.0'
VERSION = __version__
ISRELEASED = False
########################
CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: End Users/Desktop
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Scientific/Engineering :: Bio-Informatics
Topic :: Scientific/Engineering :: Chemistry
Topic :: Scientific/Engineering :: Physics
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

setup(
    name='OpenMM-CpH',
    author='Peter Eastman',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=__version__,
    license='MIT',
    url='https://github.com/peastman/openmm-cph',
    platforms=['Linux', 'Mac OS-X', 'Unix', 'Windows'],
    classifiers=CLASSIFIERS.splitlines(),
    packages=find_packages(),
    zip_safe=False,
    install_requires=['openmm >= 8.3', 'scipy'])

