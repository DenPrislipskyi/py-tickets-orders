# Generated by Django 4.1 on 2023-12-02 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_alter_ticket_movie_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='movie_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='cinema.moviesession'),
        ),
    ]
