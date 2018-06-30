from db import dbCommands
from flask import Flask

dbCommands.setSchema()

response = dbCommands.getAllPrompts()

print(response)