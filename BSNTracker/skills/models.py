from django.db import models
from datetime import date
from django.conf import settings
from instructor.models import Instructor

# Create your models here.

SKILL_CHOICES = (
    # assessment skills
    ('HAND_HYGIENE', 'Hand hygiene'),
    ('PATIENT_IDENTIFICATION', 'Patient identification'),
    ('PAIN_ASSESSMENT', 'Pain assessment'),
    ('VITAL_SIGNS', 'Vital signs (manual + electronic)'),
    ('OXYGEN_SATURATION', 'Oxygen saturation'),
    ('COMPREHENSIVE_HTT_ASSESSMENT', 'Comprehensive head-to-toe assessment'),
    ('FOCUSED_ASSESSMENTS', 'Focused assessments'),
    ('FALL_RISK_ASSESSMENT', 'Fall risk assessment'),
    ('SKIN_ASSESSMENT', 'Skin assessment / pressure injury staging'),
    ('NEURO_CHECKS', 'Neuro checks'),
    ('IO_CALCULATION', 'Intake & output calculation'),
    ('ACCURATE_DOCUMENTATION', 'Accurate documentation'),

    # infection prevention & safety
    ('PPE_DONNING_DOFFING', 'PPE donning/doffing'),
    ('STERILE_TECHNIQUE', 'Sterile technique'),
    ('ISOLATION_PRECAUTIONS', 'Isolation precautions'),
    ('SHARPS_SAFETY', 'Sharps safety'),
    ('MEDICATION_SAFETY_CHECKS', 'Medication safety checks'),
    ('BED_SAFETY_ALARMS', 'Bed safety / alarms'),
    ('SAFE_PATIENT_ENVIRONMENT_SCAN', 'Safe patient environment scan'),

    # ADLs
    ('BED_BATH_HYGIENE', 'Bed bath / hygiene'),
    ('ORAL_CARE_DEPENDENT_PATIENT', 'Oral care (including dependent patient)'),
    ('FEEDING_ASSISTANCE', 'Feeding assistance'),
    ('SAFE_PATIENT_HANDLING', 'Safe patient handling'),
    ('TRANSFERS_GAIT_BELT', 'Transfers (gait belt)'),
    ('MECHANICAL_LIFTS', 'Mechanical lifts (demo acceptable)'),
    ('POSITIONING_PRESSURE_PREVENTION', 'Positioning & pressure prevention'),
    ('BEDMAKING', 'Bedmaking (occupied/unoccupied)'),

    # medication administration
    ('SIX_RIGHTS_THREE_CHECKS', 'Six rights + three checks'),
    ('ORAL_MEDS', 'Oral meds'),
    ('LIQUID_MEDS', 'Liquid meds'),
    ('IM_INJECTIONS', 'IM injections'),
    ('SUBCUTANEOUS_INJECTIONS', 'Subcutaneous injections (incl. insulin)'),
    ('MEDICATION_RECONCILIATION', 'Medication reconciliation'),
    ('BARCODE_SCANNING', 'Barcode scanning'),
    ('MEDICATION_PATIENT_EDUCATION', 'Patient education for meds'),

    # elimination skills
    ('BEDPAN_URINAL', 'Bedpan / urinal'),
    ('FOLEY_INSERTION', 'Foley catheter insertion'),
    ('FOLEY_CARE', 'Foley care'),
    ('SPECIMEN_COLLECTION', 'Specimen collection'),
    ('BLADDER_SCAN', 'Bladder scan'),
    ('OSTOMY_CARE', 'Ostomy care'),
    ('ENEMA', 'Enema'),

    # respiratory / oxygen therapy
    ('NASAL_CANNULA', 'Nasal cannula'),
    ('SIMPLE_MASK', 'Simple mask'),
    ('INCENTIVE_SPIROMETRY', 'Incentive spirometry'),
    ('PULSE_OX_INTERPRETATION', 'Pulse ox interpretation'),
    ('COUGH_DEEP_BREATHE_COACHING', 'Cough/deep breathe coaching'),

    # fluids & basic lines
    ('IV_PUMP_PROGRAMMING', 'IV pump programming'),
    ('PRIMARY_TUBING_SETUP', 'Primary tubing setup'),
    ('IV_SITE_ASSESSMENT', 'IV site assessment'),
    ('PERIPHERAL_IV_REMOVAL', 'Peripheral IV removal'),
    ('NG_TUBE_CARE', 'NG tube care'),

    # professional & clinical judgement skills
    ('SBAR_COMMUNICATION', 'SBAR communication'),
    ('THERAPEUTIC_COMMUNICATION', 'Therapeutic communication'),
    ('CULTURAL_HUMILITY', 'Cultural humility'),
    ('INFORMED_CONSENT_AWARENESS', 'Informed consent awareness'),
    ('DELEGATION_PRINCIPLES', 'Delegation principles'),
    ('PRIORITIZATION', 'Prioritization'),
    ('PATIENT_EDUCATION', 'Patient education'),
    ('INTERPROFESSIONAL_COMMUNICATION', 'Interprofessional communication'),
)

SAI_CHOICES = (
    ('NOT_PRACTICED', 'Not practiced'),
    ('SIMULATION_SAFE', 'Simulation safe'),
    ('ASSISTED_CLINICAL', 'Assisted clinical'),
    ('INDEPENDENT_CLINICAL', 'Independent clinical'),
)

class Skill(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class StudentSkill(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=35, choices=SAI_CHOICES, default='Not practiced')
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
    class Meta:
        unique_together = ('student', 'skill')
    def __str__(self):
        return f"{self.student} - {self.skill} ({self.level})"

    def save(self, *args, **kwargs):
        if self.pk:
            old = StudentSkill.objects.get(pk=self.pk)
            if old.level != self.level:
                self.approved = False
        super().save(*args, **kwargs)

# class Skills(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='skill_entries')
#     skill = models.CharField(max_length=41, choices=SKILL_CHOICES, default='Hand hygiene')
#     sai = models.CharField(max_length=20, choices=SAI_CHOICES, default='Simulation safe')
#     completed = models.DateField(default=date.today)
#     location = models.TextField()
#     instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
#     date = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)