#!/usr/bin/env python3

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='python_ci_test',
        version="0.1.1",
        description='A basic python ci test',
        author='Patrick Avery',
        author_email='',
        url="https://github.com/psavery/python-ci-test",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        install_requires=[],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
    )
