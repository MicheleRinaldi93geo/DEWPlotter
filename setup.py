from setuptools import setup, find_packages

# Version 1.1.0

# Library info
setup(
    name="DEWPlotter_lib",
    version="1.1.0",
    author='ENKI and Michele Rinaldi',
    author_email='rinaldim@tcd.ie',
    url='http://www.dewcommunity.org',
    description='Plotter for EQ6 package',
    packages=find_packages(),  # Automatically find all packages in the project directory

    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "termcolor",
        "openpyxl",

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
