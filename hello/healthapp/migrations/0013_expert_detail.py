# Generated by Django 4.0.3 on 2022-04-05 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0012_tips'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(max_length=45)),
                ('skills', models.CharField(max_length=45)),
                ('about', models.TextField()),
                ('highest_qualification', models.CharField(max_length=45)),
                ('status', models.CharField(default='not', max_length=45)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='healthapp.healthexperts')),
            ],
        ),
    ]
