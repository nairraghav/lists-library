from lists import __VERSION__
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="",  # Update
    version=__VERSION__,
    author="",  # Update
    author_email="",  # Update
    description="",  # Update
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",  # Update
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': ['lists=lists:main'],  # Update
    }
)
