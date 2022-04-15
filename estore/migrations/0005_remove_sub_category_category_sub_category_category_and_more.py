# Generated by Django 4.0.3 on 2022-04-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0004_alter_product_options_product_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='category',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='estore.category'),
        ),
        migrations.RemoveField(
            model_name='sub_sub_category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='sub_sub_category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, related_name='sub_category', to='estore.sub_category'),
        ),
    ]
