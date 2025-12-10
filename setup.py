from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="feat-behave",
    version="0.1.1",
    author="Kiril Milititski",
    author_email="milititskiy3@gmail.com",
    description="Run behave feature files from VS Code with 'feat' command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/milititskiy/feat-behave.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.6",
    install_requires=[
        "argcomplete>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "feat=auto_behave.cli:main",
            "auto-behave=auto_behave.cli:main",
        ],
    },
)
