# Generated by Django 4.1.3 on 2022-12-03 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_cases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='url',
            new_name='slug',
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(blank=True, max_length=10)),
                ('topic_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practice_cases.topic')),
            ],
        ),
    ]
