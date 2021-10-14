from setuptools import setup

setup(
    name="pysniffer",
    version="0.1",
    py_modules=["main"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        main=main:cli
    """,
)
