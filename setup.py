from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# with open("requirements.txt", "r", encoding="utf-8") as fh:
#     requirements = fh.read()

setup(
    name='cli-app-vlakondra',
    version='0.4.2',
    author="Vlakondra",
    author_email="vkondra@gmail.com",
    description="Small cli app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlakondra/pypack",
    project_urls={
        "Bug Tracker": "https://github.com/vlakondra/pypack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    python_requires='>=3.6',
    install_requires=[
        'Click',
    ],
    packages = find_packages('src'),
    # install_requires = [requirements],
    
    include_package_data=True,
 
    py_modules=['cliapp.commands', 'cliapp.complex_commands', 'cliapp.datacomm'],
    package_dir={"": "src"}, 
 
    # package_data={
    #     # If any package contains *.txt or *.rst files, include them:
    #     "cliapp": ["*.txt", "*.rst"]
    # },
    entry_points={
        'console_scripts': [
            'simple_1 = cliapp.commands:cli',
            'simple_2 = cliapp.commands:cli2',
            'readfile = cliapp.complex_commands:getfile',
            'check = cliapp.complex_commands:touch',
            
            'showdata = cliapp.datacomm:showtable',
            'showpart = cliapp.datacomm:grp'
        ],
    },
)