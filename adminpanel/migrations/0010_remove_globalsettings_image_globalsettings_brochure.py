# Generated by Django 4.2.3 on 2023-08-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0009_alter_navigation_page_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globalsettings',
            name='image',
        ),
        migrations.AddField(
            model_name='globalsettings',
            name='brochure',
            field=models.FileField(null=True, upload_to='brochure/'),
        ),
    ]
