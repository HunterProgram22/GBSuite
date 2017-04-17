from django.db import models


class Course(models.Model):
    course = models.CharField(max_length=200, unique=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    slope = models.IntegerField()
    par = models.IntegerField()

    def __str__(self):
        return self.course


class Round(models.Model):
    course = models.ForeignKey(Course, to_field="course")
    #setting date to unique, not sure if will raise issue with multiple rounds
    #on the same date, maybe only if two rounds on same course and same date
    holesplayed = models.IntegerField(default=18)
    date = models.DateField(unique=True)
    strokes = models.IntegerField()
    putts = models.IntegerField()
    fairways_hit = models.IntegerField()
    gir = models.IntegerField()
    equistrokes = models.IntegerField()

    def __str__(self):
        return str(self.date) + " " + str(self.course)

    def print_round(self):
        return [(self.course, self.strokes)]

    def get_year(self):
        return self.date.year

    def course_rating(self):
        self.course.rating = float(self.course.rating)
        return self.course.rating

    def course_slope(self):
        self.course.slope = float(self.course.slope)
        return self.course.slope

    def handicap_diff(self):
        self.differential = ((self.equistrokes - self.course_rating())*113)/self.course_slope()
        self.differential = round(self.differential, 1)
        return self.differential


class Shots(models.Model):
    date = models.OneToOneField(Round, to_field="date")
    drdist = models.IntegerField()
    dracc = models.IntegerField()
    par3tee = models.IntegerField()
    lngdist = models.IntegerField()
    lngacc = models.IntegerField()
    shtdist = models.IntegerField()
    shtacc = models.IntegerField()
    pitch = models.IntegerField()
    chip = models.IntegerField()
    putt = models.IntegerField()
    penal = models.IntegerField()
    coursemgmt = models.IntegerField()


class PuttPractice(models.Model):
    date = models.DateField()
    distance = models.IntegerField()
    attempts = models.IntegerField()
    makes = models.IntegerField()

    def __str__ (self):
        return str(self.date) + " " + str(self.distance)


class RangeDrill(models.Model):
    date = models.DateField()
    club = models.CharField(max_length=10)
    balls_hit = models.IntegerField()
    WARMUP = "Warmup"
    COOLDOWN = "Cooldown"
    THC_STRIKE = "Toe/Heel/Center Strike"
    TH_SETUP = "Toe/Heel Setup"
    GATE_STRIKE = "Gate Strike"
    TH_CONSTRAINT = "Toe or Heel Constraint"
    STEP_DRILL = "Step Drill"
    DIVOT_DRILL = "Grass Divot Drill"
    SAND_DIVOT = "Sand Divot Drill"
    BALL_POSITION = "Ball Position Divot"
    TOWEL_DRILL = "Towel Drill"
    DRILL_CHOICES = ( (WARMUP, 'Warmup'),
                      (THC_STRIKE, 'Toe/Heel/Center Strike'),
                      (TH_SETUP, 'Toe/Heel Setup'),
                      (GATE_STRIKE, 'Gate Strike'),
                      (TH_CONSTRAINT, 'Toe or Heel Constraint'),
                      (STEP_DRILL, 'Step Drill'),
                      (DIVOT_DRILL, 'Grass Divot Drill'),
                      (SAND_DIVOT, 'Sand Divot Drill'),
                      (BALL_POSITION, 'Ball Position Divot'),
                      (TOWEL_DRILL, 'Towel Drill'),
                      (COOLDOWN, 'Cooldown'),
                      )
    drill = models.CharField(max_length=40, choices=DRILL_CHOICES, default=THC_STRIKE)

    def __str__ (self):
        return str(self.date) + " " + str(self.club) + " " + str(self.drill)


class ChipDrill(models.Model):
    date = models.DateField()
    club = models.CharField(max_length=10)
    balls_hit = models.IntegerField()
    balls_ontarget = models.IntegerField()
    INDOOR = "Home Mat Chip"
    SHORT_CHIP = "Close Hole Chip"
    LONG_CHIP = "Far Hole Chip"
    LOB_CHIP = "Lob Shot"
    BUMP_RUN = "Bump and Run"
    SAND_SHOT = "Bunker Shot"
    COIN_DRILL = "3 Coin Chip"
    DRILL_CHOICES = ( (INDOOR, 'Home Mat Chip'),
                      (SHORT_CHIP, 'Close Hole Chip'),
                      (LONG_CHIP, 'Far Hole Chip'),
                      (LOB_CHIP, 'Lob Shot'),
                      (BUMP_RUN, 'Bump and Run'),
                      (SAND_SHOT, 'Bunker Shot'),
                      (COIN_DRILL, '3 Coin Chip'),
                      )
    drill = models.CharField(max_length=40, choices=DRILL_CHOICES, default=INDOOR)

    def __str__ (self):
        return str(self.date) + " " + str(self.club) + " " + str(self.drill)

