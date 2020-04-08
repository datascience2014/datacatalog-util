import setuptools

setuptools.setup(
    name='datacatalog-util',
    version='0.1.0',
    author='Marcelo Miranda',
    author_email='mesmacosta@gmail.com',
    description='A package to manage Google Cloud Data Catalog'
    ' helper commands and scripts',
    platforms='Posix; MacOS X; Windows',
    packages=setuptools.find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'datacatalog-util = datacatalog_util:main',
        ],
    },
    include_package_data=True,
    install_requires=(
        'google-cloud-datacatalog',
        'pandas',
        'tabulate',
        'datacatalog-tag-manager @ git+https://github.com/ricardolsmendes/datacatalog-tag-manager',
    ),
    setup_requires=('pytest-runner', ),
    tests_require=('pytest-cov', ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
