# cut-video

A simple program using python to extract some section from a video file

## Getting Started

Install [pipenv](https://pypi.org/project/pipenv/) to manage the virtual environment for the project

```bash
pip install pipenv
```

Then set the virtual environment on and install all the dependencies

```bash
pipenv install
```
## Run the project

Run the **cut-video.py** file. There are some arguments to specify:

|Argument|Utilty|
|--------|-------|
|rute|The rute/name of the video file|
|start|The start time to cut in seconds|
|end|The start time to cut in seconds|
|_NAME_ (optional)|name or rute of the final cutted video|

___For default the name of the final video will be test.mp4___

For example, for extract the first 5 seconds from the video _a.mp4_ located in the current folder:

```bash
python cut-video.py a.mp4 0 5
```