from setuptools import setup, find_packages

setup(
    name="INEXJD",
    version="1.0.0rc4",
    description="A JSON SQL-like database library",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="International Technology For Everything",
    author_email="ammarbasha2011@gmail.com",
    url="https://github.com/AmmarBasha2011/IJD",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.*', '*/*.*', '*/*/*.*'],  # Include all files in all subdirectories
    },
    install_requires=[
        # List required packages here
    ],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
