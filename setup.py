from setuptools import setup, find_packages

setup(
    name="ferret",
    version="0.1.0",
    description="A simple CLI to display and explain project directory structures.",
    author="Abishek Padaki",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ],
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "ferret=project_tree_cli.cli:cli"
        ]
    },
    python_requires=">=3.7",
)
