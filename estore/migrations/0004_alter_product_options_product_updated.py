# Generated by Django 4.0.3 on 2022-04-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0003_auto_20220308_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-updated', '-release_date']},
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
