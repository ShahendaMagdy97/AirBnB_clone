#!/usr/bin/python3
import models
import uuid
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for var1, var2 in kwargs.items():
                if var1 != "__class__":
                    if var1 == "updated_at":
                        self.updated_at = datetime.fromisoformat(var2)
                    elif var1 == "created_at":
                        self.created_at = datetime.fromisoformat(var2)
                    else:
                        setattr(self, var1, var2)
    def __str__(self):

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        num1 = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            num1[key] = value
        num1['__class__'] = self.__class__.__name__

        return num1

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
