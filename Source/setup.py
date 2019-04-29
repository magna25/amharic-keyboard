import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="amharic-keyboard-magna25",
    version="0.0.1",
    author="Henok Hailemariam",
    author_email="henny.bog@gmail.com",
    description="A package to type amharic letters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/magna25/amharic-keyboard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)