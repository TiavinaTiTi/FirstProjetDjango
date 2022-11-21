# Generated by Django 4.0.5 on 2022-06-21 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('produit', '0001_initial'),
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client'),
        ),
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='status',
            field=models.CharField(choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200, null=True),
        ),
    ]
