
from odoo import models, fields, api

class AssistantVocal(models.Model):
    _name = 'assistant.vocal'
    _description = 'Assistant Vocal'

    name = fields.Char(string="Nom", required=True)
    query = fields.Text(string="Requête", required=True)
    response = fields.Text(string="Réponse", required=True)

class GoogleSheet(models.Model):
    _name = 'googlesheet.sheet'
    _description = 'Google Sheet'

    api_key = fields.Char(string="Clé API", required=True)
    scope = fields.Text(string="Portée", required=True)
    credentials = fields.Text(string="Informations d'identification", required=True)
    client = fields.Text(string="Client", required=True)

class SheetGPT(models.Model):
    _name = 'sheetgpt.sheet'
    _description = 'SheetGPT'

    query = fields.Text(string="Requête", required=True)
    response = fields.Text(string="Réponse", required=True)
    sheet_id = fields.Char(string="ID de la feuille", required=True)
    sheet_name = fields.Char(string="Nom de la feuille", required=True)
    sheet_range = fields.Char(string="Plage de la feuille", required=True)
    sheet_data = fields.Text(string="Données de la feuille", required=True)