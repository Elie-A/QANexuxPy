from setuptools import setup, find_packages

# Read the contents of README.md for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="QANexus",
    version="1.0.0",
    author="Elie Abdallah",
    author_email="elieabdallah961@gmail.com",
    description="A collection of utilities and assertions for QA and data generation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elie-A/QANexusPY'",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  
    install_requires=["numpy"],  
    extras_require={
        "dev": ["pytest"],
    },
)