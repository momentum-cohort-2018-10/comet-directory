# Generated by Django 2.1.4 on 2018-12-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181210_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='link',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]
