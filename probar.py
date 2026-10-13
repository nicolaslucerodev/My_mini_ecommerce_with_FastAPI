from sqlmodel import SQLModel, create_engine
import models

engine= create_engine("sqlite://", echo=True)
SQLModel.metadata.create_all(engine)