# Generated by Django 2.0.7 on 2018-07-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_auto_20180801_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not-specified'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]