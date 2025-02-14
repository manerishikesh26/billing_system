# Generated by Django 5.0.4 on 2024-05-07 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.product')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='products',
            field=models.ManyToManyField(through='billing.BillItem', to='billing.product'),
        ),
    ]
