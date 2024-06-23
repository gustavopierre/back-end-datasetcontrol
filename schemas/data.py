from pydantic import BaseModel
from typing import Optional, List
from model.data import Data
from datetime import datetime


class DataSchema(BaseModel):
    """ Define como um novo dado a ser inserido deve ser representado
    """
    name: str = "Ireland County Boundaries"
    description: str = "Ireland County Boundaries"
    creation_date: datetime = datetime.now()
    update_date: datetime = datetime.now()
    check_date: datetime = datetime.now()
    creator: str = "Tailte Éireann – Surveying"
    permitted: bool = True
    copyright: str = "Creative Commons Attribution 4.0"
    format: str = "SHP"
    link: str = "\Dataset\Ireland\Counties"
    info: str = "None"
    coordinate_system: str = "ITM"
    area: str = "All Ireland"


class DataSearchSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base na area do dado.
    """
    area: str = "Teste"


class ListDatasetSchema(BaseModel):
    """ Define como uma listagem de dados será retornada.
    """
    dataset: List[DataSchema]


def show_dataset(dataset: List[Data]):
    """ Retorna uma representação do dado seguindo o schema definido em
        DataViewSchema.
    """
    result = []
    for data in dataset:
        result.append({
            "name": data.name,
            "description": data.description,
            "creation_date": data.creation_date,
            "update_date": data.update_date,
            "check_date": data.check_date,
            "creator": data.creator,
            "permitted": data.permitted,
            "copyright": data.copyright,
            "format": data.format,
            "link": data.link,
            "info": data.info,
            "coordinate_system": data.coordinate_system,
            "area": data.area,
        })

    return {"dataset": result}


class DataViewSchema(BaseModel):
    """ Define como um dado será retornado.
    """
    id: int = 1
    name: str = "Ireland County Boundaries"
    description: str = "Ireland County Boundaries"
    creation_date: datetime = datetime.now()
    update_date: datetime = datetime.now()
    check_date: datetime = datetime.now()
    creator: str = "Ireland County Boundaries"
    permitted: bool = True
    copyright: str = "Ireland County Boundaries"
    format: str = "Ireland County Boundaries"
    link: str = "Ireland County Boundaries"
    info: str = "Ireland County Boundaries"
    coordinate_system: str = "ITM"
    area: str = "All Ireland"


class DataDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    name: str


def show_data(data: Data):
    """ Retorna uma representação do dado seguindo o schema definido em
        DataViewSchema.
    """
    return {
        "id": data.id,
        "name": data.name,
        "description": data.description,
        "creation_date": data.creation_date,
        "update_date": data.update_date,
        "check_date": data.check_date,
        "creator": data.creator,
        "permitted": data.permitted,
        "copyright": data.copyright,
        "format": data.format,
        "link": data.link,
        "info": data.info,
        "coordinate_system": data.coordinate_system,
        "area": data.area
    }