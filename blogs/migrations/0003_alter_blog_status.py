# Generated by Django 5.0.7 on 2024-07-28 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(choices=[('Draft', 'Draft'), ('Published', 'Publish')], default=0, max_length=20),
        ),
    ]
