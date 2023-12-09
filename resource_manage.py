from resource_1 import Resource
class ResourceManager: #creates resource class and initializes
    def __init__(self):
        self.ress = []

    def create_resource(self, name, att1, att2): #creates resourses
        res_id = len(self.ress) + 1
        new_res = Resource(res_id, name, att1, att2)
        self.ress.append(new_res)
        return new_res
    
    def search_resource(self, key_att, non_key_att): #searches for added resources
        matching_res = []
        for resource in self.ress:
            if key_att == str(resource.id) or key_att == resource.name:
                if non_key_att == str(resource.id) or non_key_att == resource.name:
                    matching_res.append(resource)
        return matching_res
    
    def edit_resource(self, res_id, new_values):#edits added resources.
        for resource in self.ress:
            if str(resource.id) == res_id:
                for key, value in new_values.items():
                    if key != 'id':
                        setattr(resource, key, value)
                break
    
    def delete_resource(self, res_id): #removes unwanted resources
        self.ress = [resource for resource in self.ress if str(resource.id) != res_id]
