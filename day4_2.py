current_date = 0
current_minute = 0
status = 0
guard_id = 0

guard_status = {}
total_per_guard = {}

# result = re.sub(r"(?im)^\[2018-(\d+)-(\d+) (\d+):(\d+)\] Guard #(\d+) begins shift", r"set_guard(\5, 1\1\2, \3, \4)", subject)
# result = re.sub(r"(?im)^\[2018-(\d+)-(\d+) (\d+):(\d+)\] falls asleep", r"fall_sleep(1\1\2, \3, \4)", subject)
# result = re.sub(r"(?im)^\[2018-(\d+)-(\d+) (\d+):(\d+)\] wakes up", r"wakes_up(1\1\2, \3, \4)", subject)


def set_guard(id, date, h, m):
    global current_date, current_minute, status, guard_id, guard_status, total_per_guard
    if h == 23:
        date += 1
    current_date = date
    current_minute = m
    status = 0
    guard_id = id
    if guard_id not in total_per_guard:
        total_per_guard[guard_id] = 0
    if guard_id not in guard_status:
        guard_status[guard_id] = {}


def wakes_up(date, h, m):
    global current_date, current_minute, status, guard_id, guard_status
    if h == 23:
        date += 1
    current_date = date
    if current_date not in guard_status[guard_id]:
        guard_status[guard_id][current_date] = {}
    if status == 1:
        for i in range(current_minute, m):
            guard_status[guard_id][current_date][i] = 1
            total_per_guard[guard_id] += 1
    current_minute = m
    status = 0


def fall_sleep(date, h, m):
    global current_date, current_minute, status, guard_id, guard_status, total_per_guard
    if h == 23:
        date += 1
    current_date = date
    current_minute = m
    status = 1


set_guard(2141, 10218, 23, 59)
fall_sleep(10219, 0, 24)
wakes_up(10219, 0, 58)
set_guard(2777, 10220, 0, 1)
fall_sleep(10220, 0, 16)
wakes_up(10220, 0, 20)
fall_sleep(10220, 0, 46)
wakes_up(10220, 0, 53)
set_guard(2749, 10221, 0, 0)
fall_sleep(10221, 0, 9)
wakes_up(10221, 0, 49)
set_guard(2749, 10221, 23, 58)
fall_sleep(10222, 0, 48)
wakes_up(10222, 0, 59)
set_guard(2749, 10223, 0, 1)
fall_sleep(10223, 0, 31)
wakes_up(10223, 0, 48)
fall_sleep(10223, 0, 52)
wakes_up(10223, 0, 53)
set_guard(2879, 10224, 0, 2)
fall_sleep(10224, 0, 22)
wakes_up(10224, 0, 32)
fall_sleep(10224, 0, 41)
wakes_up(10224, 0, 55)
set_guard(2141, 10224, 23, 57)
fall_sleep(10225, 0, 42)
wakes_up(10225, 0, 53)
set_guard(2879, 10225, 23, 50)
fall_sleep(10226, 0, 4)
wakes_up(10226, 0, 31)
fall_sleep(10226, 0, 39)
wakes_up(10226, 0, 41)
fall_sleep(10226, 0, 49)
wakes_up(10226, 0, 54)
set_guard(769, 10226, 23, 57)
fall_sleep(10227, 0, 11)
wakes_up(10227, 0, 13)
fall_sleep(10227, 0, 37)
wakes_up(10227, 0, 53)
set_guard(191, 10228, 0, 3)
fall_sleep(10228, 0, 29)
wakes_up(10228, 0, 55)
set_guard(2879, 10228, 23, 56)
fall_sleep(10301, 0, 16)
wakes_up(10301, 0, 35)
fall_sleep(10301, 0, 48)
wakes_up(10301, 0, 51)
set_guard(683, 10301, 23, 58)
fall_sleep(10302, 0, 11)
wakes_up(10302, 0, 32)
set_guard(1721, 10303, 0, 0)
fall_sleep(10303, 0, 19)
wakes_up(10303, 0, 48)
set_guard(2879, 10304, 0, 1)
fall_sleep(10304, 0, 46)
wakes_up(10304, 0, 51)
set_guard(773, 10304, 23, 57)
fall_sleep(10305, 0, 8)
wakes_up(10305, 0, 21)
fall_sleep(10305, 0, 41)
wakes_up(10305, 0, 43)
set_guard(2777, 10305, 23, 57)
fall_sleep(10306, 0, 24)
wakes_up(10306, 0, 44)
fall_sleep(10306, 0, 50)
wakes_up(10306, 0, 56)
set_guard(1213, 10306, 23, 59)
fall_sleep(10307, 0, 37)
wakes_up(10307, 0, 53)
set_guard(2749, 10308, 0, 0)
fall_sleep(10308, 0, 29)
wakes_up(10308, 0, 55)
set_guard(769, 10309, 0, 4)
fall_sleep(10309, 0, 19)
wakes_up(10309, 0, 51)
set_guard(2141, 10309, 23, 48)
fall_sleep(10310, 0, 3)
wakes_up(10310, 0, 11)
set_guard(2777, 10310, 23, 58)
fall_sleep(10311, 0, 10)
wakes_up(10311, 0, 52)
set_guard(191, 10312, 0, 3)
fall_sleep(10312, 0, 57)
wakes_up(10312, 0, 59)
set_guard(769, 10313, 0, 1)
fall_sleep(10313, 0, 24)
wakes_up(10313, 0, 50)
fall_sleep(10313, 0, 55)
wakes_up(10313, 0, 58)
set_guard(1907, 10313, 23, 59)
fall_sleep(10314, 0, 8)
wakes_up(10314, 0, 47)
fall_sleep(10314, 0, 53)
wakes_up(10314, 0, 55)
set_guard(2879, 10314, 23, 58)
fall_sleep(10315, 0, 27)
wakes_up(10315, 0, 53)
set_guard(1907, 10316, 0, 2)
fall_sleep(10316, 0, 7)
wakes_up(10316, 0, 47)
set_guard(97, 10316, 23, 49)
fall_sleep(10317, 0, 4)
wakes_up(10317, 0, 26)
fall_sleep(10317, 0, 42)
wakes_up(10317, 0, 44)
set_guard(2749, 10318, 0, 0)
fall_sleep(10318, 0, 42)
wakes_up(10318, 0, 47)
set_guard(2879, 10319, 0, 3)
fall_sleep(10319, 0, 10)
wakes_up(10319, 0, 59)
set_guard(2777, 10320, 0, 0)
fall_sleep(10320, 0, 31)
wakes_up(10320, 0, 35)
set_guard(1493, 10320, 23, 56)
fall_sleep(10321, 0, 31)
wakes_up(10321, 0, 51)
set_guard(1049, 10322, 0, 0)
fall_sleep(10322, 0, 6)
wakes_up(10322, 0, 57)
set_guard(2879, 10323, 0, 0)
fall_sleep(10323, 0, 48)
wakes_up(10323, 0, 53)
set_guard(1277, 10324, 0, 1)
fall_sleep(10324, 0, 32)
wakes_up(10324, 0, 38)
set_guard(991, 10324, 23, 47)
fall_sleep(10325, 0, 0)
wakes_up(10325, 0, 36)
fall_sleep(10325, 0, 42)
wakes_up(10325, 0, 50)
set_guard(2749, 10326, 0, 0)
fall_sleep(10326, 0, 9)
wakes_up(10326, 0, 27)
fall_sleep(10326, 0, 37)
wakes_up(10326, 0, 48)
fall_sleep(10326, 0, 51)
wakes_up(10326, 0, 58)
set_guard(2141, 10326, 23, 59)
fall_sleep(10327, 0, 25)
wakes_up(10327, 0, 57)
set_guard(2713, 10328, 0, 0)
fall_sleep(10328, 0, 6)
wakes_up(10328, 0, 21)
fall_sleep(10328, 0, 50)
wakes_up(10328, 0, 52)
fall_sleep(10328, 0, 57)
wakes_up(10328, 0, 58)
set_guard(1277, 10329, 0, 2)
fall_sleep(10329, 0, 30)
wakes_up(10329, 0, 54)
set_guard(2711, 10330, 0, 0)
fall_sleep(10330, 0, 52)
wakes_up(10330, 0, 53)
fall_sleep(10330, 0, 57)
wakes_up(10330, 0, 59)
set_guard(1907, 10330, 23, 59)
fall_sleep(10331, 0, 31)
wakes_up(10331, 0, 34)
fall_sleep(10331, 0, 49)
wakes_up(10331, 0, 55)
set_guard(1049, 10401, 0, 1)
fall_sleep(10401, 0, 34)
wakes_up(10401, 0, 56)
set_guard(2879, 10402, 0, 1)
fall_sleep(10402, 0, 27)
wakes_up(10402, 0, 29)
fall_sleep(10402, 0, 46)
wakes_up(10402, 0, 58)
set_guard(191, 10403, 0, 2)
fall_sleep(10403, 0, 26)
wakes_up(10403, 0, 29)
set_guard(2711, 10404, 0, 0)
fall_sleep(10404, 0, 14)
wakes_up(10404, 0, 32)
fall_sleep(10404, 0, 47)
wakes_up(10404, 0, 57)
set_guard(1721, 10405, 0, 3)
fall_sleep(10405, 0, 14)
wakes_up(10405, 0, 30)
set_guard(1907, 10405, 23, 53)
fall_sleep(10406, 0, 2)
wakes_up(10406, 0, 12)
fall_sleep(10406, 0, 32)
wakes_up(10406, 0, 42)
fall_sleep(10406, 0, 47)
wakes_up(10406, 0, 53)
set_guard(2749, 10406, 23, 59)
fall_sleep(10407, 0, 25)
wakes_up(10407, 0, 35)
fall_sleep(10407, 0, 42)
wakes_up(10407, 0, 54)
set_guard(769, 10408, 0, 2)
fall_sleep(10408, 0, 14)
wakes_up(10408, 0, 50)
set_guard(2711, 10409, 0, 2)
fall_sleep(10409, 0, 23)
wakes_up(10409, 0, 59)
set_guard(2711, 10410, 0, 2)
fall_sleep(10410, 0, 14)
wakes_up(10410, 0, 33)
fall_sleep(10410, 0, 49)
wakes_up(10410, 0, 53)
set_guard(1907, 10411, 0, 1)
fall_sleep(10411, 0, 29)
wakes_up(10411, 0, 54)
set_guard(191, 10411, 23, 56)
fall_sleep(10412, 0, 22)
wakes_up(10412, 0, 38)
set_guard(2113, 10413, 0, 0)
set_guard(769, 10414, 0, 1)
fall_sleep(10414, 0, 35)
wakes_up(10414, 0, 41)
fall_sleep(10414, 0, 44)
wakes_up(10414, 0, 53)
set_guard(1049, 10415, 0, 0)
fall_sleep(10415, 0, 25)
wakes_up(10415, 0, 30)
fall_sleep(10415, 0, 37)
wakes_up(10415, 0, 39)
set_guard(2777, 10416, 0, 2)
fall_sleep(10416, 0, 12)
wakes_up(10416, 0, 23)
fall_sleep(10416, 0, 47)
wakes_up(10416, 0, 59)
set_guard(1721, 10417, 0, 3)
fall_sleep(10417, 0, 16)
wakes_up(10417, 0, 17)
fall_sleep(10417, 0, 32)
wakes_up(10417, 0, 43)
set_guard(1049, 10418, 0, 0)
fall_sleep(10418, 0, 10)
wakes_up(10418, 0, 21)
fall_sleep(10418, 0, 35)
wakes_up(10418, 0, 58)
set_guard(191, 10419, 0, 0)
fall_sleep(10419, 0, 36)
wakes_up(10419, 0, 49)
fall_sleep(10419, 0, 52)
wakes_up(10419, 0, 59)
set_guard(773, 10419, 23, 48)
fall_sleep(10420, 0, 2)
wakes_up(10420, 0, 31)
set_guard(2777, 10420, 23, 56)
fall_sleep(10421, 0, 25)
wakes_up(10421, 0, 52)
set_guard(2917, 10422, 0, 2)
fall_sleep(10422, 0, 18)
wakes_up(10422, 0, 48)
set_guard(1277, 10423, 0, 0)
fall_sleep(10423, 0, 26)
wakes_up(10423, 0, 43)
set_guard(1049, 10424, 0, 2)
fall_sleep(10424, 0, 31)
wakes_up(10424, 0, 41)
set_guard(1493, 10425, 0, 1)
fall_sleep(10425, 0, 7)
wakes_up(10425, 0, 26)
fall_sleep(10425, 0, 35)
wakes_up(10425, 0, 37)
set_guard(2879, 10426, 0, 3)
fall_sleep(10426, 0, 50)
wakes_up(10426, 0, 54)
set_guard(1493, 10427, 0, 3)
fall_sleep(10427, 0, 13)
wakes_up(10427, 0, 35)
fall_sleep(10427, 0, 40)
wakes_up(10427, 0, 53)
set_guard(769, 10428, 0, 2)
fall_sleep(10428, 0, 14)
wakes_up(10428, 0, 29)
fall_sleep(10428, 0, 36)
wakes_up(10428, 0, 53)
set_guard(773, 10428, 23, 53)
fall_sleep(10429, 0, 3)
wakes_up(10429, 0, 4)
fall_sleep(10429, 0, 40)
wakes_up(10429, 0, 56)
set_guard(2711, 10430, 0, 0)
fall_sleep(10430, 0, 14)
wakes_up(10430, 0, 20)
set_guard(2711, 10430, 23, 57)
fall_sleep(10501, 0, 43)
wakes_up(10501, 0, 51)
set_guard(2141, 10501, 23, 59)
fall_sleep(10502, 0, 22)
wakes_up(10502, 0, 26)
fall_sleep(10502, 0, 32)
wakes_up(10502, 0, 54)
set_guard(2917, 10502, 23, 58)
fall_sleep(10503, 0, 22)
wakes_up(10503, 0, 38)
fall_sleep(10503, 0, 53)
wakes_up(10503, 0, 54)
set_guard(2879, 10503, 23, 57)
fall_sleep(10504, 0, 45)
wakes_up(10504, 0, 50)
fall_sleep(10504, 0, 53)
wakes_up(10504, 0, 59)
set_guard(191, 10505, 0, 1)
fall_sleep(10505, 0, 27)
wakes_up(10505, 0, 57)
set_guard(2917, 10505, 23, 59)
fall_sleep(10506, 0, 11)
wakes_up(10506, 0, 36)
set_guard(1049, 10506, 23, 59)
fall_sleep(10507, 0, 17)
wakes_up(10507, 0, 22)
set_guard(773, 10507, 23, 58)
fall_sleep(10508, 0, 12)
wakes_up(10508, 0, 55)
set_guard(1277, 10509, 0, 0)
fall_sleep(10509, 0, 13)
wakes_up(10509, 0, 37)
fall_sleep(10509, 0, 48)
wakes_up(10509, 0, 55)
set_guard(1049, 10509, 23, 58)
fall_sleep(10510, 0, 33)
wakes_up(10510, 0, 34)
fall_sleep(10510, 0, 40)
wakes_up(10510, 0, 58)
set_guard(1213, 10510, 23, 46)
fall_sleep(10511, 0, 5)
wakes_up(10511, 0, 41)
fall_sleep(10511, 0, 49)
wakes_up(10511, 0, 56)
set_guard(1049, 10511, 23, 47)
fall_sleep(10512, 0, 0)
wakes_up(10512, 0, 56)
set_guard(1493, 10512, 23, 58)
fall_sleep(10513, 0, 44)
wakes_up(10513, 0, 53)
fall_sleep(10513, 0, 57)
wakes_up(10513, 0, 58)
set_guard(1277, 10514, 0, 2)
fall_sleep(10514, 0, 13)
wakes_up(10514, 0, 14)
fall_sleep(10514, 0, 27)
wakes_up(10514, 0, 50)
set_guard(1187, 10515, 0, 4)
fall_sleep(10515, 0, 47)
wakes_up(10515, 0, 51)
set_guard(2879, 10515, 23, 56)
fall_sleep(10516, 0, 8)
wakes_up(10516, 0, 34)
fall_sleep(10516, 0, 39)
wakes_up(10516, 0, 54)
set_guard(773, 10517, 0, 0)
fall_sleep(10517, 0, 23)
wakes_up(10517, 0, 41)
fall_sleep(10517, 0, 53)
wakes_up(10517, 0, 58)
set_guard(991, 10517, 23, 59)
fall_sleep(10518, 0, 20)
wakes_up(10518, 0, 47)
set_guard(2749, 10519, 0, 2)
fall_sleep(10519, 0, 36)
wakes_up(10519, 0, 46)
fall_sleep(10519, 0, 49)
wakes_up(10519, 0, 53)
set_guard(2917, 10519, 23, 51)
fall_sleep(10520, 0, 3)
wakes_up(10520, 0, 26)
fall_sleep(10520, 0, 33)
wakes_up(10520, 0, 59)
set_guard(1277, 10521, 0, 0)
fall_sleep(10521, 0, 51)
wakes_up(10521, 0, 52)
fall_sleep(10521, 0, 56)
wakes_up(10521, 0, 58)
set_guard(1907, 10522, 0, 2)
fall_sleep(10522, 0, 31)
wakes_up(10522, 0, 38)
fall_sleep(10522, 0, 55)
wakes_up(10522, 0, 57)
set_guard(1277, 10523, 0, 4)
fall_sleep(10523, 0, 31)
wakes_up(10523, 0, 37)
fall_sleep(10523, 0, 47)
wakes_up(10523, 0, 59)
set_guard(2777, 10523, 23, 58)
fall_sleep(10524, 0, 45)
wakes_up(10524, 0, 53)
set_guard(1721, 10524, 23, 56)
fall_sleep(10525, 0, 26)
wakes_up(10525, 0, 40)
fall_sleep(10525, 0, 43)
wakes_up(10525, 0, 52)
set_guard(769, 10526, 0, 0)
fall_sleep(10526, 0, 6)
wakes_up(10526, 0, 37)
set_guard(2777, 10527, 0, 4)
fall_sleep(10527, 0, 17)
wakes_up(10527, 0, 19)
fall_sleep(10527, 0, 37)
wakes_up(10527, 0, 58)
set_guard(2113, 10527, 23, 57)
set_guard(2713, 10529, 0, 0)
fall_sleep(10529, 0, 15)
wakes_up(10529, 0, 51)
set_guard(2141, 10530, 0, 0)
fall_sleep(10530, 0, 38)
wakes_up(10530, 0, 51)
set_guard(1213, 10531, 0, 4)
fall_sleep(10531, 0, 13)
wakes_up(10531, 0, 20)
fall_sleep(10531, 0, 23)
wakes_up(10531, 0, 31)
set_guard(2879, 10531, 23, 54)
fall_sleep(10601, 0, 5)
wakes_up(10601, 0, 11)
fall_sleep(10601, 0, 33)
wakes_up(10601, 0, 55)
set_guard(1277, 10601, 23, 56)
fall_sleep(10602, 0, 36)
wakes_up(10602, 0, 56)
set_guard(1381, 10603, 0, 0)
set_guard(1907, 10604, 0, 2)
fall_sleep(10604, 0, 37)
wakes_up(10604, 0, 44)
fall_sleep(10604, 0, 55)
wakes_up(10604, 0, 56)
set_guard(1277, 10604, 23, 58)
fall_sleep(10605, 0, 15)
wakes_up(10605, 0, 55)
set_guard(769, 10606, 0, 2)
fall_sleep(10606, 0, 27)
wakes_up(10606, 0, 59)
set_guard(1721, 10606, 23, 50)
fall_sleep(10607, 0, 5)
wakes_up(10607, 0, 36)
fall_sleep(10607, 0, 41)
wakes_up(10607, 0, 43)
fall_sleep(10607, 0, 48)
wakes_up(10607, 0, 51)
set_guard(1049, 10608, 0, 4)
fall_sleep(10608, 0, 10)
wakes_up(10608, 0, 51)
fall_sleep(10608, 0, 56)
wakes_up(10608, 0, 58)
set_guard(97, 10609, 0, 3)
fall_sleep(10609, 0, 54)
wakes_up(10609, 0, 55)
set_guard(1049, 10610, 0, 3)
fall_sleep(10610, 0, 12)
wakes_up(10610, 0, 51)
set_guard(1049, 10611, 0, 1)
fall_sleep(10611, 0, 25)
wakes_up(10611, 0, 52)
set_guard(2749, 10611, 23, 56)
fall_sleep(10612, 0, 29)
wakes_up(10612, 0, 53)
set_guard(1187, 10613, 0, 2)
fall_sleep(10613, 0, 39)
wakes_up(10613, 0, 57)
set_guard(2879, 10614, 0, 2)
fall_sleep(10614, 0, 31)
wakes_up(10614, 0, 56)
set_guard(1907, 10614, 23, 58)
fall_sleep(10615, 0, 37)
wakes_up(10615, 0, 57)
set_guard(769, 10615, 23, 57)
fall_sleep(10616, 0, 12)
wakes_up(10616, 0, 48)
fall_sleep(10616, 0, 56)
wakes_up(10616, 0, 57)
set_guard(2711, 10616, 23, 56)
fall_sleep(10617, 0, 6)
wakes_up(10617, 0, 52)
set_guard(2879, 10618, 0, 1)
fall_sleep(10618, 0, 21)
wakes_up(10618, 0, 58)
set_guard(191, 10618, 23, 57)
fall_sleep(10619, 0, 7)
wakes_up(10619, 0, 19)
fall_sleep(10619, 0, 30)
wakes_up(10619, 0, 35)
set_guard(1721, 10620, 0, 0)
fall_sleep(10620, 0, 33)
wakes_up(10620, 0, 45)
fall_sleep(10620, 0, 54)
wakes_up(10620, 0, 55)
set_guard(2711, 10621, 0, 1)
fall_sleep(10621, 0, 27)
wakes_up(10621, 0, 52)
set_guard(1049, 10621, 23, 50)
fall_sleep(10622, 0, 5)
wakes_up(10622, 0, 41)
set_guard(2777, 10622, 23, 59)
fall_sleep(10623, 0, 27)
wakes_up(10623, 0, 34)
set_guard(2141, 10624, 0, 2)
fall_sleep(10624, 0, 42)
wakes_up(10624, 0, 54)
set_guard(97, 10624, 23, 59)
fall_sleep(10625, 0, 27)
wakes_up(10625, 0, 46)
set_guard(1049, 10625, 23, 50)
fall_sleep(10626, 0, 2)
wakes_up(10626, 0, 29)
fall_sleep(10626, 0, 37)
wakes_up(10626, 0, 58)
set_guard(1277, 10626, 23, 59)
fall_sleep(10627, 0, 20)
wakes_up(10627, 0, 57)
set_guard(191, 10627, 23, 56)
fall_sleep(10628, 0, 7)
wakes_up(10628, 0, 9)
set_guard(1493, 10628, 23, 51)
fall_sleep(10629, 0, 1)
wakes_up(10629, 0, 7)
fall_sleep(10629, 0, 15)
wakes_up(10629, 0, 25)
fall_sleep(10629, 0, 53)
wakes_up(10629, 0, 57)
set_guard(769, 10629, 23, 46)
fall_sleep(10630, 0, 1)
wakes_up(10630, 0, 51)
set_guard(2713, 10630, 23, 53)
fall_sleep(10701, 0, 2)
wakes_up(10701, 0, 25)
fall_sleep(10701, 0, 35)
wakes_up(10701, 0, 45)
set_guard(769, 10702, 0, 3)
fall_sleep(10702, 0, 16)
wakes_up(10702, 0, 44)
set_guard(1277, 10703, 0, 4)
fall_sleep(10703, 0, 25)
wakes_up(10703, 0, 35)
fall_sleep(10703, 0, 47)
wakes_up(10703, 0, 54)
set_guard(769, 10704, 0, 0)
fall_sleep(10704, 0, 21)
wakes_up(10704, 0, 42)
set_guard(1213, 10704, 23, 58)
fall_sleep(10705, 0, 53)
wakes_up(10705, 0, 58)
set_guard(2777, 10706, 0, 0)
fall_sleep(10706, 0, 25)
wakes_up(10706, 0, 38)
set_guard(1213, 10706, 23, 58)
fall_sleep(10707, 0, 12)
wakes_up(10707, 0, 41)
set_guard(2711, 10708, 0, 0)
fall_sleep(10708, 0, 22)
wakes_up(10708, 0, 42)
set_guard(191, 10709, 0, 0)
fall_sleep(10709, 0, 21)
wakes_up(10709, 0, 53)
set_guard(991, 10709, 23, 49)
fall_sleep(10710, 0, 1)
wakes_up(10710, 0, 15)
fall_sleep(10710, 0, 41)
wakes_up(10710, 0, 50)
set_guard(1721, 10710, 23, 58)
fall_sleep(10711, 0, 28)
wakes_up(10711, 0, 45)
set_guard(1213, 10711, 23, 58)
fall_sleep(10712, 0, 23)
wakes_up(10712, 0, 48)
fall_sleep(10712, 0, 54)
wakes_up(10712, 0, 55)
set_guard(1277, 10712, 23, 57)
fall_sleep(10713, 0, 20)
wakes_up(10713, 0, 51)
set_guard(2917, 10714, 0, 3)
fall_sleep(10714, 0, 21)
wakes_up(10714, 0, 45)
fall_sleep(10714, 0, 55)
wakes_up(10714, 0, 57)
set_guard(1213, 10715, 0, 1)
fall_sleep(10715, 0, 38)
wakes_up(10715, 0, 56)
set_guard(2711, 10715, 23, 57)
fall_sleep(10716, 0, 17)
wakes_up(10716, 0, 27)
set_guard(1907, 10717, 0, 1)
fall_sleep(10717, 0, 38)
wakes_up(10717, 0, 39)
fall_sleep(10717, 0, 44)
wakes_up(10717, 0, 56)
set_guard(1049, 10718, 0, 0)
fall_sleep(10718, 0, 29)
wakes_up(10718, 0, 54)
set_guard(2713, 10719, 0, 0)
fall_sleep(10719, 0, 15)
wakes_up(10719, 0, 33)
fall_sleep(10719, 0, 51)
wakes_up(10719, 0, 56)
set_guard(2777, 10719, 23, 59)
fall_sleep(10720, 0, 7)
wakes_up(10720, 0, 19)
fall_sleep(10720, 0, 42)
wakes_up(10720, 0, 49)
fall_sleep(10720, 0, 55)
wakes_up(10720, 0, 56)
set_guard(2713, 10720, 23, 57)
fall_sleep(10721, 0, 24)
wakes_up(10721, 0, 56)
set_guard(1277, 10722, 0, 2)
fall_sleep(10722, 0, 16)
wakes_up(10722, 0, 28)
fall_sleep(10722, 0, 33)
wakes_up(10722, 0, 43)
fall_sleep(10722, 0, 46)
wakes_up(10722, 0, 52)
set_guard(2713, 10722, 23, 56)
fall_sleep(10723, 0, 23)
wakes_up(10723, 0, 47)
set_guard(2749, 10724, 0, 2)
fall_sleep(10724, 0, 10)
wakes_up(10724, 0, 59)
set_guard(1493, 10724, 23, 58)
fall_sleep(10725, 0, 18)
wakes_up(10725, 0, 39)
set_guard(1187, 10726, 0, 0)
fall_sleep(10726, 0, 17)
wakes_up(10726, 0, 40)
set_guard(1907, 10727, 0, 3)
fall_sleep(10727, 0, 52)
wakes_up(10727, 0, 56)
set_guard(1381, 10728, 0, 0)
set_guard(1213, 10728, 23, 57)
fall_sleep(10729, 0, 12)
wakes_up(10729, 0, 19)
fall_sleep(10729, 0, 24)
wakes_up(10729, 0, 25)
set_guard(2141, 10729, 23, 56)
fall_sleep(10730, 0, 40)
wakes_up(10730, 0, 57)
set_guard(1493, 10730, 23, 58)
fall_sleep(10731, 0, 10)
wakes_up(10731, 0, 40)
fall_sleep(10731, 0, 49)
wakes_up(10731, 0, 58)
set_guard(683, 10731, 23, 49)
fall_sleep(10801, 0, 2)
wakes_up(10801, 0, 11)
fall_sleep(10801, 0, 40)
wakes_up(10801, 0, 58)
set_guard(2713, 10802, 0, 0)
fall_sleep(10802, 0, 7)
wakes_up(10802, 0, 55)
set_guard(683, 10802, 23, 59)
fall_sleep(10803, 0, 7)
wakes_up(10803, 0, 55)
set_guard(1213, 10804, 0, 4)
fall_sleep(10804, 0, 25)
wakes_up(10804, 0, 38)
fall_sleep(10804, 0, 48)
wakes_up(10804, 0, 56)
set_guard(1049, 10804, 23, 57)
fall_sleep(10805, 0, 32)
wakes_up(10805, 0, 53)
set_guard(2917, 10805, 23, 59)
fall_sleep(10806, 0, 39)
wakes_up(10806, 0, 59)
set_guard(1049, 10806, 23, 59)
fall_sleep(10807, 0, 22)
wakes_up(10807, 0, 49)
fall_sleep(10807, 0, 52)
wakes_up(10807, 0, 56)
set_guard(2879, 10808, 0, 3)
fall_sleep(10808, 0, 45)
wakes_up(10808, 0, 52)
set_guard(683, 10809, 0, 3)
fall_sleep(10809, 0, 6)
wakes_up(10809, 0, 40)
fall_sleep(10809, 0, 46)
wakes_up(10809, 0, 59)
set_guard(769, 10810, 0, 3)
fall_sleep(10810, 0, 33)
wakes_up(10810, 0, 55)
set_guard(1213, 10810, 23, 58)
fall_sleep(10811, 0, 28)
wakes_up(10811, 0, 59)
set_guard(991, 10811, 23, 59)
fall_sleep(10812, 0, 51)
wakes_up(10812, 0, 55)
set_guard(2777, 10813, 0, 2)
fall_sleep(10813, 0, 23)
wakes_up(10813, 0, 57)
set_guard(97, 10813, 23, 59)
fall_sleep(10814, 0, 30)
wakes_up(10814, 0, 58)
set_guard(769, 10814, 23, 59)
fall_sleep(10815, 0, 6)
wakes_up(10815, 0, 32)
fall_sleep(10815, 0, 35)
wakes_up(10815, 0, 36)
fall_sleep(10815, 0, 49)
wakes_up(10815, 0, 56)
set_guard(1277, 10815, 23, 50)
fall_sleep(10816, 0, 0)
wakes_up(10816, 0, 54)
set_guard(2141, 10816, 23, 57)
fall_sleep(10817, 0, 33)
wakes_up(10817, 0, 54)
set_guard(2917, 10817, 23, 57)
fall_sleep(10818, 0, 12)
wakes_up(10818, 0, 14)
fall_sleep(10818, 0, 35)
wakes_up(10818, 0, 45)
set_guard(2711, 10819, 0, 3)
fall_sleep(10819, 0, 26)
wakes_up(10819, 0, 32)
fall_sleep(10819, 0, 37)
wakes_up(10819, 0, 51)
set_guard(683, 10819, 23, 50)
fall_sleep(10820, 0, 4)
wakes_up(10820, 0, 26)
fall_sleep(10820, 0, 36)
wakes_up(10820, 0, 42)
fall_sleep(10820, 0, 51)
wakes_up(10820, 0, 58)
set_guard(2141, 10820, 23, 56)
fall_sleep(10821, 0, 11)
wakes_up(10821, 0, 19)
fall_sleep(10821, 0, 40)
wakes_up(10821, 0, 45)
fall_sleep(10821, 0, 55)
wakes_up(10821, 0, 57)
set_guard(1277, 10822, 0, 1)
fall_sleep(10822, 0, 9)
wakes_up(10822, 0, 29)
fall_sleep(10822, 0, 32)
wakes_up(10822, 0, 45)
set_guard(1277, 10823, 0, 1)
fall_sleep(10823, 0, 45)
wakes_up(10823, 0, 50)
set_guard(1213, 10824, 0, 3)
fall_sleep(10824, 0, 12)
wakes_up(10824, 0, 16)
fall_sleep(10824, 0, 33)
wakes_up(10824, 0, 41)
set_guard(1187, 10824, 23, 50)
fall_sleep(10825, 0, 5)
wakes_up(10825, 0, 6)
fall_sleep(10825, 0, 48)
wakes_up(10825, 0, 50)
fall_sleep(10825, 0, 55)
wakes_up(10825, 0, 57)
set_guard(2917, 10826, 0, 0)
fall_sleep(10826, 0, 13)
wakes_up(10826, 0, 41)
set_guard(2141, 10826, 23, 56)
fall_sleep(10827, 0, 24)
wakes_up(10827, 0, 46)
fall_sleep(10827, 0, 54)
wakes_up(10827, 0, 59)
set_guard(97, 10828, 0, 3)
fall_sleep(10828, 0, 10)
wakes_up(10828, 0, 12)
fall_sleep(10828, 0, 18)
wakes_up(10828, 0, 34)
set_guard(1049, 10829, 0, 3)
fall_sleep(10829, 0, 41)
wakes_up(10829, 0, 59)
set_guard(1213, 10829, 23, 56)
fall_sleep(10830, 0, 23)
wakes_up(10830, 0, 28)
fall_sleep(10830, 0, 31)
wakes_up(10830, 0, 41)
set_guard(1907, 10831, 0, 0)
fall_sleep(10831, 0, 39)
wakes_up(10831, 0, 57)
set_guard(1721, 10831, 23, 58)
fall_sleep(10901, 0, 25)
wakes_up(10901, 0, 58)
set_guard(1721, 10901, 23, 59)
fall_sleep(10902, 0, 10)
wakes_up(10902, 0, 59)
set_guard(2917, 10903, 0, 1)
fall_sleep(10903, 0, 20)
wakes_up(10903, 0, 53)
set_guard(97, 10903, 23, 50)
fall_sleep(10904, 0, 3)
wakes_up(10904, 0, 22)
fall_sleep(10904, 0, 45)
wakes_up(10904, 0, 49)
set_guard(1049, 10905, 0, 2)
fall_sleep(10905, 0, 14)
wakes_up(10905, 0, 51)
set_guard(191, 10906, 0, 2)
fall_sleep(10906, 0, 46)
wakes_up(10906, 0, 50)
set_guard(1493, 10907, 0, 1)
fall_sleep(10907, 0, 35)
wakes_up(10907, 0, 50)
set_guard(2879, 10908, 0, 0)
fall_sleep(10908, 0, 49)
wakes_up(10908, 0, 54)
set_guard(2777, 10908, 23, 47)
fall_sleep(10909, 0, 5)
wakes_up(10909, 0, 23)
fall_sleep(10909, 0, 38)
wakes_up(10909, 0, 57)
set_guard(769, 10910, 0, 0)
fall_sleep(10910, 0, 34)
wakes_up(10910, 0, 43)
set_guard(1493, 10910, 23, 58)
fall_sleep(10911, 0, 31)
wakes_up(10911, 0, 48)
set_guard(1721, 10911, 23, 48)
fall_sleep(10912, 0, 1)
wakes_up(10912, 0, 18)
fall_sleep(10912, 0, 23)
wakes_up(10912, 0, 27)
fall_sleep(10912, 0, 56)
wakes_up(10912, 0, 58)
set_guard(991, 10912, 23, 59)
fall_sleep(10913, 0, 21)
wakes_up(10913, 0, 36)
set_guard(773, 10914, 0, 2)
fall_sleep(10914, 0, 15)
wakes_up(10914, 0, 53)
set_guard(1493, 10914, 23, 58)
fall_sleep(10915, 0, 16)
wakes_up(10915, 0, 56)
set_guard(97, 10916, 0, 0)
fall_sleep(10916, 0, 16)
wakes_up(10916, 0, 27)
fall_sleep(10916, 0, 38)
wakes_up(10916, 0, 45)
fall_sleep(10916, 0, 49)
wakes_up(10916, 0, 59)
set_guard(2749, 10917, 0, 0)
fall_sleep(10917, 0, 11)
wakes_up(10917, 0, 48)
set_guard(2777, 10918, 0, 0)
fall_sleep(10918, 0, 26)
wakes_up(10918, 0, 58)
set_guard(769, 10919, 0, 1)
fall_sleep(10919, 0, 41)
wakes_up(10919, 0, 54)
set_guard(991, 10919, 23, 48)
fall_sleep(10920, 0, 1)
wakes_up(10920, 0, 5)
fall_sleep(10920, 0, 25)
wakes_up(10920, 0, 39)
set_guard(2917, 10921, 0, 4)
fall_sleep(10921, 0, 19)
wakes_up(10921, 0, 51)
set_guard(97, 10921, 23, 59)
fall_sleep(10922, 0, 14)
wakes_up(10922, 0, 41)
set_guard(991, 10922, 23, 47)
fall_sleep(10923, 0, 5)
wakes_up(10923, 0, 6)
fall_sleep(10923, 0, 16)
wakes_up(10923, 0, 47)
set_guard(1907, 10923, 23, 47)
fall_sleep(10924, 0, 2)
wakes_up(10924, 0, 35)
fall_sleep(10924, 0, 46)
wakes_up(10924, 0, 48)
fall_sleep(10924, 0, 51)
wakes_up(10924, 0, 56)
set_guard(191, 10924, 23, 57)
fall_sleep(10925, 0, 25)
wakes_up(10925, 0, 33)
fall_sleep(10925, 0, 51)
wakes_up(10925, 0, 59)
set_guard(191, 10925, 23, 57)
fall_sleep(10926, 0, 53)
wakes_up(10926, 0, 56)
set_guard(1187, 10926, 23, 56)
fall_sleep(10927, 0, 13)
wakes_up(10927, 0, 54)
set_guard(2777, 10928, 0, 3)
fall_sleep(10928, 0, 13)
wakes_up(10928, 0, 44)
fall_sleep(10928, 0, 48)
wakes_up(10928, 0, 57)
set_guard(2917, 10928, 23, 54)
fall_sleep(10929, 0, 1)
wakes_up(10929, 0, 22)
fall_sleep(10929, 0, 34)
wakes_up(10929, 0, 50)
set_guard(1049, 10930, 0, 1)
fall_sleep(10930, 0, 7)
wakes_up(10930, 0, 8)
fall_sleep(10930, 0, 12)
wakes_up(10930, 0, 43)
fall_sleep(10930, 0, 49)
wakes_up(10930, 0, 51)
set_guard(2749, 11001, 0, 0)
fall_sleep(11001, 0, 39)
wakes_up(11001, 0, 41)
fall_sleep(11001, 0, 44)
wakes_up(11001, 0, 48)
set_guard(2879, 11002, 0, 1)
fall_sleep(11002, 0, 8)
wakes_up(11002, 0, 14)
fall_sleep(11002, 0, 53)
wakes_up(11002, 0, 54)
set_guard(769, 11003, 0, 1)
fall_sleep(11003, 0, 9)
wakes_up(11003, 0, 19)
fall_sleep(11003, 0, 47)
wakes_up(11003, 0, 49)
fall_sleep(11003, 0, 53)
wakes_up(11003, 0, 55)
set_guard(1721, 11003, 23, 57)
fall_sleep(11004, 0, 41)
wakes_up(11004, 0, 57)
set_guard(2917, 11005, 0, 4)
fall_sleep(11005, 0, 21)
wakes_up(11005, 0, 41)
set_guard(2749, 11006, 0, 0)
fall_sleep(11006, 0, 45)
wakes_up(11006, 0, 46)
set_guard(191, 11006, 23, 57)
fall_sleep(11007, 0, 41)
wakes_up(11007, 0, 50)
fall_sleep(11007, 0, 55)
wakes_up(11007, 0, 59)
set_guard(2917, 11007, 23, 57)
fall_sleep(11008, 0, 27)
wakes_up(11008, 0, 58)
set_guard(2749, 11008, 23, 56)
fall_sleep(11009, 0, 43)
wakes_up(11009, 0, 47)
set_guard(2917, 11010, 0, 3)
fall_sleep(11010, 0, 28)
wakes_up(11010, 0, 30)
fall_sleep(11010, 0, 39)
wakes_up(11010, 0, 56)
set_guard(1277, 11010, 23, 59)
fall_sleep(11011, 0, 13)
wakes_up(11011, 0, 35)
set_guard(1187, 11012, 0, 1)
fall_sleep(11012, 0, 24)
wakes_up(11012, 0, 41)
set_guard(2711, 11012, 23, 58)
fall_sleep(11013, 0, 33)
wakes_up(11013, 0, 52)
set_guard(2917, 11014, 0, 1)
fall_sleep(11014, 0, 45)
wakes_up(11014, 0, 55)
set_guard(2917, 11015, 0, 4)
fall_sleep(11015, 0, 23)
wakes_up(11015, 0, 39)
set_guard(191, 11016, 0, 0)
fall_sleep(11016, 0, 21)
wakes_up(11016, 0, 40)
fall_sleep(11016, 0, 49)
wakes_up(11016, 0, 59)
set_guard(2879, 11017, 0, 0)
fall_sleep(11017, 0, 12)
wakes_up(11017, 0, 50)
set_guard(2879, 11018, 0, 3)
fall_sleep(11018, 0, 28)
wakes_up(11018, 0, 56)
set_guard(2711, 11019, 0, 3)
fall_sleep(11019, 0, 14)
wakes_up(11019, 0, 55)
set_guard(1213, 11019, 23, 56)
fall_sleep(11020, 0, 21)
wakes_up(11020, 0, 25)
fall_sleep(11020, 0, 33)
wakes_up(11020, 0, 44)
set_guard(191, 11020, 23, 56)
fall_sleep(11021, 0, 40)
wakes_up(11021, 0, 52)
set_guard(2917, 11022, 0, 2)
fall_sleep(11022, 0, 20)
wakes_up(11022, 0, 54)
set_guard(1907, 11023, 0, 0)
fall_sleep(11023, 0, 9)
wakes_up(11023, 0, 39)
fall_sleep(11023, 0, 52)
wakes_up(11023, 0, 59)
set_guard(773, 11023, 23, 46)
fall_sleep(11024, 0, 1)
wakes_up(11024, 0, 2)
fall_sleep(11024, 0, 52)
wakes_up(11024, 0, 57)
set_guard(769, 11025, 0, 3)
fall_sleep(11025, 0, 13)
wakes_up(11025, 0, 28)
set_guard(2711, 11025, 23, 54)
fall_sleep(11026, 0, 3)
wakes_up(11026, 0, 45)
fall_sleep(11026, 0, 49)
wakes_up(11026, 0, 59)
set_guard(2749, 11026, 23, 59)
fall_sleep(11027, 0, 18)
wakes_up(11027, 0, 23)
fall_sleep(11027, 0, 28)
wakes_up(11027, 0, 46)
fall_sleep(11027, 0, 49)
wakes_up(11027, 0, 54)
set_guard(1187, 11028, 0, 4)
fall_sleep(11028, 0, 40)
wakes_up(11028, 0, 50)
set_guard(1187, 11029, 0, 0)
fall_sleep(11029, 0, 27)
wakes_up(11029, 0, 44)
fall_sleep(11029, 0, 51)
wakes_up(11029, 0, 55)
set_guard(191, 11029, 23, 52)
fall_sleep(11030, 0, 1)
wakes_up(11030, 0, 33)
set_guard(2711, 11030, 23, 53)
fall_sleep(11031, 0, 0)
wakes_up(11031, 0, 12)
fall_sleep(11031, 0, 50)
wakes_up(11031, 0, 52)
set_guard(683, 11101, 0, 2)
fall_sleep(11101, 0, 22)
wakes_up(11101, 0, 26)
fall_sleep(11101, 0, 34)
wakes_up(11101, 0, 43)
set_guard(683, 11102, 0, 0)
fall_sleep(11102, 0, 16)
wakes_up(11102, 0, 35)
fall_sleep(11102, 0, 45)
wakes_up(11102, 0, 47)
set_guard(2917, 11102, 23, 56)
fall_sleep(11103, 0, 11)
wakes_up(11103, 0, 43)
set_guard(683, 11104, 0, 2)
fall_sleep(11104, 0, 13)
wakes_up(11104, 0, 23)
fall_sleep(11104, 0, 27)
wakes_up(11104, 0, 59)
set_guard(2711, 11105, 0, 0)
fall_sleep(11105, 0, 45)
wakes_up(11105, 0, 48)
fall_sleep(11105, 0, 51)
wakes_up(11105, 0, 52)
set_guard(2879, 11105, 23, 56)
fall_sleep(11106, 0, 16)
wakes_up(11106, 0, 22)
fall_sleep(11106, 0, 46)
wakes_up(11106, 0, 55)
set_guard(1721, 11107, 0, 1)
fall_sleep(11107, 0, 23)
wakes_up(11107, 0, 56)
set_guard(1907, 11107, 23, 56)
fall_sleep(11108, 0, 7)
wakes_up(11108, 0, 22)
fall_sleep(11108, 0, 39)
wakes_up(11108, 0, 54)
set_guard(2917, 11109, 0, 4)
fall_sleep(11109, 0, 39)
wakes_up(11109, 0, 41)
fall_sleep(11109, 0, 48)
wakes_up(11109, 0, 52)
set_guard(2141, 11109, 23, 56)
fall_sleep(11110, 0, 22)
wakes_up(11110, 0, 55)
set_guard(1381, 11110, 23, 58)
set_guard(2917, 11112, 0, 0)
fall_sleep(11112, 0, 21)
wakes_up(11112, 0, 41)
set_guard(2879, 11112, 23, 57)
fall_sleep(11113, 0, 47)
wakes_up(11113, 0, 52)
fall_sleep(11113, 0, 55)
wakes_up(11113, 0, 56)
set_guard(1493, 11114, 0, 2)
fall_sleep(11114, 0, 11)
wakes_up(11114, 0, 33)
fall_sleep(11114, 0, 42)
wakes_up(11114, 0, 59)
set_guard(2777, 11115, 0, 3)
fall_sleep(11115, 0, 11)
wakes_up(11115, 0, 24)
fall_sleep(11115, 0, 51)
wakes_up(11115, 0, 52)
fall_sleep(11115, 0, 55)
wakes_up(11115, 0, 56)
set_guard(2879, 11116, 0, 0)
fall_sleep(11116, 0, 11)
wakes_up(11116, 0, 53)
set_guard(1493, 11116, 23, 50)
fall_sleep(11117, 0, 1)
wakes_up(11117, 0, 23)
set_guard(1049, 11118, 0, 2)
fall_sleep(11118, 0, 24)
wakes_up(11118, 0, 38)
fall_sleep(11118, 0, 50)
wakes_up(11118, 0, 51)
set_guard(2879, 11118, 23, 57)
fall_sleep(11119, 0, 42)
wakes_up(11119, 0, 57)
set_guard(1213, 11120, 0, 1)
fall_sleep(11120, 0, 38)
wakes_up(11120, 0, 44)
set_guard(2113, 11120, 23, 56)
set_guard(2141, 11121, 23, 57)
fall_sleep(11122, 0, 42)
wakes_up(11122, 0, 53)
set_guard(769, 11123, 0, 2)
fall_sleep(11123, 0, 16)
wakes_up(11123, 0, 49)


score_by_minute = {}
for m in range(0, 60):
    best_candidate = 0
    best_score = 0
    for guard_id, guard_data in guard_status.items():
        guard_score = 0
        for d, minutes in guard_data.items():
            if m in minutes:
                guard_score += 1
        if guard_score > best_score:
            best_score = guard_score
            best_candidate = guard_id
    score_by_minute[m] = (best_score, best_candidate)

best_candidate = 0
score = 0
for m, best in score_by_minute.items():
    if best[0] > score:
        minute = m
        score = best[0]
        best_candidate = best[1]
        print("new score : %s %s %s" % (minute, best_candidate, score))

print("best : %s %s %s %s" % (minute, best_candidate, score, best_candidate * minute))
