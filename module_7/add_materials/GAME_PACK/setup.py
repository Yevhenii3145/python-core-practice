from setuptools import setup, find_namespace_packages

setup(
    name="Turt33le_Ra445ce",
    version="0.0.1",
    description="Turtle Race game by Python",
    author="Eugen",
    author_email="zakolochennoe457@gmail.com",
    url="https://github.com/Yevhenii3145/python-core-practice",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['startgame=turtle_race.main:run']}
)
# data_files=[('turtle_rale', ['turtle_race/score.bin'])],
