import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidate = json.load(file)
    return candidate


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if pk == candidate['pk']:
            return candidate


def get_by_skill(skill_name):
    candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower():
            candidates.append("Имя кандидата - " + candidate['name'])
            candidates.append("Позиция кандидата - " + str(candidate['pk']))
            candidates.append("Навыки - " + candidate['skills'])
    return f'{"<br><br>".join(candidates)}'
