import librosa
import numpy as np
from raccoonML.audiotools import audio
from hparams import hparams
from hifigan.inference import Hifigan

"""
This helps implement a user interface for a vocoder.

Required elements for the vocoder UI are:
self.sample_rate
self.source_action
self.vocode_action
"""

class Sample_Project:
    def __init__(self):
        # Property needed for voicebox
        self.sample_rate = hparams.sample_rate

        # Initialization for project
        self.source_spec = None
        self.hifigan = Hifigan(hparams)

    """
    The following action methods are called by Voicebox on button press
    Source: [Load] --> source_action
    Vocode: [Vocode] --> vocode_action
    """

    def source_action(self, wav):
        # The vocoder toolbox also vocodes the spectrogram with Griffin-Lim for comparison.
        # Inputs: wav (from voicebox)
        # Outputs: spec, wav_GL, spec_GL (to voicebox)
        self.source_spec = audio.melspectrogram(wav, hparams)
        wav_GL = audio.inv_mel_spectrogram(self.source_spec, hparams)
        spec_GL = audio.melspectrogram(wav_GL, hparams)
        return self.source_spec.T, wav_GL, spec_GL.T

    def vocode_action(self):
        # For this vocoder project, we will use hifigan as the vocoder.
        # Inputs: None
        # Outputs: wav, spec (to voicebox)
        
        wav = self.hifigan.inference(np.expand_dims(self.source_spec,axis=0))
        spec = audio.melspectrogram(wav, hparams)
        return wav, spec.T
