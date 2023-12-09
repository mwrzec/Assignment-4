from ui import UI
from resource_manage import res_manage
from data_persistence import DataPersistence
if __name__ == 'main':
    ui = UI()
    data_persistence = DataPersistence("data.json")
    resource_manage = res_manage()

    resource_manage.ress = data_persistence.data_load()

    while True:
        ui.show_menu()
        selection = ui.user_input("Enter your choice: ")

        if selection == 1:
            ui.create_res(resource_manage)
        elif selection == 2:
            ui.create_res(resource_manage)
        elif selection == 3:
            ui.create_res(resource_manage)
        elif selection == 4:
            ui.create_res(resource_manage)
        elif selection == 5:

            data_persistence.data_save(resource_manage.ress)
            print("Exiting Program.")
            break
        else:
            print("Invalid Choice. Please try again.")