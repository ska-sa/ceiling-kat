from django.db.models import Model, CharField, FileField, BooleanField,\
    FloatField, IntegerField


class Simulation(Model):
    SKY_TYPES = (
        ('T', 'Tigger LSM'),
        ('F', 'FITS'),
        ('S', 'Siamese Model'),
    )

    OUTPUT_TYPES = (
        ('I', 'Image'),
        ('V', 'Visibilities'),
    )

    # global settings
    name = CharField(default='New simulation', max_length=200)
    sky_type = CharField(choices=SKY_TYPES, max_length=1, default='T')
    sky_model = FileField(blank=True)
    tdl_conf_file = FileField(blank=True,
                              help_text='TDL Configuration File')
    tdl_section = CharField(blank=True, max_length=200)
    make_psf = BooleanField(default=True,
                            blank=True)
    add_noise = BooleanField(default=True,
                             blank=True)
    noise_standard_dev = FloatField(default=0)
    output = CharField(choices=OUTPUT_TYPES, max_length=1,
                       default='I')

    # observation setup
    synthesis_time = FloatField(default=1, help_text='in seconds')
    integration_time = FloatField(default=1, help_text='in seconds')
    start_frequency = FloatField(default=1, help_text='in Hz')
    channel_width = FloatField(default=1, help_text='in Hz')
    channels_per_band = IntegerField(default=1,
                                     help_text='Number of frequency channels per band')
    freq_bands = IntegerField(default=1,
                              help_text='Number of frequency bands')
    correlate = BooleanField(help_text='Autocorrelation data', default=True)
    declination = FloatField(blank=True, null=True)
    right_ascension = FloatField(blank=True, null=True)

    BEAM_TYPES = (
        ('M', 'MeerKAT 1'),
        ('N', 'MeerKAT 2'),
        ('O', 'MeerKAT 3'),
        ('K', 'KAT-7'),
        ('W', 'WSRT'),
        ('J', 'JVLA'),
    )

    # dish settings
    am_phase_gains = FloatField(default=1, help_text='Amplitude Phase Gains')
    par_angle_rot = BooleanField(help_text='Parallactic Angle Rotation',
                                 default=True)
    primary_beam = CharField(choices=BEAM_TYPES, max_length=1, default='M')

    # corruptions
    corrup_am_phase_gains = FloatField(help_text='Amplitude Phase Gains',
                                       default=1)
    pointing_errors = FloatField(default=0)
    rfi = FloatField(default=0)

    WEIGHTING_TYPES = (
        ('N', 'Natural'),
        ('U', 'Uniform'),
        ('B', 'Briggs'),
    )

    IMAGING_TYPES = (
        ('C', 'Channel'),
        ('M', 'MFS'),
    )

    CHANNELISE_TYPES = (
        ('A', 'Average all'),
        ('E', 'Image every channel'),
        ('C', 'Custom'),
    )


    # imaging settings
    pixels = IntegerField(default=1)
    pixel_width = FloatField(help_text='in arcseconds',
                             default=1)
    uv_weighting = CharField(choices=WEIGHTING_TYPES, max_length=1,
                             default='N')
    weight_fov = FloatField(help_text='in arcminutes',
                            default=1)
    w_projection_planes = IntegerField(default=1)
    imaging_mode = CharField(choices=IMAGING_TYPES, max_length=1,
                             default='C')
    spectral_window = FloatField(default=1)
    num_channels = IntegerField(default=1)
    image_channelise = CharField(choices=CHANNELISE_TYPES, max_length=1,
                                 default='A')
    stokes = CharField(default='Q', max_length=5)

    DECONV_TYPES = (
        ('C', 'csclean'),
        ('H', 'hogbom'),
        ('D', 'clark'),
        ('M', 'multiscale'),
    )

    # deconvolution settings
    cleaning = BooleanField(default=True)
    Deconv_alg = CharField(choices=DECONV_TYPES, max_length=1, default='c')
    clean_scales = FloatField(default=1)
    num_scales = FloatField(default=1)
    num_clean_iter = IntegerField(help_text='number of clean iterations',
                                  default=1)
    clean_threshold = FloatField(help_text='in mJy',
                                 default=1)

    def __str__(self):
        return self.name
