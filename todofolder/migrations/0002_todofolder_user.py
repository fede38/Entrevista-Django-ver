# Generated by Django 3.1.5 on 2021-01-21 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('todofolder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todofolder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.usuario'),
            preserve_default=False,
        ),
    ]
