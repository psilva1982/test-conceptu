from django.db import migrations

def create_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    users = [
        'admin',
        'test',
    ]

    for user in users:
         obj = User.objects.create_user(
             username=user,
             password='1234',
             is_active=True,
             is_superuser=True
         )
         obj.save()

def load_categories(apps, schema_editor):
    Category = apps.get_model('acervo', 'Category')
    categories_lst = [
        'Romance',
        'Ação',
        'Ficção Científica',
        'Suspense',
        'Terror'
        'Geografia',
        'História'
    ]

    for cat in categories_lst: 
        obj = Category.objects.create(name=cat)
        obj.save()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('acervo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(load_categories, reverse_code=migrations.RunPython.noop),
    ]