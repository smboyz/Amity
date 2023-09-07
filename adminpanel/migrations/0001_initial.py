# Generated by Django 4.2.3 on 2023-07-28 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(max_length=100)),
                ('SiteContact', models.CharField(max_length=50)),
                ('SiteEmail', models.EmailField(max_length=254)),
                ('SiteAddress', models.CharField(max_length=500)),
                ('Sitedescription', models.CharField(max_length=500)),
                ('Sitelicence', models.CharField(max_length=30)),
                ('Sitetwitterlink', models.CharField(max_length=30)),
                ('Sitefacebooklink', models.CharField(max_length=30)),
                ('Sitelinkdinlink', models.CharField(max_length=30)),
                ('Siteinstagram', models.CharField(max_length=30)),
                ('Siteyoutubelink', models.CharField(max_length=30)),
                ('logo', models.ImageField(default=None, max_length=200, null=True, upload_to='Global/')),
                ('image', models.ImageField(upload_to='Global/')),
            ],
        ),
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=50)),
                ('position', models.IntegerField()),
                ('page_type', models.CharField(blank=True, choices=[('Home', 'Home'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Documents', 'Documents'), ('About Company', 'About Company'), ('Registration/Approval', 'Registration/Approval'), ('About', 'About'), ('Our Message', 'Our Message'), ('Our Commitment', 'Our Commitment'), ('Contact', 'Contact'), ('Organizational Chart', 'Organizational Chart'), ('Demand Letter', 'Demand Letter'), ('Job Seeker', 'Job Seeker'), ('Recruiting Procedure', 'Recruiting Procedure'), ('Recruiting Documents', 'Recruiting Documents'), ('Gallery', 'Gallery'), ('Slider', 'Slider'), ('Service', 'Service'), ('Newspaper Vacancy', 'Newspaper Vacancy'), ('Group', 'Group'), ('Normal', 'Normal')], max_length=50, null=True)),
                ('title', models.CharField(max_length=200)),
                ('title1', models.CharField(max_length=200, null=True)),
                ('short_desc', models.TextField(null=True)),
                ('long_desc', models.TextField(null=True)),
                ('desc', models.TextField(null=True)),
                ('bannerimage', models.ImageField(upload_to='about/')),
                ('meta_title', models.CharField(max_length=100, null=True)),
                ('meta_keyword', models.CharField(max_length=100, null=True)),
                ('icon_image', models.ImageField(upload_to='about/')),
                ('slider_image', models.ImageField(null=True, upload_to='about/')),
                ('banner_image1', models.ImageField(null=True, upload_to='about/')),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='adminpanel.navigation')),
            ],
        ),
    ]
