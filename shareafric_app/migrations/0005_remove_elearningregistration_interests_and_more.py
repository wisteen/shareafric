# Generated by Django 4.2.1 on 2023-06-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareafric_app', '0004_remove_mentorregistration_professional_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elearningregistration',
            name='interests',
        ),
        migrations.AddField(
            model_name='elearningregistration',
            name='elearning_interest',
            field=models.CharField(blank=True, choices=[('improveCapacity', 'To help improve on my professional and corporate capacity.'), ('dreamJob', 'To help me get my dream job.'), ('paidInternship', 'To help me access opportunities for paid internship opportunities.'), ('startupBusiness', 'To help me start up my new business.'), ('strengthenLeadership', 'To strengthen my leadership capabilities.'), ('allOfTheAbove', 'All of the above.')], max_length=20, null=True),
        ),
    ]
