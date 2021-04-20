# Generated by Django 3.2 on 2021-04-18 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_alter_curso_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capitulo', models.IntegerField(default=1)),
                ('tema', models.IntegerField(default=1)),
                ('detalle', models.IntegerField(default=1)),
                ('culminado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
            ],
        ),
    ]
