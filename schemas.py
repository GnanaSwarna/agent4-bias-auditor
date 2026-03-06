from pydantic import BaseModel
from typing import List


class JDData(BaseModel):
    job_id: str
    required_skills: List[str]
    preferred_skills: List[str]
    experience_required: float
    degree: str


class CandidateProfile(BaseModel):
    candidate_id: str
    skills: List[str]
    experience_years: float
    education: str
    university: str
    passout_year: int
    location: str


class SkillAssessment(BaseModel):
    coding_score: float
    aptitude_score: float
    domain_score: float
    overall_skill_score: float


class Agent4Request(BaseModel):
    jd: JDData
    profile: CandidateProfile
    assessment: SkillAssessment