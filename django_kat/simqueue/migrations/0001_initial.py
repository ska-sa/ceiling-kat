# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(default='New simulation', max_length=200)),
                ('observatory', models.CharField(default='MK', max_length=32, choices=[('MK', 'MeerKAT'), ('K7', 'KAT-7'), ('JA', 'JVLA-A')])),
                ('output', models.CharField(default='I', verbose_name='Output type', max_length=1, choices=[('I', 'Image'), ('V', 'Visibilities')])),
                ('sefd', models.FloatField(null=True, blank=True, verbose_name='SEFD', help_text='System defaults will be used if left blank')),
                ('sky_type', models.CharField(default='T', max_length=1, choices=[('T', 'Tigger-LSM'), ('A', 'ASCII'), ('F', 'FITS'), ('S', 'KATALOG')])),
                ('sky_model', models.FileField(blank=True, upload_to='sky')),
                ('katalog_id', models.CharField(default='NV', verbose_name='KATALOG', help_text='Choose from our sky catalogs', max_length=64, blank=True, choices=[('NV', 'nvss6deg'), ('S3', 'scubed1deg'), ('K3', '3c147_field'), ('K4', '3c147_field_no_core')])),
                ('radius', models.FloatField(blank=True, default=0.5, verbose_name='Radius', help_text='Radius of degrees')),
                ('fluxrange', models.CharField(default='0.001-1', verbose_name='Flux range', help_text='Flux range in Jy', max_length=32)),
                ('ms_dec', models.CharField(default='-30d0m0s', verbose_name='Declination', help_text='in dms', max_length=32)),
                ('ms_ra', models.CharField(default='0h0m0s', verbose_name='Right ascension', help_text='in hms', max_length=32)),
                ('add_noise', models.BooleanField(default=True)),
                ('vis_noise_std', models.FloatField(default=0, verbose_name='Visibility noise std', help_text='Generates from SEFD if 0')),
                ('ms_synthesis', models.FloatField(default=0.25, verbose_name='Synthesis time', help_text='in hours')),
                ('ms_scan_length', models.FloatField(blank=True, default=0.25, verbose_name='Scan length', help_text='in hours')),
                ('ms_start_time', models.FloatField(blank=True, default=-0.125, verbose_name='Initial hour angle', help_text='in hours')),
                ('ms_dtime', models.IntegerField(default=10, verbose_name='Integration time', help_text='in seconds')),
                ('ms_freq0', models.FloatField(default=700, verbose_name='Start frequency', help_text='in MHz')),
                ('ms_dfreq', models.FloatField(default=50000.0, verbose_name='Channel width', help_text='in kHz')),
                ('ms_nchan', models.IntegerField(default=1, verbose_name='Channels', help_text='Number of frequency channels')),
                ('ds_parallactic_angle_rotation', models.BooleanField(default=True, verbose_name='Parallactic Angle Rotation', help_text='Can not be applied to FITS skymodels at the moment.')),
                ('ds_primary_beam', models.CharField(default='M', verbose_name='Primary Beam', max_length=1, choices=[('M', 'MeerKAT-1'), ('N', 'MeerKAT-2'), ('O', 'MeerKAT-3'), ('K', 'KAT-7'), ('W', 'WSRT'), ('J', 'JVLA')])),
                ('ds_feed_angle', models.FloatField(default=0, verbose_name='Feed angle')),
                ('cr_amp_phase_gains', models.FloatField(default=1, verbose_name='Amplitude Phase Gains')),
                ('cr_pointing_error', models.FloatField(default=0)),
                ('cr_rfi', models.FloatField(default=0)),
                ('imager', models.CharField(default='LW', verbose_name='Imager', max_length=32, choices=[('LW', 'LWIMAGER'), ('WS', 'WSCLEAN'), ('CA', 'CASA')])),
                ('im_npix', models.IntegerField(default=512, verbose_name='Image size', help_text='in pixels')),
                ('im_cellsize', models.FloatField(default=1, verbose_name='Pixel size', help_text='in arcseconds')),
                ('im_weight', models.CharField(default='N', verbose_name='uv-Weighting', max_length=1, choices=[('N', 'Natural'), ('U', 'Uniform'), ('B', 'Briggs')])),
                ('im_robust', models.FloatField(default=0, verbose_name='Robust', help_text='Briggs robust parameter')),
                ('im_weight_fov', models.FloatField(null=True, blank=True, verbose_name='Weight FoV', help_text='in arcminutes')),
                ('im_wprojplanes', models.IntegerField(default=0, verbose_name='w-Projection planes')),
                ('im_mode', models.CharField(default='C', verbose_name='Imaging mode', max_length=1, choices=[('C', 'channel'), ('M', 'mfs'), ('V', 'velocity'), ('F', 'frequency')])),
                ('channelise', models.IntegerField(default=0, verbose_name='Image channelise', help_text='0 means average all, 1 per channel, etc.')),
                ('im_stokes', models.CharField(default='I', verbose_name='Stokes', max_length=4)),
                ('make_psf', models.BooleanField(default=False, verbose_name='Make PSF')),
                ('lwimager', models.BooleanField(default=False, verbose_name='Deconvolve with me!')),
                ('lwimager_niter', models.IntegerField(default=1000, verbose_name='NITER')),
                ('lwimager_gain', models.FloatField(default=0.1, verbose_name='Loop gain')),
                ('lwimager_threshold', models.FloatField(default=0, verbose_name='Clean Threshold', help_text='In Jy')),
                ('lwimager_operation', models.CharField(default='C', verbose_name='Clean algorithm', max_length=1, choices=[('C', 'csclean'), ('H', 'hogbom'), ('D', 'clark'), ('M', 'multiscale')])),
                ('lwimager_cyclefactor', models.FloatField(default=1.5, verbose_name='Cycle factor')),
                ('lwimager_cyclespeedup', models.FloatField(default=-1, verbose_name='Cycle speed up')),
                ('lwimager_stoppointmode', models.FloatField(default=-1, verbose_name='Stop point mode,')),
                ('lwimager_nscales', models.IntegerField(default=4, verbose_name='Scales for MS clean')),
                ('lwimager_uservector', models.CharField(null=True, blank=True, verbose_name='Clean scales', help_text='Comma seperated scales in pixels', max_length=64)),
                ('wsclean', models.BooleanField(default=False, verbose_name='Deconvolve with me!')),
                ('wsclean_niter', models.IntegerField(default=1000, verbose_name='NITER')),
                ('wsclean_gain', models.FloatField(default=0.1, verbose_name='Minor loop gain')),
                ('wsclean_mgain', models.FloatField(default=0.1, verbose_name='Major loop gain')),
                ('wsclean_threshold', models.FloatField(default=0, verbose_name='Clean Threshold', help_text='In Jy')),
                ('wsclean_joinpolarizations', models.BooleanField(default=False, verbose_name='Join polarizations')),
                ('wsclean_joinchannels', models.BooleanField(default=False, verbose_name='Join channels')),
                ('wsclean_multiscale', models.BooleanField(default=False, verbose_name='Multiscale clean')),
                ('wsclean_multiscale_dash_threshold_dash_bias', models.FloatField(default=0.7, verbose_name='Multi scale threshold bias')),
                ('wsclean_multiscale_dash_scale_dash_bias', models.FloatField(default=0.6, verbose_name='Multi scale bias')),
                ('wsclean_cleanborder', models.FloatField(default=5, verbose_name='Clean border', help_text='In percentage of image width/height')),
                ('wsclean_smallpsf', models.BooleanField(default=False, verbose_name='Small PSF', help_text='Resize the psf to speed up minor clean iterations')),
                ('wsclean_nonegative', models.BooleanField(default=False, verbose_name='No negative', help_text='Do not allow negative components during cleaning')),
                ('wsclean_stopnegative', models.BooleanField(default=False, verbose_name='Stop on negative')),
                ('wsclean_beamsize', models.CharField(null=True, blank=True, verbose_name='Restoring beam size', help_text='In arcseconds', max_length=32)),
                ('casa', models.BooleanField(default=False, verbose_name='Deconvolve with me!')),
                ('casa_niter', models.IntegerField(default=1000, verbose_name='NITER')),
                ('casa_threshold', models.FloatField(default=0, verbose_name='Threshold')),
                ('casa_gain', models.FloatField(default='0.1', verbose_name='Loop Gain', help_text='Clean Loop gain')),
                ('casa_psfmode', models.CharField(default='CL', verbose_name='PSF mode', max_length=32, choices=[('CL', 'clark'), ('CS', 'clarkstokes'), ('H', 'hogbom')])),
                ('casa_imagermode', models.CharField(blank=True, default='csclean', verbose_name='Imager mode', max_length=32, choices=[('C', 'csclean'), ('M', 'mosiac')])),
                ('casa_gridmode', models.CharField(default='W', verbose_name='Grid mode', help_text='A-projection only works JVLA', max_length=32, blank=True, choices=[('W', 'widefield'), ('A', 'aprojection')])),
                ('casa_nterms', models.IntegerField(default=1, verbose_name='NTERMS', help_text='See CASA clean task')),
                ('casa_reffreq', models.FloatField(null=True, blank=True, verbose_name='MFS ref Frequency', help_text='in MHz')),
                ('casa_multiscale', models.CharField(null=True, blank=True, verbose_name='Multiscale', help_text='Deconvolution scales in pixels', max_length=200)),
                ('casa_negcomponent', models.FloatField(default=-1, verbose_name='Negative Components', help_text='See CASA clean task')),
                ('casa_smallscalebias', models.FloatField(default=0.6, verbose_name='Small scale bias', help_text='See CASA clean task')),
                ('casa_restoringbeam', models.CharField(null=True, blank=True, verbose_name='Restoring beam', max_length=32)),
                ('casa_cyclefactor', models.FloatField(default=1.5, verbose_name='Cycle factor')),
                ('casa_cyclespeedup', models.FloatField(default=-1, verbose_name='Cycle speed up')),
                ('moresane', models.BooleanField(default=False, verbose_name='Deconvolve with me!')),
                ('moresane_scalecount', models.IntegerField(null=True, blank=True, verbose_name='Scale count', help_text='See MORESANE help')),
                ('moresane_subregion', models.IntegerField(null=True, blank=True, verbose_name='Sub region', help_text='Inner region to deconvolve in pixels')),
                ('moresane_startscale', models.FloatField(default=1, verbose_name='Start scale')),
                ('moresane_stopscale', models.FloatField(default=20, verbose_name='Stop scale')),
                ('moresane_sigmalevel', models.FloatField(default=3, verbose_name='Threshold level', help_text='in sigma above noise')),
                ('moresane_loopgain', models.FloatField(default='0.1', verbose_name='Loop gain')),
                ('moresane_tolerance', models.FloatField(default=0.75, verbose_name='Tolerance')),
                ('moresane_accuracy', models.FloatField(default=1e-06, verbose_name='Accuracy')),
                ('moresane_majorloopmiter', models.IntegerField(default=100, verbose_name='Major loop iterations')),
                ('moresane_minorloopmiter', models.IntegerField(default=50, verbose_name='Minor loop iterations')),
                ('moresane_convmode', models.CharField(default='C', verbose_name='Convolution mode', max_length=32, choices=[('C', 'circular'), ('L', 'linear')])),
                ('moresane_enforcepositivity', models.BooleanField(default=False, verbose_name='Enforce Positivity')),
                ('moresane_edgesupression', models.BooleanField(default=False, verbose_name='Edge Suppression')),
                ('moresane_edgeoffset', models.FloatField(default=0, verbose_name='Edge offset')),
                ('moresane_mfs', models.BooleanField(default=False, verbose_name='MFS map', help_text='Comes with an spi map')),
                ('moresane_spi_dash_sigmalevel', models.FloatField(default=10, verbose_name='spi threshold level', help_text='In sigma above noise')),
                ('state', models.CharField(default='S', max_length=1, choices=[('S', 'scheduled'), ('R', 'running'), ('C', 'crashed'), ('F', 'finished')])),
                ('started', models.DateTimeField(null=True, blank=True)),
                ('finished', models.DateTimeField(null=True, blank=True)),
                ('log', models.FileField(null=True, blank=True, upload_to='')),
                ('console', models.TextField(null=True, blank=True)),
                ('task_id', models.CharField(null=True, blank=True, max_length=36)),
                ('results_uvcov', models.FileField(null=True, blank=True, upload_to='uvcov')),
                ('results_lwimager_dirty', models.FileField(null=True, blank=True, upload_to='lwimager_dirty')),
                ('results_lwimager_model', models.FileField(null=True, blank=True, upload_to='lwimager_model')),
                ('results_lwimager_residual', models.FileField(null=True, blank=True, upload_to='lwimager_residual')),
                ('results_lwimager_restored', models.FileField(null=True, blank=True, upload_to='lwimager_restored')),
                ('results_casa_dirty', models.FileField(null=True, blank=True, upload_to='casa_dirty')),
                ('results_casa_model', models.FileField(null=True, blank=True, upload_to='casa_model')),
                ('results_casa_residual', models.FileField(null=True, blank=True, upload_to='casa_residual')),
                ('results_casa_restored', models.FileField(null=True, blank=True, upload_to='casa_restored')),
                ('results_wsclean_dirty', models.FileField(null=True, blank=True, upload_to='wsclean_dirty')),
                ('results_wsclean_model', models.FileField(null=True, blank=True, upload_to='wsclean_model')),
                ('results_wsclean_residual', models.FileField(null=True, blank=True, upload_to='wsclean_residual')),
                ('results_wsclean_restored', models.FileField(null=True, blank=True, upload_to='wsclean_restored')),
                ('results_moresane_dirty', models.FileField(null=True, blank=True, upload_to='moresane_dirty')),
                ('results_moresane_model', models.FileField(null=True, blank=True, upload_to='moresane_model')),
                ('results_moresane_residual', models.FileField(null=True, blank=True, upload_to='moresane_residual')),
                ('results_moresane_restored', models.FileField(null=True, blank=True, upload_to='moresane_restored')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
