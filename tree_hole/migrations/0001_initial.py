from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)), ('description', models.TextField()),
                ('author_name', models.CharField(default='Anonymous student', max_length=80)),
                ('discipline', models.CharField(max_length=50)), ('tags', models.CharField(blank=True, max_length=240)),
                ('hearts', models.PositiveIntegerField(default=0)), ('created_at', models.DateTimeField(auto_now_add=True)),
            ], options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='KnowledgeBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()), ('author_name', models.CharField(default='Anonymous student', max_length=80)),
                ('discipline', models.CharField(blank=True, max_length=50)), ('created_at', models.DateTimeField(auto_now_add=True)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='tree_hole.challenge')),
            ], options={'ordering': ['created_at']},
        ),
    ]
