# Generated by Django 4.2.3 on 2023-07-09 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OCU', 'Ocupada'), ('LIV', 'Livre'), ('RES', 'Reservada')], default='LIV', max_length=3)),
                ('numero_mesa', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Mesa',
                'verbose_name_plural': 'Mesas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField(blank=True, default='')),
                ('is_cozinha', models.BooleanField(default=False)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='GenPedidos.categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=100)),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('REL', 'Realizado'), ('INI', 'Aceito'), ('PEN', 'Pronto para entrega'), ('ENT', 'Pedido entregado'), ('FIM', 'Finalizado')], default='REL', max_length=3)),
                ('mesa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='GenPedidos.mesa')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItensPedidos', to='GenPedidos.pedido')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItensProdutos', to='GenPedidos.produto')),
            ],
            options={
                'verbose_name': 'ItemPedido',
                'verbose_name_plural': 'ItensPedidos',
            },
        ),
        migrations.CreateModel(
            name='ComandaCozinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACT', 'Aceito'), ('AGR', 'Aguardando'), ('PCP', 'Problma com pedido'), ('PRD', 'Em produção'), ('FIM', 'Finalizado')], default='AGR', max_length=3)),
                ('pedido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ComandasCozinha', to='GenPedidos.pedido')),
            ],
            options={
                'verbose_name': 'ComandasCozinha',
                'verbose_name_plural': 'ComandasCozinha',
            },
        ),
    ]
