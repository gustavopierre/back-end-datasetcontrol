from sqlalchemy import Column, String, Integer, DateTime, Boolean
# from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base


class Data(Base):
    __tablename__ = 'data'

    id = Column("pk_data", Integer, primary_key=True, autoincrement=True)
    name = Column(String(140))
    description = Column(String(255))
    creation_date = Column(DateTime)
    update_date = Column(DateTime)
    check_date = Column(DateTime, default=datetime.now(), nullable=False)
    creator = Column(String(140))
    permitted = Column(Boolean, default=False, nullable=False)
    copyright = Column(String(140))
    format = Column(String(150), nullable=False)
    link = Column(String(140))
    info = Column(String(255))
    coordinate_system = Column(String(140))
    area = Column(String(140))

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # comentarios = relationship("Comentario")

    def __init__(self, name: str, description: str,
                 check_date: DateTime,
                 creator: str,
                 permitted: bool,
                 copyright: str,
                 link: str,
                 info: str,
                 coordinate_system: str,
                 area: str,
                 creation_date: Union[DateTime, None] = None,
                 update_date: Union[DateTime, None] = None,
                 format: str = "SHP"):
        """
        Cria um Produto

        Arguments:
            nome: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.name = name
        self.description = description

        # se não for informada, será o data exata da inserção no banco
        if creation_date:
            self.creation_date = creation_date

        if update_date:
            self.update_date = update_date

        if check_date:
            self.check_date = check_date

        self.creator = creator
        self.permitted = permitted
        self.copyright = copyright
        self.format = format
        self.link = link
        self.info = info
        self.coordinate_system = coordinate_system
        self.area = area

'''
    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)
'''