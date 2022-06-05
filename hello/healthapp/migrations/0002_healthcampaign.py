# Generated by Django 4.0.3 on 2022-03-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthCampaign',
            fields=[
                ('campaig_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('organizer_name', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('pic_name', models.ImageField(default='', max_length=255, upload_to='healthapp/campaign_pic')),
            ],
        ),
    ]
