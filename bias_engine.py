import datetime


class BiasEngine:

    def skill_match(self, candidate_skills, required_skills):

        if not required_skills:
            return 0

        matched = set(candidate_skills) & set(required_skills)

        return len(matched) / len(required_skills)


    def experience_score(self, candidate_exp, required_exp):

        if candidate_exp >= required_exp:
            return 1

        gap = required_exp - candidate_exp

        if gap <= 1:
            return 0.85
        elif gap <= 2:
            return 0.7
        else:
            return 0.5


    def education_score(self, education, jd_degree):

        if jd_degree.lower() in education.lower():
            return 1

        return 0.7


    def passout_adjustment(self, passout_year):

        current = datetime.datetime.now().year
        gap = current - passout_year

        if gap <= 3:
            return 1
        elif gap <= 7:
            return 0.9
        else:
            return 0.8


    def compute_fair_score(self, jd, profile, assessment):

        skill_score = self.skill_match(
            profile.skills,
            jd.required_skills
        )

        exp_score = self.experience_score(
            profile.experience_years,
            jd.experience_required
        )

        edu_score = self.education_score(
            profile.education,
            jd.degree
        )

        passout_factor = self.passout_adjustment(
            profile.passout_year
        )

        test_score = assessment.overall_skill_score

        final_score = (
            0.45 * skill_score +
            0.30 * test_score +
            0.15 * exp_score +
            0.10 * edu_score
        )

        final_score = final_score * passout_factor

        return {
            "skill_score": skill_score,
            "test_score": test_score,
            "experience_score": exp_score,
            "education_score": edu_score,
            "passout_adjustment": passout_factor,
            "fair_score": round(final_score, 3)
        }