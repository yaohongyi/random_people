#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 都君丨大魔王
import random
from PyQt5 import QtCore


class RandomPeople(QtCore.QThread):
    text = QtCore.pyqtSignal(list)

    def __init__(self, people_num=3):
        super().__init__()
        self.people_num = people_num

    def create_people(self):
        new_people = []
        with open('人员清单.txt', 'r', encoding='utf-8') as file:
            all_people = file.readlines()
        for people in all_people:
            temp = people.strip()
            new_people.append(temp)
        people_list = random.sample(new_people, self.people_num)
        self.text.emit(people_list)
        return people_list

    def run(self):
        self.create_people()


if __name__ == '__main__':
    rp = RandomPeople(3)
    rp.create_people()
