from fastapi import APIRouter
from data_models.db_setup import Item, session, Category
from sqlalchemy import select, and_
import json

router = APIRouter()


@router.get("/")
async def get_some_from_catalog(first_number: int, last_number: int):
    items = []
    for item in session.execute(
            select(Item).where(and_(Item.id >= first_number, Item.id <= last_number))).all():
        items.append({
            "id": item[0].id,
            "cte_id": item[0].cte_id,
            "cte_name": item[0].cte_name,
            "category_id": session.execute(select(Category).where(Category.id == item[0].category_id)).one()[0].name,
            "description": item[0].description,
            "cte_props": item[0].cte_props,
            "regions": item[0].regions,
            "made_contracts": item[0].made_contracts,
            "suppliers": item[0].suppliers,
            "country": item[0].country,
            "other_items_in_contracts": item[0].other_items_in_contracts,
            "cpgz_id": item[0].cpgz_id,
            "cpgz_code": item[0].cpgz_code,
            "model": item[0].model,
            "price": item[0].price
        })
    return items


@router.get("/item")
async def get_some_from_catalog(item_id):
    items = []
    for item in session.execute(
            select(Item).where(Item.id == item_id)).one():
        items.append({
            "id": item.id,
            "cte_id": item.cte_id,
            "cte_name": item.cte_name,
            "category_id": session.execute(select(Category).where(Category.id == item.category_id)).one()[0].name,
            "description": item.description,
            "cte_props": item.cte_props,
            "regions": item.regions,
            "made_contracts": item.made_contracts,
            "suppliers": item.suppliers,
            "country": item.country,
            "other_items_in_contracts": item.other_items_in_contracts,
            "cpgz_id": item.cpgz_id,
            "cpgz_code": item.cpgz_code,
            "model": item.model,
            "price": item.price
        })
    return items
