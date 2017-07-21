from menus.models import MenuItem

def main_menu_processor(request):
    try:
        main_menu_root = MenuItem.objects.get(slug='menu-principal')
        return {'main_menu_items': main_menu_root}
    except MainMenu.DoesNotExist:
        return {'main_menu_items': []}
