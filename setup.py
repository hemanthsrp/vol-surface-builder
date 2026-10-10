from setuptools import setup, find_packages

setup(
    name="vol-surface-builder",
    version="0.2.1",
    description="Implied volatility surface construction from equity option chains",
    author="hemanthsrp",
    author_email="bahubali.hemanth11@gmail.com",
    url="https://github.com/hemanthsrp/vol-surface-builder-main",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.0",
        "scipy>=1.11",
        "matplotlib>=3.7",
        "plotly>=5.15",
    ],
    extras_require={
        "live": ["yfinance>=0.2.30"],
        "dev": ["pytest>=7.0", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "vol-surface=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering",
    ],
)
