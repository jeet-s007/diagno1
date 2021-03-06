# Generated by Django 3.0.3 on 2020-05-16 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_date_time_patient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='merge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=8)),
                ('age', models.IntegerField()),
                ('ph_no', models.IntegerField()),
                ('disease', models.CharField(max_length=100)),
                ('dates', models.DateField()),
                ('time', models.TimeField()),
                ('hospital', models.CharField(max_length=30)),
                ('dr_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.data1')),
                ('patient_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.patient')),
            ],
        ),
        migrations.DeleteModel(
            name='date_time',
        ),
    ]
