# Generated by Django 3.0.3 on 2020-05-15 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20200514_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_time',
            name='patient_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.patient'),
        ),
    ]
