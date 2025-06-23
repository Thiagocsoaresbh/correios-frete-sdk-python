from setuptools import setup, find_packages

setup(
    name="correios_frete_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Seu Nome",
    description="SDK simples para cálculo de frete dos Correios (PAC e SEDEX)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/correios_frete_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
