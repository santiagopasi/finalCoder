# Generated by Django 4.0.4 on 2022-05-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Altec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestos',
            name='precio',
            field=models.FloatField(null=True),
        ),
    ]