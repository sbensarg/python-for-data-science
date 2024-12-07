import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="sbensarg",
    author_email="sbensarg@student.1337.ma",
    description="A sample test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sbensarg",
    license="MIT",
    python_requires=">=3.10"
)
