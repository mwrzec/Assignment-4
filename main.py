class UI:
    def main_menu(self):
        print("1. Create Resource")
        print("2. Search Resource")
        print("3. Edit Resource")
        print("4. Delete Resource")
        print("5. Exit")

    def user_input(self, message):
        while True:
            try:
                return input(message)
            except Exception as e:
                print(f"Error: {e}")

    def create_resource(self, resource_manager):
        name = self.user_input("Enter resource name: ")
        att1 = self.user_input("Enter attribute #1: ")
        att2 = self.user_input("Enter attribute #2: ")
        new_res = resource_manager.create_resource(name, att1, att2)
        print(f"Resource created with ID: {new_res.id}")

    def search_resource(self, resource_manager):
        key_att = self.user_input("Enter key attribute: ")
        non_key_att = self.user_input("Enter non-key attribute: ")
        matching_res = resource_manager.search_resource(key_att, non_key_att)
        self.display_res(matching_res)

    def edit_resource(self, resource_manager):
        res_id = self.user_input("Enter resource ID to edit: ")
        new_values = {
            'name': self.user_input("Enter new name: "),
            'att1': self.user_input("Enter new attribute #1: "),
            'att2': self.user_input("Enter new attribute #2: "),
        }
        resource_manager.edit_resource(res_id, new_values)
        print("Resource updated successfully.")

    def delete_resource(self, resource_manager):
        res_id = self.user_input("Enter resource ID to remove: ")
        resource_manager.delete_resource(res_id)
        print("Resource has been successfully removed.")

    def display_res(self, ress):
        for resource in ress:
            print(f"ID: {resource.id}, Name: {resource.name}, Attribute #1: {resource.att1}, Attribute #2: {resource.att2}")
