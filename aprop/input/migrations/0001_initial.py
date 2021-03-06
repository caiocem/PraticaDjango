# Generated by Django 2.2.5 on 2020-03-09 15:10

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Colaboradores',
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('colaboradores', models.ManyToManyField(to='input.Colaborador')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Apropriacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('referencia', models.DateField(validators=[django.core.validators.RegexValidator(regex='[0-9]{4}-[0-9]{2}-[0-9]{2}')])),
                ('duracao', models.DurationField(validators=[django.core.validators.MinValueValidator(datetime.timedelta(0)), django.core.validators.MaxValueValidator(datetime.timedelta(seconds=86340))])),
                ('descricao', models.CharField(max_length=2048)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='input.Colaborador')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='input.Projeto')),
            ],
            options={
                'verbose_name_plural': 'Apropria????es',
            },
        ),
    ]
