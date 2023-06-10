# Generated by Django 4.2.1 on 2023-06-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareafric_app', '0005_remove_elearningregistration_interests_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elearningregistration',
            name='agree_to_newsletters',
        ),
        migrations.RemoveField(
            model_name='elearningregistration',
            name='contact_options',
        ),
        migrations.AlterField(
            model_name='elearningregistration',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='elearningregistration',
            name='contact_options',
            field=models.CharField(blank=True, choices=[('improveCapacity', 'To help improve on my professional and corporate capacity.'), ('dreamJob', 'To help me get my dream job.'), ('paidInternship', 'To help me access opportunities for paid internship opportunities.'), ('startupBusiness', 'To help me start up my new business.'), ('strengthenLeadership', 'To strengthen my leadership capabilities.'), ('allOfTheAbove', 'All of the above.')], max_length=20, null=True),
        ),
    ]
