import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eda_utils", # Replace with your own username
    version="0.0.1",
    author="rajat ghosh",
    author_email="rajat.ghosh11@gmail.com",
    description="this is an experimental package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rghosh8/firstpip.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)