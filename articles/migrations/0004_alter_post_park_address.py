# Generated by Django 3.2.13 on 2022-11-18 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
        ('articles', '0003_alter_post_park_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='park_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
    ]
