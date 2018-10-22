# Generated by Django 2.1.2 on 2018-10-22 07:40

from django.db import migrations, models
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20181016_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, default='', null=True, validators=[photos.validators.badwords_detector]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(choices=[('QUE', 'Quentin Tarantino'), ('DSH', 'Dr. Schutz')], max_length=3),
        ),
    ]
