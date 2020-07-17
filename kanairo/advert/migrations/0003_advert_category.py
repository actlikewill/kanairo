# Generated by Django 3.0.7 on 2020-07-17 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='category',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='advert.Category'),
            preserve_default=False,
        ),
    ]