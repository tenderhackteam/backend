from fastapi import APIRouter
from data_models.db_setup import Item, session
from sqlalchemy import select, and_
import json

router = APIRouter()


@router.get("/")
async def get_some_from_catalog(first_number: int, last_number: int):
    items = []
    for item in session.execute(
            select(Item).where(and_(Item.id >= first_number, Item.id <= last_number))):
        items.append({
            "id": Item.id,
            "cte_id": Item.cte_id,
            "cte_name": Item.cte_name,
            "category_id": Item.category_id,
            "description": Item.description,
            "cte_props": Item.cte_props,
            "regions": Item.regions,
            "made_contracts": Item.made_contracts,
            "suppliers": Item.suppliers,
            "country": Item.country,
            "other_items_in_contracts": Item.other_items_in_contracts,
            "cpgz_id": Item.cpgz_id,
            "cpgz_code": Item.cpgz_code,
            "model": Item.model,
            "price": Item.price
        })
    return json.dumps(items)


@router.get("/item")
async def get_some_from_catalog(item_id):
    items = []
    for item in session.execute(
            select(Item).where(Item.id == item_id)):
        items.append({
            "id": Item.id,
            "cte_id": Item.cte_id,
            "cte_name": Item.cte_name,
            "category_id": Item.category_id,
            "description": Item.description,
            "cte_props": Item.cte_props,
            "regions": Item.regions,
            "made_contracts": Item.made_contracts,
            "suppliers": Item.suppliers,
            "country": Item.country,
            "other_items_in_contracts": Item.other_items_in_contracts,
            "cpgz_id": Item.cpgz_id,
            "cpgz_code": Item.cpgz_code,
            "model": Item.model,
            "price": Item.price
        })
    return json.dumps(items)
