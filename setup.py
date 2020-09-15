from setuptools import setup

VERSION = '1.1.3.1'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="awscli-data-mock",
    version=VERSION,
    description="Mocks json data from aws cli responses for testting and privacy porpouses",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="test mock privacy aws cli",
    url="https://github.com/danilocgsilva/awscli-data-mock",
    author="Danilo Carlos de Góes Silva",
    author_email="contact@danilocgsilva.me",
    packages=["awsclimock"],
    entry_points={"console_scripts": ["awsclimock=awsclimock.__main__:main"],},
    include_package_data=True
)
