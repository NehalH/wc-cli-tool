from setuptools import setup

setup(
    name="wc_cli_tool",
    version="1.0",
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "cliwc=main:wc",
        ],
    },
)