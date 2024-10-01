from setuptools import setup, find_packages

setup(
    name="sistema_bancario",
    version="1.0.0",
    description="Sistema bancário modularizado com transações de depósito, saque e exibição de extrato",
    author="Giancarlo Malfate Caprino",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
