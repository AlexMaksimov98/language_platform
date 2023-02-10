# Generated by Django 4.1.5 on 2023-02-09 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grammar_section', '0002_grammarsection_slug_grammartopic_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammartopic',
            name='type_of_topic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='GrammarTheorySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('rule', models.CharField(blank=True, max_length=500)),
                ('questions', models.CharField(blank=True, max_length=50)),
                ('functions', models.CharField(blank=True, max_length=500)),
                ('examples', models.CharField(blank=True, max_length=500)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grammar_section.grammartopic')),
            ],
        ),
    ]