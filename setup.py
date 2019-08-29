import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="async_sendgrid",
    version="0.1.0",
    description="Sendgrid v3 API async/await",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sergey-tikhonov/async_sendgrid",
    author="Sergey Tikhonov",
    author_email="srg.tikhonov@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["async_sendgrid"],
    include_package_data=True,
    install_requires=["requests_async"],
)
