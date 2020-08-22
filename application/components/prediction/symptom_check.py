from application.schema import Symptom

def get_risk_level(symptom: Symptom):
    if not (symptom.fever or symptom.dry_cough or symptom.tiredness or symptom.breathing_problem):
        return 'Low risk level. THIS IS A DEMO APP'
    
    if not (symptom.breathing_problem or symptom.dry_cough):
        if symptom.fever:
            return 'moderate risk level. THIS IS A DEMO APP'
    
    if symptom.breathing_problem:
        return 'High risk level. THIS IS A DEMO APP'
    
    return 'THIS IS A DEMO APP'