from fastapi import APIRouter, Form, Request
from app.telegram_app.router import send_msg
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

router_api = APIRouter(
    tags=['API']
)

templates = Jinja2Templates(directory="app/frontend/templates")


@router_api.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="base.html"
    )


@router_api.get('/application', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="application.html"
    )


@router_api.post('/application')
async def add_application(
        name: Annotated[str, Form()],
        emergency_service: Annotated[bool, Form()],
        city: Annotated[str, Form()],
        education: Annotated[str, Form()],
        number: Annotated[str, Form()]
):
    if len(number) != 11:
        print('Введите корректный номер телефона')

    if emergency_service is True:
        emergency_service = 'Да'
    else:
        emergency_service = 'Нет'

    await send_msg(
        value=f'Имя: {name},'
              f'\nНомер телефона: {number},'
              f'\nГород: {city},'
              f'\nОбразование: {education},'
              f'\nСрочная служба: {emergency_service}'
    )
    return RedirectResponse(url='http://79.174.91.112/', status_code=302)