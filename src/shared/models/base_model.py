import abc 
from dataclasses import dataclass, asdict
from src.config.database import db


@dataclass
class BaseModel(metaclass=abc.ABCMeta):

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        filtered_data = cls._filter_dict(data)
        dict_data = {}

        for key in filtered_data.keys():
            item = filtered_data[key]
            if isinstance(item, list):
                for list_item in item:
                    if cls._is_db_model(list_item):
                        model_class = cls._get_dict_type(key)
                        model = model_class.from_dict(list_item.__dict__)
                        if key in dict_data:
                            dict_data[key].append(model)
                        else:     
                            dict_data[key] = [model]
                    elif isinstance(list_item, dict) and cls._get_dict_type(key):
                        model_class = cls._get_dict_type(key)
                        model = model_class.from_dict(list_item)
                        if key in dict_data:
                            dict_data[key].append(model)
                        else:     
                            dict_data[key] = [model]
                    else:
                        if key in dict_data:
                            dict_data[key].append(list_item)
                        else:
                            dict_data[key] = []
                            dict_data[key].append(list_item)

            elif cls._is_db_model(item): 
                model_class = cls._get_dict_type(key)
                dict_data[key] = model_class.from_dict(item.__dict__)
            elif isinstance(item, dict) and cls._get_dict_type(key):
                model_class = cls._get_dict_type(key)
                dict_data[key] = model_class.from_dict(item)
            else:
                dict_data[key] = item
        return cls(**dict_data)

    @classmethod
    def dict_filters(cls) -> list:
        return []

    @classmethod
    def dict_types(cls) -> dict:
        return {}


    #Métodos privados

    @classmethod
    def _filter_dict(cls, data):
        dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
        return dictfilt(data, cls.dict_filters())

    @classmethod
    def _get_dict_type(cls, field_key):
        dict_types = cls.dict_types()
        if field_key in dict_types:
            return dict_types[field_key]

    @classmethod
    def _is_db_model(cls, item) -> bool:
        return isinstance(item, db.Model)


