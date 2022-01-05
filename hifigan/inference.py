import os
import torch
from hifigan.models import Generator

class Hifigan():
    def __init__(self, hparams):
        # Setup
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')

        # Init generator
        self.generator = Generator(hparams).to(self.device)

        state_dict_g = self.load_checkpoint(hparams.hifigan_model_path)
        self.generator.load_state_dict(state_dict_g['generator'])

        self.generator.eval()
        self.generator.remove_weight_norm()
        

    def load_checkpoint(self, filepath):
        assert os.path.isfile(filepath)
        print("Loading '{}'".format(filepath))
        checkpoint_dict = torch.load(filepath, map_location=self.device)
        print("Complete.")
        return checkpoint_dict


    def inference(self, mel):
        with torch.no_grad():
            y_g_hat = self.generator(torch.from_numpy(mel).to(self.device))
            audio = y_g_hat.squeeze()
            audio = audio.cpu().numpy()
            return audio
