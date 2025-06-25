from app.libs.response import SuccessResponse
from app.route import get_router
from app.route.prompt import service

router = get_router("prompt")

@router.post("/")
async def create_prompt(prompt_name: str, prompt_content: str):
    "create prompt"
    res = await service.create_prompt(prompt_name, prompt_content)
    return SuccessResponse(data=res)

@router.get("/{prompt_id}")
async def get_prompt(prompt_id: int):
    "get prompt"
    res = await service.get_prompt(prompt_id)
    return SuccessResponse(data=res)

@router.put("/{prompt_id}")
async def update_prompt(prompt_id: int, prompt_name: str, prompt_content: str):
    "update prompt" 
    await service.update_prompt(prompt_id, prompt_name, prompt_content)
    return SuccessResponse(message="Prompt updated")

@router.delete("/{prompt_id}")
async def delete_prompt(prompt_id: int):
    "delete prompt"
    await service.delete_prompt(prompt_id)
    return SuccessResponse(message="Prompt deleted")