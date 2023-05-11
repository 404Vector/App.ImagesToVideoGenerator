## Setup

### Install FFmpeg

>for Debian/Ubuntu
``` bash
sudo apt install ffmpeg
```

>for OS X, etc.
``` bash
brew install ffmpeg
```

>or Official download link

-> [Link](https://ffmpeg.org/download.html)

>설치 여부 확인
``` bash
ffmpeg

>>ffmpeg version 4.2.7-0ubuntu0.1 Copyright (c) 2000-2022 the FFmpeg developers
  built with gcc 9 (Ubuntu 9.4.0-1ubuntu1~20.04.1)
```

### Install Python

>Official download link : 

-> [Link](https://www.python.org/downloads/release/python-3810/)

### Install Pipenv

``` bash
pip install pipenv
```

### Install Python Packages

> Change Directory

``` bash
cd {YOUR DIRECTORY}

example)
cd ./App.ImagesToVideoGenerator
```

> Install Packages
``` bash
pipenv install
```

> Setting for Jupyter & Voila
``` bash
jupyter labextension install @jupyter-voila/jupyterlab-preview
jupyter serverextension enable voila --sys-prefix
```