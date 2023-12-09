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

    def make_res(self, res_manage):
        name = self.user_input("Enter resource name: ")
        att1 = self.user_input("Enter attribute #1: ")
        att2 = self.user_input("Enter attribute #2: ")
        new_res = res_manage.make_res(name, att1, att2)
        print(f"Resource created with ID: {new_res.id}")

    def search_res(self, res_manage):
        key_att = self.user_input("Enter key attribute: ")
        non_key_att = self.user_input("Enter non-key attribute: ")
        matching_res = res_manage.search_res(key_att, non_key_att)
        self.display_res(matching_res)

    def edit_res(self, res_manage):
        res_id = self.user_input("Enter resource ID to edit: ")
        new_values = {
            'name': self.user_input("Enter new name: "),
            'att1': self.user_input("Enter new attribute #1: "),
            'att2': self.user_input("Enter new attribute #2: "),
        }
        res_manage.edit_res(res_id, new_values)
        print("Resource updated successfully.")

    def delete_res(self, res_manage):
        res_id = self.user_input("Enter resource ID to remove: ")
        res_manage.delete_res(res_id)
        print("Resource has been successfully removed.")

    def display_res(self, ress):
        for resource in ress:
            print(f"ID: {resource.id}, Name: {resource.name}, Attribute #1: {resource.att1}, Attribute #2: {resource.att2}")
