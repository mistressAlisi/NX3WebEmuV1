# Generated by Django 3.2.8 on 2021-10-20 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NX3', '0005_auto_20211020_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemstate',
            name='userProfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='NX3.userprofile', verbose_name='User Profile'),
        ),
        migrations.AddField(
            model_name='systemstate',
            name='userProfileStep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='NX3.userprofilestep', verbose_name='User Profile Step'),
        ),
    ]
