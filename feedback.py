import datetime
import os

class Feedback:
    def __init__(self):
        self.lane = ''
        self.champ = ''
        self.time_of_start_to_play = None
        self.time_of_play = None
        self.time_of_record = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.the_reason_of_lose = ''
        self.possible_things = []
        self.what_to_learn = []
        self.next_things_to_do = []

    def write_report(self):
        path = os.getcwd()
        file_name = self.time_of_record+'('+self.lane+'-'+self.champ+')'+'.txt'
        with open(path + '\\' + file_name, 'w') as f:
            f.write(self.lane + ', ' + self.champ + '로 패배.\n')
            f.write('경기 플레이 시간 : ' + self.time_of_play + '\n')
            f.write('경기 시작 시간 : ' + self.time_of_start_to_play.strftime("%Y-%m-%d %H:%M:%S") + '\n')
            f.write('주요 패배의 원인 : ' + self.the_reason_of_lose + '\n')
            f.write('내가 할 수 있었던 것 : \n')
            for i, things in enumerate(self.possible_things):
                f.write('\t' + str(i+1) + '. ' + things + '\n')
            f.write('경기 후 배운 점 : \n')
            for i, things in enumerate(self.what_to_learn):
                f.write('\t' + str(i+1) + '. ' + things + '\n')
            f.write('앞으로 해야할 것 : \n')
            for i, things in enumerate(self.next_things_to_do):
                f.write('\t' + str(i+1) + '. ' + things + '\n')
            


    def get_feedback(self):
        self.lane = input('라인 : ')
        self.champ = input('챔피언 : ')
        self.time_of_play = input('플레이 시간(ex15:57) : ')
        self.time_of_start_to_play = self.get_play_time()
        self.the_reason_of_lose = input('주요 패배의 원인 : ')
        self.set_possible_things()
        self.set_what_to_learn()
        self.set_next_things()
        

    def get_play_time(self):
        play_time = list(map(int, input('경기 시작 시간(ex2017/08/23/17/23) : ').split('/')))
        result = datetime.datetime(year=play_time[0], month=play_time[1], day=play_time[2],
                               hour=play_time[3], minute=play_time[4])
        return result

    def set_possible_things(self):
        self.possible_things = self.get_array_input('본인이 할 수 있었던 것 : ')

    def set_what_to_learn(self):
        self.what_to_learn = self.get_array_input('배운 점 : ')

    def set_next_things(self):
        self.next_things_to_do = self.get_array_input('앞으로 해야할 것 : ')

    def get_array_input(self, help_str):
        result = []
        thing = input(help_str)
        while thing != '':
            result.append(thing)
            thing = input(help_str)
        return result
        
        
