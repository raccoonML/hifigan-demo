from argparse import Namespace

hparams = Namespace(sample_rate = 22050,
                    n_fft = 1024,
                    num_mels = 80,
                    hop_size = 256,
                    win_size = 1024,
                    fmin = 0,
                    fmax = 8000,
                    preemphasis = 0.97,
                    preemphasize = False,
                    # Settings for hifigan-style mel preprocessing
                    use_hifigan_spectrograms = True,
                    # Settings for RTVC-style mel preprocessing
                    min_level_db = -100,
                    ref_level_db = 20,
                    max_abs_value = 4.,
                    symmetric_mels = True,
                    signal_normalization = True,
                    allow_clipping_in_normalization = True,
                    # Griffin-Lim settings
                    power = 1.2,
                    griffin_lim_iters = 30,
                    # HiFi-GAN settings
                    hifigan_model_path = "saved_models/generator_v3",
                    resblock = "2",
                    upsample_rates = [8,8,4],
                    upsample_kernel_sizes = [16,16,8],
                    upsample_initial_channel = 256,
                    resblock_kernel_sizes = [3,5,7],
                    resblock_dilation_sizes = [[1,2], [2,6], [3,12]],
)
