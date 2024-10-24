from Core.models import HeadMenu, DropMenu


def BuilderMenu(request):
    menu = ''
    head = HeadMenu.objects.all()
    for item in head:
        if item.title is False:
            item_line = f'''
            <div class="mdc-list-item mdc-drawer-item">
              <a class="mdc-drawer-link" href="{ item.url }">
                <i class="material-icons mdc-list-item__start-detail mdc-drawer-item-icon" aria-hidden="true">{ item.icon }</i>
                    { item.name }
              </a>
            </div>
            '''
            menu = menu + item_line
        else:
            path_start = f'''
            <div class="mdc-list-item mdc-drawer-item">
              <a class="mdc-expansion-panel-link" href="#" data-toggle="expansionPanel" data-target="{ item.gk_name }">
                <i class="material-icons mdc-list-item__start-detail mdc-drawer-item-icon" aria-hidden="true">{ item.icon }</i>
                { item.name }
                <i class="mdc-drawer-arrow material-icons">chevron_right</i>
              </a>
              <div class="mdc-expansion-panel" id="{ item.gk_name }">
                <nav class="mdc-list mdc-drawer-submenu">
            
            '''
            deep_menu_item = ''
            items_drop = DropMenu.objects.filter(headmenu=item)
            for deep_item in items_drop:
                line = f'''
                  <div class="mdc-list-item mdc-drawer-item">
                    <a class="mdc-drawer-link" href="{ deep_item.url }">
                      { deep_item.name }
                    </a>
                  </div>
                '''
                deep_menu_item = deep_menu_item + line
                
            path_end = '''
                </nav>
              </div>
            </div>
            '''
            path_full = path_start + deep_menu_item + path_end 
            menu = menu + path_full
        
    return menu
    
    
    
    
