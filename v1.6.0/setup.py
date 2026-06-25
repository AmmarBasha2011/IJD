from setuptools import setup, find_packages

setup(
    name="INEXJD",
    version="1.6.0",
    description="A JSON SQL-like database library with statistics, compression, encryption, audit logging, health checks, and all previous features!",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="International Technology For Everything",
    author_email="ammarbasha2011@gmail.com",
    url="https://github.com/AmmarBasha2011/IJD",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.*', '*/*.*', '*/*/*.*'],
    },
    install_requires=[],
    extras_require={
        "gui": ["flask"],
        "excel": ["openpyxl"],
        "s3": ["boto3"],
        "dropbox": ["dropbox"],
        "fastapi": ["fastapi", "uvicorn"],
        "encryption": ["cryptography"],
        "all": ["flask", "openpyxl", "boto3", "dropbox", "fastapi", "uvicorn", "cryptography"]
    },
    entry_points={
        "console_scripts": [
            "inexjd = INEXJD.cli:main",
        ],
    },
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
