from setuptools import setup, find_packages

setup(
    name="OptiFlowPy",
    version="1.0",
    author="Light Andy",
    author_email="andy197197@example.com",
    description="An advanced batch image compressor.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["imageio", "numpy", "Pillow", "PyQt5", "tk", "pytest", "wheel"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
