class ExtremeFilter: 
    def __init__(self, model):
        self.model = model
    
    def filter(self, request):
        query_params = {key: value for key, value in request.GET.items() if value}
        if query_params:
            objects = self.model.objects.filter(**query_params)
        else:
            objects = self.model.objects.filter(**query_params)
        return objects