from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ConsoleM",
    version="0.1.9",
    author="Remi",
    description="A powerful Python library for terminal manipulation and text styling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Remi-Avec-Un-I/ConsoleM",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    keywords="terminal, console, text styling, cursor control, keyboard input",
) 