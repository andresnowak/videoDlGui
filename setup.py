import setuptools

setuptools.setup(
    name="videoDlGui",
    version="1.0",
    author="Andres Nowak",
    author_email="",
    description="downloads a youtube video in mp3",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "videodlgui =  videoDl.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
