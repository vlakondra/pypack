from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# with open("requirements.txt", "r", encoding="utf-8") as fh:
#     requirements = fh.read()

setup(
    name='cliscript',
    version='0.1.3',
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
    packages = find_packages(),
    # install_requires = [requirements],
    
    python_requires='>=3.6',
    
    
    py_modules=['src.newlib.ttt'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'myscript = src.newlib.ttt:cli',
            'second = src.newlib.ttt:cli2 '
        ],
    },
)