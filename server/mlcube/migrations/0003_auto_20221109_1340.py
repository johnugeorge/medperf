# Generated by Django 3.2.16 on 2022-11-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlcube', '0002_auto_20220624_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlcube',
            name='mlcube_hash',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mlcube',
            name='parameters_hash',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mlcube',
            name='git_parameters_url',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterUniqueTogether(
            name='mlcube',
            unique_together={('image_tarball_url', 'image_tarball_hash', 'additional_files_tarball_url', 'additional_files_tarball_hash', 'git_mlcube_url', 'mlcube_hash', 'git_parameters_url', 'parameters_hash')},
        ),
    ]
