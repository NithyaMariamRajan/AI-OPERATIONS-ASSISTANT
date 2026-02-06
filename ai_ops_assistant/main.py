from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import generate_response

app = FastAPI(title="OpsPilot AI")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, query: str = Form(...)):

    plan = create_plan(query)

    if not isinstance(plan, dict) or "steps" not in plan:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Planning failed."}
        )

    execution = execute_plan(plan)
    final_answer = generate_response(query, execution)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "query": query,
            "response": final_answer
        }
    )
