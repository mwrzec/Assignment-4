
from ui import UI
from resource_manage import ResourceManager
from data_persistence import DataPersistence

if __name__ == '__main__':
    ui = UI()
    data_persistence = DataPersistence("data.json")
    resource_manager = ResourceManager()

    resource_manager.ress = data_persistence.data_load()

    while True:
        ui.main_menu()  
        selection = ui.user_input("Enter your choice: ")  

        if selection == '1':
            ui.make_res(resource_manager)  
        elif selection == '2':
            ui.search_res(resource_manager)  
        elif selection == '3':
            ui.edit_res(resource_manager) 
        elif selection == '4':
            ui.delete_res(resource_manager)
        elif selection == '5':
            data_persistence.data_save(resource_manager.ress)
            print("Exiting Program.")
            break
        else:
            print("Invalid Choice. Please try again.")
