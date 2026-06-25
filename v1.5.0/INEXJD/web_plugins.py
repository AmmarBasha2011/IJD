"""
Web Framework Plugins for INEXJD!
Supports Flask, FastAPI, and Django!
"""


# -----------------------------
# Flask Extension
# -----------------------------
class INEXJDFlask:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        app.config.setdefault("INEXJD_PREFIX", "/inexjd")
        self.app = app
        
        from flask import jsonify, request
        
        @app.route(app.config["INEXJD_PREFIX"] + "/tables")
        def inexjd_list_tables():
            from .SQL.getTables import getTables
            return jsonify(getTables())
        
        @app.route(app.config["INEXJD_PREFIX"] + "/table/<table_name>")
        def inexjd_get_table(table_name):
            try:
                from .SQL.getTableData import getTableData
                return jsonify({"data": getTableData(table_name)})
            except Exception as e:
                return jsonify({"error": str(e)})
        
        @app.route(app.config["INEXJD_PREFIX"] + "/query", methods=["POST"])
        def inexjd_query():
            try:
                from .SQL.query_parser import execute_query
                q = request.json.get("query", "")
                return jsonify({"results": execute_query(q)})
            except Exception as e:
                return jsonify({"error": str(e)})


# -----------------------------
# FastAPI Extension
# -----------------------------
def create_inexjd_fastapi_router(prefix="/inexjd"):
    from fastapi import APIRouter, HTTPException
    from pydantic import BaseModel

    router = APIRouter(prefix=prefix)
    
    class QueryRequest(BaseModel):
        query: str
    
    @router.get("/tables")
    async def list_tables():
        from .SQL.getTables import getTables
        return getTables()
    
    @router.get("/table/{table_name}")
    async def get_table(table_name: str):
        try:
            from .SQL.getTableData import getTableData
            return {"data": getTableData(table_name)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @router.post("/query")
    async def run_query(req: QueryRequest):
        try:
            from .SQL.query_parser import execute_query
            return {"results": execute_query(req.query)}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return router


# -----------------------------
# Django App
# -----------------------------
class INEXJDDjango:
    """
    Basic Django integration setup!
    """
    @staticmethod
    def setup_urls():
        urls = """
from django.urls import path
from . import views

urlpatterns = [
    path('tables', views.inexjd_tables),
    path('table/<str:table_name>', views.inexjd_table),
    path('query', views.inexjd_query),
]
"""
        return urls

    @staticmethod
    def setup_views():
        views = """
from django.http import JsonResponse
from INEXJD.SQL.getTables import getTables
from INEXJD.SQL.getTableData import getTableData
from INEXJD.SQL.query_parser import execute_query
import json

def inexjd_tables(request):
    return JsonResponse(getTables())

def inexjd_table(request, table_name):
    try:
        return JsonResponse({"data": getTableData(table_name)})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def inexjd_query(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            q = body.get('query', '')
            return JsonResponse({"results": execute_query(q)})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
"""
        return views
