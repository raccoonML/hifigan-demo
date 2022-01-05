from raccoonML.voicebox_project import Sample_Project as Sample_Vocoder_Project
from raccoonML.voicebox.vocoder import Voicebox as Voicebox_Vocoder

if __name__ == "__main__":
    # Define the Voicebox project type
    Sample_Project = Sample_Vocoder_Project
    Voicebox = Voicebox_Vocoder
    window_title = "HiFi-GAN Demo Voicebox"
    
    # Initialize the project
    sample_project = Sample_Project()

    # Start hifigan voice UI for project
    Voicebox(sample_project, window_title=window_title)
