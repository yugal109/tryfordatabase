# Generated by Django 4.1 on 2022-08-08 02:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=350)),
                ('phonenumber', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]