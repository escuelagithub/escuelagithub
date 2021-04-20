# Generated by Django 3.2 on 2021-04-18 19:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0003_capitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('capitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitante.capitulo')),
            ],
        ),
    ]
