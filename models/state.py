#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import city


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'

    if models.storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')
    else:
        name= ""

    if models.storage_type != "db"
    @property
    def cities(self):
        """
        public method to return the list of City objects from storage
        linked to the current State
        """
        list_of_city = []
        all_cities = models.storage.all(city)
        for value in all_cities.values():
            if city.state_id == self.id:
                list_of_city.append(city)
        return list_of_city
