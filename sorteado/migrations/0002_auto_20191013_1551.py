# Generated by Django 2.2.6 on 2019-10-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorteado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='num_calcado',
            field=models.CharField(choices=[('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41')], max_length=2, verbose_name='Número do calçado'),
        ),
    ]
