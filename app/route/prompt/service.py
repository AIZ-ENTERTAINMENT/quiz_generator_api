from fastapi import HTTPException

from app.libs.database import with_session
from app.models.prompt import PromptORM


@with_session
async def create_prompt(prompt_name: str, prompt_content: str, session=None):
    "create prompt"
    try :
        print("orm 직전")
        return await PromptORM.create(
            prompt_name=prompt_name,
            prompt_content=prompt_content,
            session=session,
        )
    except :
        raise HTTPException(status_code=422, detail="Failed to create prompt")

@with_session
async def get_prompt(prompt_id: int, session=None):
    "get prompt"
    prompt = await PromptORM.get(
        prompt_id=prompt_id, session=session
    )
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return prompt

@with_session
async def update_prompt(prompt_id: int, prompt_name: str, prompt_content: str, session=None):
    "update prompt"
    prompt = await PromptORM.get(
        prompt_id=prompt_id, session=session
    )
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    await prompt.update_by_dict(
        data={
            "prompt_name": prompt_name,
            "prompt_content": prompt_content
        },
        session=session,
    )

@with_session
async def delete_prompt(prompt_id: int, session=None):
    "delete prompt"
    prompt = await PromptORM.get(
        prompt_id=prompt_id, session=session
    )
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    await prompt.delete(session=session)