# Generated by Django 4.0.3 on 2022-03-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0005_alter_filedocxpdf_filepathpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedocxpdf',
            name='filename',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='filedocxpdf',
            name='filepath',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='filedocxpdf',
            name='filepathpdf',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='filedocxpdf',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]