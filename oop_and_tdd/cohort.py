class andela_35:
    language = 'python'

    def __init__(self,attendees,date_started,facilitators,duration = 2):
        self.attendees = attendees
        self.date_started = date_started
        self.facilitators = facilitators
        self.ages = []
        self.duration = duration

    def new_ages(self, age):
        self.ages.append(age)
    # def get_ages(self):
        # return self.ages

    def add_learners(self, new_learners):
        self.attendees+=new_learners


class BootCamp(andela_35):
    def __init__(self,attendees,date_started,facilitators):
        super().__init__()
        self.facilitators = self.attendees//5


class learner:
    pass




# andela35Dec = andela_35(70,'Dec',5)
# andela35Nov = andela_35(45,'Nov',6)
# andela35Dec.new_ages(50)
# baker = learner()

# print(andela35Dec.attendees)
# print(andela35Nov.attendees)
# # print(baker)
# print(andela35Dec.ages)

# btJan = BootCamp(12,'Jan',54)
# print(f'Andela bootcamp {btJan.date_started} has {btJan.attendees} attendeees')

# print(f'Andela bootcamp {btJan.date_started} has {btJan.facilitators} facilitators')