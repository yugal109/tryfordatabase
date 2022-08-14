# Generated by Django 4.1 on 2022-08-08 03:41

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_blog_created_at_career_created_at_contact_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=350)),
                ('phonenumber', models.CharField(max_length=10)),
                ('education_status', models.CharField(choices=[('SEE', 'SEE')], max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
