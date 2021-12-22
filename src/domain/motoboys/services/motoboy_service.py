from injector import inject
from src.domain.motoboys.models.motoboy_model import ListMotoboyModel, MotoboyModel
from src.domain.motoboys.repositories import MotoboyRepository

class MotoboyService:
    
    @inject
    def __init__(self,repository: MotoboyRepository):
        self._repository = repository

    def get(self, id:int = None, **kwargs) -> MotoboyModel:
        return self._repository.find_motoboy(id,**kwargs)

    def get_motoboy_list(self, page, per_page) -> ListMotoboyModel:
        
        return self._repository.find_list_motoboy(
            page=int(page),
            per_page=int(per_page)
        )
    
    def create_motoboy(self, create_motoboy_model) -> MotoboyModel:
        return self._repository.create_motoboy(create_motoboy_model)