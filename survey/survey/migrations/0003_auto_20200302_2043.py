# Generated by Django 3.0.3 on 2020-03-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200302_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='direct_reports',
            field=models.ManyToManyField(blank=True, related_name='_person_direct_reports_+', to='survey.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='peers',
            field=models.ManyToManyField(blank=True, related_name='_person_peers_+', to='survey.Person'),
        ),
    ]
