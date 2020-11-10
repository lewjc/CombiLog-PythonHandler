import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="combilog-handler",  # Replace with your own username
    version="1.0.14",
    author="Lewis Cummins",
    author_email="lewisjcummins@hotmail.co.uk",
    description="Interfaces with inbuilt python logger to send logs to combilog aggregator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lewjc/combilog-pythonhandler",
    packages=setuptools.find_packages(),
    install_requires=["websocket_client", "asyncio"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)