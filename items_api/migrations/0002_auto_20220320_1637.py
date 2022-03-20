# Generated by Django 3.1.7 on 2022-03-20 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0002_auto_20220317_0133'),
        ('items_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auth_api.useraccount'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]