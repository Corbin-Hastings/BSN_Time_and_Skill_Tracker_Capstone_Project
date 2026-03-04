from django.db import models
from datetime import date
from django.conf import settings
from instructor.models import Instructor

# Create your models here.

SKILL_CHOICES = (
    # assessment skills
    ('Hand hygiene', 'HAND_HYGIENE'),
    ('Patient identification', 'PATIENT_IDENTIFICATION'),
    ('Pain assessment', 'PAIN_ASSESMENT'),
    ('Vital signs (manual + electronic)', 'VITAL_SIGNS'),
    ('Oxygen saturation', 'OXYGEN_SATURATION'),
    ('Comprehensive head-to-toe assessment', 'COMPREHENSIVE_HTT_ASSESSMENT'),
    ('Focused assessments', 'FOCUSED_ASSESMENTS'),
    ('Fall risk assessment', 'FALL_RISK_ASSESSMENT'),
    ('Skin assessment / pressure injury staging', 'SKIN ASSESSMENT'),
    ('Neuro checks', 'NEURO_CHECKS'),
    ('Intake & output calculation', 'IO_CALCULATION'),
    ('Accurate documentation', 'ACCURATE_DOCUMENTATION'),

    # #infection prevention & safety
    # PPE donning/doffing
    # Sterile technique
    # Isolation precautions S
    # Sharps safety
    # Medication safety checks
    # Bed safety / alarms
    # Safe patient environment scan
    # #ADLs
    # Bed bath / hygiene
    # Oral care (including dependent patient)
    # Feeding assistance
    # Safe patient handling
    # Transfers (gait belt)
    # Mechanical lifts (demo acceptable)
    # Positioning & pressure prevention
    # Bedmaking (occupied/unoccupied)
    # #medication administration
    # Six rights + three checks
    # Oral meds
    # Liquid meds
    # IM injections
    # Subcutaneous injections (incl. insulin)
    # Medication reconciliation
    # Barcode scanning
    # Patient education for meds
    # #elimination skills
    # Bedpan / urinal
    # Foley catheter insertion
    # Foley care
    # Specimen collection
    # Bladder scan
    # Ostomy care
    # Enema
    # #wound&skin care
    # Nasal cannula
    # Simple mask
    # Incentive spirometry
    # Pulse ox interpretation
    # Cough/deep breathe coaching
    # #fluids & basic lines
    # IV pump programming
    # Primary tubing setup
    # IV site assessment
    # Peripheral IV removal
    # NG tube care
    # #professional & clinical judgement skills:
    # SBAR communication
    # Therapeutic communication
    # Cultural humility
    # Informed consent awareness
    # Delegation principles
    # Prioritization
    # Patient education
    # Interprofessional communication

)

SAI_CHOICES = (
    ('Simulation safe', 'SIMULATION_SAFE'),
    ('Assisted clinical', 'ASSISTED_CLINICAL'),
    ('Independent clinical', 'INDEPENDENT_CLINICAL'),
)

# TODO - change to pulling instructors from users (sprint 2?)
INSTRUCTOR_CHOICES = (
    ('Instructor 1', 'INSTR_1'),
    ('Instructor 2', 'INSTR_2'),
    ('Instructor 3', 'INSTR_3'),
)


class Skills(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='skill_entries')
    skill = models.CharField(max_length=41, choices=SKILL_CHOICES, default='Hand hygiene')
    sai = models.CharField(max_length=20, choices=SAI_CHOICES, default='Simulation safe')
    completed = models.DateField(default=date.today)
    location = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    # TODO - foreign key
