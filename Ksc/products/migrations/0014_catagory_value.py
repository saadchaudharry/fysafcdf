# Generated by Django 2.2.7 on 2020-04-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200215_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='value',
            field=models.CharField(blank=True, choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('BIRD', 'Bird'), ('FEATU0RED', 'Featured'), ('fish', 'Fishes'), ('ACCESSORIES', 'Accessories')], max_length=100, null=True),
        ),
    ]
