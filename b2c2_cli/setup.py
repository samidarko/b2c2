from setuptools import setup

setup(
    name="b2c2-cli",
    version="1.0",
    py_modules=["b2c2"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        b2c2=b2c2:cli
    """,
)