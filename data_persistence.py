import json

class DataPersistence: #creates data persistence class and initializes
    def __init__(self, file_name):
        self.file_name = file_name

    def data_save(self, ress): #allows you to save the data inputted
        data = []
        for resource in ress:
            data.append({
                'id': resource.id,
                'name': resource.name,
                'att1': resource.att1,
                'att2': resource.att2,
            })
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

    def data_load(self): #loads inputed data
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)

                ress = []

                for item in data:
                    new_res = Resource(item['id'], item['name'], item['att1'], item['att2'])
                    ress.append(new_res)

                return ress
        except FileNotFoundError: #shows file not found if doesnt exist
            return []
