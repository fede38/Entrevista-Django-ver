# Generated by Django 3.1.5 on 2021-01-19 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todofolder', '0001_initial'),
        ('todoitem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todofolder.todofolder'),
            preserve_default=False,
        ),
    ]
