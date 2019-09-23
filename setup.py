import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gbart",
    version="0.0.1",
    author="Augus Hsu(Yuhao Su)",
    author_email="su000088@umn.edu",
    description='A python package to implement Variable grouping based on Bayesian additive regression tree',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AugusHsu/gbart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'joblib',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'seaborn',
        'sklearn',
        'statsmodels',
    ]
)


'''

from os import path
from setuptools import setup, find_packages

#here = path.abspath(path.dirname())

setup(
    name='gbart',
    version='0.0.1',
    description='Variable grouping based on Bayesian additive regression tree',
    author='Augus Hsu(Yuhao Su)',
    url='www.ahsu.site',
    author_email='su000088@umn.edu',
    packages=find_packages(),
    install_requires=[
        'joblib',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'seaborn',
        'sklearn',
        'statsmodels',
    ]
)

'''
