from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional

app = FastAPI(title="Smart Resume Maker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeRequest(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    location: str
    linkedin: Optional[str] = None
    github: Optional[str] = None
    photo_base64: Optional[str] = None
    summary: str
    experience: str
    projects: str
    education: str
    achievements: str
    certifications: str
    hobbies: str
    skills: List[str]
    template: str = "modern"

@app.post("/generate-resume")
async def generate_resume(data: ResumeRequest):
    return {
        "full_name": data.full_name,
        "template": data.template,
        "data": data
    }