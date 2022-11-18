from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="testmiqui",
    description="test miqui",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Miquel Ferrer",
    url="https://github.com/miquiferrer/testmiqui",
    project_urls={
        "Issues": "https://github.com/miquiferrer/testmiqui/issues",
        "CI": "https://github.com/miquiferrer/testmiqui/actions",
        "Changelog": "https://github.com/miquiferrer/testmiqui/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["testmiqui"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
