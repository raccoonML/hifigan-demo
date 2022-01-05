from argparse import Namespace

hparams = Namespace(sample_rate = 16000,
                    n_fft = 800,
                    num_mels = 80,
                    hop_size = 200,
                    win_size = 800,
                    fmin = 55,
                    fmax = 7600,
                    min_level_db = -100,
                    ref_level_db = 20,
                    max_abs_value = 4.,
                    preemphasis = 0.97,
                    preemphasize = True,
                    symmetric_mels = True,
                    signal_normalization = True,
                    allow_clipping_in_normalization = True,
                    # Griffin-Lim settings
                    power = 1.2,
                    griffin_lim_iters = 30,
                    # HiFi-GAN settings
                    hifigan_model_path = "saved_models/g_00150000",
                    resblock = "1",
                    upsample_rates = [5,5,4,2],
                    upsample_kernel_sizes = [5,5,4,2],
                    upsample_initial_channel = 512,
                    resblock_kernel_sizes = [3,7,11],
                    resblock_dilation_sizes = [[1,3,5], [1,3,5], [1,3,5]],
)
