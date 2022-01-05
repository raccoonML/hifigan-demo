# raccoonML hifigan demo

This repo adds a GUI to the awesome neural vocoder hifi-gan. This makes it easier to test quality of pretrained models. Only inference is supported. Please download a [release](https://github.com/raccoonML/hifigan-demo/releases) for the best experience.

Demo makes use of my [audiotools](https://github.com/raccoonML/audiotools) and [voicebox](https://github.com/raccoonML/voicebox) projects. This is part of a larger project to integrate the hifigan vocoder with MLRTVC (see [issue #20](https://github.com/sveneschlbeck/Multi-Language-RTVC/issues/20)).

## Announcements

* 1/5/2022: [Generator-v1](https://github.com/raccoonML/hifigan-demo/releases/tag/Generator-v1), [Generator-v2](https://github.com/raccoonML/hifigan-demo/releases/tag/Generator-v2), and [Generator-v3](https://github.com/raccoonML/hifigan-demo/releases/tag/Generator-v3) released. These are compatible with the pretrained models provided by the hifigan authors.

* 1/4/2022: [MLRTVC-v1 pretrained model](https://github.com/raccoonML/hifigan-demo/releases/tag/MLRTVC-v1) released. This is compatible with the audio settings used in the [RTVC](https://github.com/CorentinJ/Real-Time-Voice-Cloning) and [Multi-Language RTVC](https://github.com/sveneschlbeck/Multi-Language-RTVC) repos. The hifigan model is trained to only 150,000 steps at this time.

## Windows setup

1. Install Python 3.7+ if you don't have it already. GUIDE: [Installing Python on Windows](https://www.patreon.com/posts/guide-install-in-59934677).
2. Download [**hifigan-demo.zip**](https://github.com/raccoonML/hifigan-demo/releases/download/MLRTVC-v1/hifigan-demo.zip) from the [MLRTVC-v1 release](https://github.com/raccoonML/hifigan-demo/releases/tag/MLRTVC-v1).
3. Extract the zip file.
4. Create and activate a Python virtual environment. GUIDE: [Python virtual environments in Windows](https://www.patreon.com/posts/guide-python-in-59936054)
```
cd C:\path\to\hifigan-demo
python -m venv venv
venv\Scripts\activate.bat
```
5. Install dependencies
```
pip install --upgrade pip
pip install torch -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
```
6. Run the toolbox
```
python run_voicebox.py
```

## Usage

Load an audio file. A spectrogram is created using the settings in hparams.py, and displayed in the top row. At the same time, Griffin-Lim is used to vocode the spectrogram back to audio. The spectrogram of the resulting audio is calculated and displayed in the middle row.

When the "vocode" button is pressed, hifigan inference is performed on the top spectrogram. The resulting audio from hifigan can be played back. A spectrogram of hifigan audio is displayed in the bottom row.

## Screenshot

<img src="https://github.com/raccoonML/hifigan-demo/blob/master/screenshot.png?raw=true">

## Credits
* https://github.com/jik876/hifi-gan

Thanks to my Patreon supporters for making this work possible. Learn how to support me [here](https://www.patreon.com/raccoonML).
