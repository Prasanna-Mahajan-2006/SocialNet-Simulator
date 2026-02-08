import os
import csv
import math
class Participant:
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str):
        self.name = name
        self.idi = idi
        self.__birth_year = birth_year
        self.__birth_month = birth_month
        self.__birth_day = birth_day
        self.__gender =  gender
    def get_values(self):
        return tuple(self.__dict__.values())
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')
    def set_values(self, data_attributes: dict):
        for key in data_attributes.keys():
            if key == 'name':
                self.name = data_attributes[key]
            elif key == 'idi':
                self.idi = data_attributes[key]
            elif key == 'birth_year':
                self.__birth_year = data_attributes[key]
            elif key == 'birth_month':
                self.__birth_month = data_attributes[key]
            elif key == 'birth_day':
                self.__birth_day = data_attributes[key]
            elif key == 'gender':
                self.__gender = data_attributes[key]
            else:
                setattr(self, key, data_attributes[key])
    def calculate_age(self, curr_day: int, curr_month: int, curr_year: int):
        if curr_day > 31 or curr_day < 1:
            return -1
        elif curr_month > 12 or curr_month < 1:
            return -1
        else:
            if curr_month > self.__birth_month:
                year_factor = math.floor(curr_year - self.__birth_year)
                month_factor = curr_month - self.__birth_month
                day_factor = curr_day
                return year_factor
            elif self.__birth_month == curr_month and curr_day >= self.__birth_day:
                return math.floor(curr_year - self.__birth_year)
            else:
                return math.floor(curr_year - self.__birth_year - 1)
class Teacher(Participant):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, subject: str, mentor_grade: int, mentor_class: str, judge: bool):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__subject = subject
        self.__mentor_grade = mentor_grade
        self.__mentor_class = mentor_class
        self.__judge = judge
    def get_values(self):
        return tuple(self.__dict__.values())
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')
    def set_values(self, data_attributes: dict):
        for k in list(data_attributes.keys()):
            if k == 'subject':
                self.__subject = data_attributes[k]
            elif k == 'mentor_grade':
                self.__mentor_grade = data_attributes[k]
            elif k == 'mentor_class':
                self.__mentor_class = data_attributes[k]
            elif k == 'judge':
                self.__judge = data_attributes[k]
            else:
                mangled_name = f"_{Participant.__name__}__{k}"
                setattr(self, mangled_name, data_attributes[k])
                
class Student(Participant):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, grade_level: int, class_assigned: str, gpa: float, selected_activity: str, talent_score: float, athletic_score: float, leadership_score: float):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__age = self.calculate_age(1, 1, 2025)
        self.__grade_level = grade_level
        self.__class_assigned = class_assigned
        self.__gpa = gpa
        self.__selected_activity = selected_activity
        self.__talent_score = talent_score
        self.__athletic_score = athletic_score
        self.__leadership_score = leadership_score
        self.__eligible = self.is_eligible()
        
    def is_eligible(self):
        if self.__gpa >= 5.0:
            self.__eligible = True
        else:
            self.__eligible = False
        return self.__eligible
    def get_values(self):
        return tuple(self.__dict__.values())
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')
    def set_values(self, data_attributes: dict):
        for k in list(data_attributes.keys()):
            if k == 'age':
                self.__age = data_attributes[k]
            elif k == 'grade_level':
                self.__grade_level = data_attributes[k]
            elif k == 'class_assigned':
                self.__class_assigned = data_attributes[k]
            elif k == 'gpa':
                self.__gpa = data_attributes[k]
                if self.__gpa >= 5.0:
                    self.__eligible = True
                else:
                    self.__eligible = False
            elif k == 'selected_activity':
                self.__selected_activity = data_attributes[k]
            elif k == 'talent_score':
                self.__talent_score = data_attributes[k]
            elif k == 'athletic_score':
                self.__athletic_score = data_attributes[k]
            elif k == 'leadership_score':
                self.__leadership_score = data_attributes[k]
            elif k == 'eligible':
                self.__eligible = data_attributes[k]
            else:
                mangled_name = f"_{Participant.__name__}__{k}"
                setattr(self, mangled_name, data_attributes[k])

class Artist(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, grade_level: int, class_assigned: str, gpa: float, selected_activity: str, talent_score: float, athletic_score: float, leadership_score: float, talent: str):
        super().__init__( name, idi, birth_year, birth_month, birth_day, gender, grade_level, class_assigned, gpa, selected_activity, talent_score, athletic_score, leadership_score)
        self.__talent = talent
        self.__performance_level = self._Student__talent_score
        self.__eligible = self.is_eligible()
    def is_eligible(self):
        return (self._Student__age >= 16 and self._Student__gpa > 6.0)

    def compute_scores(self):
        if self.is_eligible():
            return self.__performance_level
        else:
            return -1
    
    def get_values(self):
        return tuple(self.__dict__.values())
    
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')

    def set_values(self, data_attributes: dict):
        for key in data_attributes.keys():
            if key == 'talent':
                self.__talent = data_attributes[key]
            elif key == 'performance_level':
                self.__performance_level = data_attributes[key]
            else:
                mangled_name = f"_{Student.__name__}__{key}"
                setattr(self, mangled_name, data_attributes[key])

class Athlete(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, grade_level: int, class_assigned: str, gpa: float, selected_activity: str, talent_score: float, athletic_score: float, leadership_score: float, sports_category: str, fitness_score: float):
        super().__init__( name, idi, birth_year, birth_month, birth_day, gender, grade_level, class_assigned, gpa, selected_activity, talent_score, athletic_score, leadership_score)

        self.__sports_category = sports_category
        self.__fitness_score = fitness_score
        self.__performance_level = self._Student__athletic_score
        self.__eligible = self.is_eligible()

    def is_eligible(self):
        return (self._Student__gpa > 5.5 and self._Student__age >= 12)

    def compute_scores(self):
        if self.is_eligible():
            return self.__fitness_score * self.__performance_level
        else:
            return -1

    def get_values(self):
        return tuple(self.__dict__.values())
    
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')

    def set_values(self, data_attributes: dict):
        for key in data_attributes.keys():
            if key == 'fitness_score':
                self.__fitness_score = data_attributes[key]
            elif key == 'sports_category':
                self.__sports_category = data_attributes[key]
            elif key == 'performance_level':
                self.__performance_level = data_attributes[key]
            else:
                mangled_name = f"_{Student.__name__}__{key}"
                setattr(self, mangled_name, data_attributes[key])

class Scholar(Student):
    def __init__(self, name: str, idi: int, birth_year: int, birth_month: int, birth_day: int, gender: str, grade_level: int, class_assigned: str, gpa: float, selected_activity: str, talent_score: float, athletic_score: float, leadership_score: float, subject_specialization: str, olympiad_scores: list[float]):

        self.__subject_specialization = subject_specialization
        self.__olympiad_scores = olympiad_scores
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, grade_level, class_assigned, gpa, selected_activity, talent_score, athletic_score, leadership_score)
        self.__performance_level = self._Student__gpa * 10
        self.__eligible = self.is_eligible()

    def is_eligible(self):
        if self._Student__age >= 10 and self._Student__gpa >= 8.0:
            for j in self.__olympiad_scores:
                if j > 80.0:
                    self.__eligible = True
                    return True
            self.__eligible = False
            return False
        else:
            self.__eligible = False
            return False

    def compute_scores(self):
        if self.is_eligible():
            net_sum = 0
            for val in self.__olympiad_scores:
                net_sum += val
            return net_sum * self.__performance_level
            #return max(self.__olympiad_scores) * self.__performance_level
        else:
            return -1

    def get_values(self):
        return tuple(self.__dict__.values())
     
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')

    def set_values(self, data_attributes: dict):
        for key in data_attributes.keys():
            if key == 'subject_specialization':
                self.__subject_specialization = data_attributes[key]
            elif key == 'olympiad_scores':
                self.__olympiad_scores = data_attributes[key]
            elif key == 'performance_level':
                self.__performance_level = data_attributes[key]
            else:
                mangled_name = f"_{Student.__name__}__{key}"
                setattr(self, mangled_name, data_attributes[key])

class Activity:
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int, grade_level: int, is_active: bool, participants: list[Student], organizers: list[Teacher]):
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.__activity_type = activity_type
        self.__max_participants = max_participants
        self.__grade_level = grade_level
        self.__is_active = is_active
        self.__participants = participants
        self.__organizers = organizers

    def get_values(self):
        return tuple(self.__dict__.values())
     
    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')

    def set_values(self, data_attributes: dict):
        for key in data_attributes.keys():
            if key == 'max_participants':
                self.__max_participants = data_attributes[key]
            elif key == 'activity_type':
                self.__activity_type = data_attributes[key]
            elif key == 'grade_level':
                self.__grade_level = data_attributes[key]
            elif key == 'is_active':
                self.__is_active = data_attributes[key]
            elif key == 'participants':
                self.__participants = data_attributes[key]
            elif key == 'organizers':
                self.__organizers = data_attributes[key]

class SportsTournament(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int, grade_level: int, is_active: bool, participants: list[Student], organizers: list[Teacher], game_type: str, duration_minutes: int):
        self.__game_type = game_type
        self.__duration_minutes = duration_minutes
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)

    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')

   #def getattr(self):
   #    return super().activity_name
    def get_teams(self):
        team_dict = {}
        data_list = []
        for student in self._Activity__participants:
            grade = student._Student__class_assigned
            if grade not in team_dict.keys():
                team_dict[grade] = []
                if student._Student__gpa > 5.5 and student._Student__age >= 12:
                    team_dict[grade].append(student)
            else:
                if student._Student__gpa > 5.5 and student._Student__age >= 12:
                    team_dict[grade].append(student)
        for value in team_dict.values():
            scores_and_average_list = []
            max_individual_score = 0
            score_sum = count_players = 0
            for player in value:
                scores_and_average_list.append(player.compute_scores())
                if player.compute_scores() > max_individual_score:
                    max_individual_score = player.compute_scores()
                    winner_player = player
                score_sum += player.compute_scores()
                count_players += 1
            scores_and_average_list.append(winner_player)
            scores_and_average_list.append(score_sum / count_players)
            data_list.append(scores_and_average_list)
        return data_list
        
    def determine_winner(self):
        if self.__game_type not in ['Team', 'Individual']:
            return -1
        max_score = 0
        winner_name = -1
        if self.__game_type == 'Individual':
            for contestant in self._Activity__participants:
                if not isinstance(contestant, Athlete):
                    continue
                else:
                    score = contestant.compute_scores()     
                    if score > max_score:
                        max_score = score
                        winner_name = contestant
        else:
            all_teams_data = self.get_teams()
            for team in all_teams_data:
                if team[-1] > max_score:
                    max_score = team[-1]
                    winner_name = team[-2]
        return winner_name

class TalentShow(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int, grade_level: int, is_active: bool, participants: list[Student], organizers: list[Teacher], talent_categories: list):
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)

        self.__talent_categories = talent_categories

    def show_values(self):
        for value in self.get_values():
            print(value, end = ' ')
            
    def evaluate_talent(self):
        max_score = 0
        winner_name = -1
        for contestant in self._Activity__participants:
            if not isinstance(contestant, Artist):
                continue
            else:
                score = contestant.compute_scores()
                if score > max_score:
                    max_score = score
                    winner_name = contestant
        return winner_name

class AcademicCompetition(Activity):
    def __init__(self, activity_id: int, activity_name: str, activity_type: str, max_participants: int, grade_level: int, is_active: bool, participants: list[Student], organizers: list[Teacher], subjects: list, max_marks: float):
        super().__init__(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers)

        self.__subjects = subjects
        self.__max_marks = max_marks

    def determine_winner(self):
        max_score = 0
        winner_name = -1
        for contestant in self._Activity__participants:
            if not isinstance(contestant, Scholar):
                continue
            else:
                score = contestant.compute_scores()
                if score > max_score:
                    max_score = score
                    winner_name = contestant
        return winner_name

# Defining function to read the participant data
def load_participant_data(filepath: str):
    teacher_list = []
    student_list = []
    with open(filepath, 'r') as my_file:
        csv_file = csv.reader(my_file)
        next(csv_file)
        
        for line in csv_file:
            name = str(line[1])
            idi = int(line[0])
            birth_year = int(line[2])
            birth_month = int(line[3])
            birth_day = int(line[4])
            gender = str(line[5])
            grade_level = int(line[12]) if line[12] else None
            class_assigned = str(line[10]) if line[10] else None
            gpa = float(line[9]) if line[9] else None
            selected_activity = str(line[11])
            if line[8] != '' and line[6] != '' and line[7] != '':
                talent_score = float(line[8])
                athletic_score = float(line[6])
                leadership_score = float(line[7])
            
            subject = str(line[18]) if line[18] else None
            mentor_grade = int(line[19]) if line[19] else None
            mentor_class = str(line[20]) if line[20] else None
            judge = bool(line[21])
            
            if subject:
                teacher = Teacher(name, idi, birth_year, birth_month, birth_day, gender, subject, mentor_grade, 
                                  mentor_class, judge)
                teacher_list.append(teacher)
            else:
                student = Student(name, idi, birth_year, birth_month, birth_day, gender, grade_level, class_assigned, 
                                  gpa, selected_activity, talent_score, athletic_score, leadership_score)
                student_list.append(student)

        return student_list, teacher_list

all_students, all_teachers = load_participant_data('easy_participant_data.csv')

def load_activities_data(filepath: str):
    sports_tournament = []
    talent_show = []
    academic_competition = []
    
    with open(filepath, 'r') as my_file:
        csv_file = csv.reader(my_file)
        next(csv_file)
        
        for line in csv_file:
            activity_id = int(line[0])
            activity_name = str(line[1])
            activity_type = str(line[2])
            max_participants = int(line[3])
            grade_level = int(line[4])
            is_active = False
            participants = []
            organizers = []
            game_type = str(line[5]) if line[5] else None
            duration_minutes = int(line[6]) if line[6] else None
            talent_categories = [str(j) for j in (line[7].strip()).split('-')] if line[7] else []
            subjects = list(line[8]) if line[8] else None
            max_marks = int(line[9]) if line[9] else None
            
            if activity_type == 'Sports':
                sport_activity = SportsTournament(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers, game_type, duration_minutes)
                sports_tournament.append(sport_activity)
                
            elif activity_type == 'Talent':
                talent_activity = TalentShow(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers, talent_categories)
                talent_show.append(talent_activity)
                
            else:
                academic_activity = AcademicCompetition(activity_id, activity_name, activity_type, max_participants, grade_level, is_active, participants, organizers, subjects, max_marks)
                academic_competition.append(academic_activity)
            
        return (sports_tournament, talent_show, academic_competition)

def specialised_students(filepath: str):
    artist_list = []
    athlete_list = []
    scholar_list = []
    with open(filepath, 'r') as my_file:
        csv_file = csv.reader(my_file)
        next(csv_file)
        for line in csv_file:
            name = str(line[1])
            idi = int(line[0])
            birth_year = int(line[2])
            birth_month = int(line[3])
            birth_day = int(line[4])
            gender = str(line[5])
            grade_level = int(line[12]) if line[12] else 0
            class_assigned = str(line[10]) if line[10] else 0
            gpa = float(line[9]) if line[9] else 0
            selected_activity = str(line[11])
            talent_score = float(line[8]) if line[8] else 0
            athletic_score = float(line[6]) if line[6] else 0
            leadership_score = float(line[7]) if line[7] else 0
                
            if selected_activity == 'Sports':
                sports_category = str(line[17])
                fitness_score = float(line[16])
                athlete_student = Athlete(name, idi, birth_year, birth_month, birth_day, gender, grade_level, 
                                class_assigned, gpa, selected_activity, talent_score, athletic_score, 
                                leadership_score, sports_category, fitness_score)
                score = athlete_student.compute_scores()
                athlete_list.append(athlete_student)
                with open(f'{class_assigned}-athlete.csv', 'a') as write_file:
                    writer_object = csv.writer(write_file)
                    if os.path.getsize(f'{class_assigned}-athlete.csv') == 0:
                        writer_object.writerow(['participant_id', 'name', 'grade_level', 'class_assigned', 
                                               'selected_activity', 'score'])
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])
                    else:
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])
            elif selected_activity == 'Talent':
                talent = str(line[13])
                artist_student = Artist(name, idi, birth_year, birth_month, birth_day, gender, grade_level, 
                                class_assigned, gpa, selected_activity, talent_score, athletic_score, 
                                leadership_score, talent)
                artist_list.append(artist_student)
                score = artist_student.compute_scores()
                with open(f'{class_assigned}-artist.csv', 'a') as write_file:
                    writer_object = csv.writer(write_file)
                    if os.path.getsize(f'{class_assigned}-artist.csv') == 0:
                        writer_object.writerow(['participant_id', 'name', 'grade_level', 'class_assigned', 
                                               'selected_activity', 'score'])
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])
                    else:
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])

            else:
                subject_specialization = str(line[15])
                olympiad_scores = [int(j) for j in (line[14].strip()).split('-')] if line[14] else []
                scholar_student = Scholar(name, idi, birth_year, birth_month, birth_day, gender, grade_level, 
                                class_assigned, gpa, selected_activity, talent_score, athletic_score, 
                                leadership_score, subject_specialization, olympiad_scores)
                scholar_list.append(scholar_student)
                score = scholar_student.compute_scores()
                with open(f'{class_assigned}-scholar.csv', 'a') as write_file:
                    writer_object = csv.writer(write_file)
                    if os.path.getsize(f'{class_assigned}-scholar.csv') == 0:
                        writer_object.writerow(['participant_id', 'name', 'grade_level', 'class_assigned', 
                                               'selected_activity', 'score'])
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])
                    else:
                        writer_object.writerow([idi, name, grade_level, class_assigned, selected_activity, score])
                        
        return (artist_list, athlete_list, scholar_list)

# Defining the function to conduct registrations
def register_activity(participant_filepath: str, activity_filepath: str):
    cricket_list = []
    chess_list = []
    math_list = []
    science_list = []
    computers_list = []
    blackrose_list = []
    with open(participant_filepath, 'r') as part_file, open(activity_filepath, 'r') as act_file:
        sports, talents, acads = load_activities_data(activity_filepath)
        teachers = load_participant_data(participant_filepath)[1]
        artists, athletes, scholars = specialised_students(participant_filepath)
        print
        for artist_activity in talents:
            for student in artists:
                if student._Student__selected_activity == 'Talent' and student._Student__grade_level == artist_activity._Activity__grade_level and student.is_eligible():
                    artist_activity._Activity__participants.append(student)
            for teacher in teachers:
                if teacher._Teacher__mentor_grade == artist_activity._Activity__grade_level:
                    artist_activity._Activity__organizers.append(teacher)
            if (len(artist_activity._Activity__participants) > artist_activity._Activity__max_participants) or (len(artist_activity._Activity__participants) < 2):
                artist_activity._Acitivity__is_active = False
            
            else:
                artist_activity._Activity__is_active = True

            blackrose_list.append(artist_activity)
        for athlete_activity in sports:
            for student in athletes:
                if student._Student__selected_activity == 'Sports' and student._Student__grade_level == athlete_activity._Activity__grade_level and student.is_eligible():
                    athlete_activity._Activity__participants.append(student)
            for teacher in teachers:
                if teacher._Teacher__mentor_grade == athlete_activity._Activity__grade_level:
                    athlete_activity._Activity__organizers.append(teacher)
            if athlete_activity._SportsTournament__game_type == 'Individual':
                if (len(athlete_activity._Activity__participants) > athlete_activity._Activity__max_participants) or (len(athlete_activity._Activity__participants) < 2):
                    athlete_activity._Acitivity__is_active = False
            
                else:
                    athlete_activity._Activity__is_active = True

            else:
                unique_classes_assigned = []
                for parti in athlete_activity._Activity__participants:
                    if parti._Student__class_assigned not in unique_classes_assigned:
                        unique_classes_assigned.append(parti._Student__class_assigned)
                if len(unique_classes_assigned) > athlete_activity._Activity__max_participants or len(unique_classes_assigned) < 2:
                    athlete_activity._Activity__is_active = False
                else:
                    athlete_activity._Activity__is_active = True

            if athlete_activity.activity_name == 'cricket':
                cricket_list.append(athlete_activity)
            else:
                chess_list.append(athlete_activity)
        for academic_activity in acads:
            for student in scholars:
                if student._Student__selected_activity == 'Academic' and student._Student__grade_level == academic_activity._Activity__grade_level and student.is_eligible():
                    academic_activity._Activity__participants.append(student)
            for teacher in teachers:
                if teacher._Teacher__mentor_grade == academic_activity._Activity__grade_level:
                    academic_activity._Activity__organizers.append(teacher)
            if (len(academic_activity._Activity__participants) > academic_activity._Activity__max_participants) or (len(academic_activity._Activity__participants) < 2):
                academic_activity._Acitivity__is_active = False
            
            else:
                academic_activity._Activity__is_active = True

            if academic_activity.activity_name == 'mathematics':
                math_list.append(academic_activity)
            elif academic_activity.activity_name == 'science':
                science_list.append(academic_activity)
            else:
                computers_list.append(academic_activity)

        return cricket_list, chess_list, math_list, science_list, computers_list, blackrose_list

# Defining the winner function
def winner(activities: tuple):
    all_file_list = []
    cricket, chess, math, science, computers, blackrose = activities     # Unpacking the tuple
    for k in chess:
        print(k.__dict__)
    for grade_level in range(6, 13):
        winner_row = [''] * 6
        with open(f'grade{grade_level}.csv', 'a') as final_report:
            csv_writer = csv.writer(final_report)
            csv_writer.writerow(['cricket','chess','mathematics','science','computers','blackrose'])
            for comp in cricket:
                if comp._Activity__grade_level == grade_level:
                    if comp.determine_winner() != -1 and comp._Activity__is_active == True:
                        winner_row[0] = comp.determine_winner().idi
                    else:
                        winner_row[0] = 'NA'
            for comp in chess:
                if comp._Activity__grade_level == grade_level:
                    if comp.determine_winner() != -1 and comp._Activity__is_active == True:
                        winner_row[1] = comp.determine_winner().idi
                    else:
                        winner_row[1] = 'NA'
            for comp in math:
                if comp._Activity__grade_level == grade_level:
                    if comp.determine_winner() != -1 and comp._Activity__is_active == True:
                        winner_row[2] = comp.determine_winner().idi
                    else:
                        winner_row[2] = 'NA'
            for comp in science:
                if comp._Activity__grade_level == grade_level:
                    if comp.determine_winner() != -1 and comp._Activity__is_active == True:
                        winner_row[3] = comp.determine_winner().idi
                    else:
                        winner_row[3] = 'NA'
            for comp in computers:
                if comp._Activity__grade_level == grade_level:
                    if comp.determine_winner() != -1 and comp._Activity__is_active == True:
                        winner_row[4] = comp.determine_winner().idi
                    else:
                        winner_row[4] = 'NA'
            for comp in blackrose:
                if comp._Activity__grade_level == grade_level:
                    if comp.evaluate_talent() != -1 and comp._Activity__is_active == True:
                        winner_row[5] = comp.evaluate_talent().idi
                    else:
                        winner_row[5] = 'NA'
            csv_writer.writerow(winner_row)
        all_file_list.append(f'grade{grade_level}.csv')
    return tuple(all_file_list)
#winner(register_activity('easy_participant_data.csv', 'easy_activity_data.csv'))