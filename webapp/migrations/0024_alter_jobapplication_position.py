# Generated by Django 4.1 on 2022-08-10 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_jobapplication_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='position',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.career'),
        ),
    ]
