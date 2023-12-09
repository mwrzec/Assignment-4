class res_manage:
    def __init__(self):
        self.ress = []

    def create_res(self,name, att1,att2):
        res_id = len(self.ress) + 1
        new_res = Resource(res_id, name, att1, att2)
        self.ress.append(new_res)
        return new_res
    
    def search_res(self, key_att, non_key_att):
        matching_res = []
        for resource in self.ress:
            if key_att == str(resource.id) or key_att == resource.name:
                if non_key_att == str(resource.id) or non_key_att == resource.name:
                    matching_res.append(resource)
        return matching_res
    
    def edit_res(self, res_id, new_value):
        for resource in self.ress:
            if str(resource.id) == resource.id:
                for key, value in new_value.items():
                    if key != 'id':
                        setattr(resource, key, value)

                break
    
    def delete_res(self, res_id):
        self.ress = [resource for resource in self.ress if str(resource.id) != res_id]
