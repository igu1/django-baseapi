from setuptools import setup, find_packages

setup(
    name="ez-baseapi",
    version="0.1.0",
    description="A Python package for simplifying the RESTful API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Eza",
    author_email="eesaard@gmail.com",
    url="https://github.com/igu1/MessagingAPI",
    packages=find_packages(),
    install_requires=["django", "djangorestframework"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
