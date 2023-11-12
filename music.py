from scamp import *
from utils import pi_digits
from scamp_extensions.pitch import Scale

# session = Session()

# piano1 = session.new_part("Piano")
# piano2 = session.new_part("Piano")

# pitches = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]


# def piano_part(which_piano):
#     while True:
#         for pitch in pitches:
#             which_piano.play_note(pitch, 1.0, 0.25)

# clock1 = session.fork(piano_part, args=(piano1,), initial_tempo=100)
# clock2 = session.fork(piano_part, args=(piano2,), initial_tempo=98)

# session.start_transcribing(clock=clock1)
# session.wait(30)

# performance = session.stop_transcribing()
# performance.to_score(QuantizationScheme.from_time_signature("3/4", 16)).show_xml()

# extract every digit from pie and print it, first 100 digits
digits = [n for n in list(pi_digits(10))]
# print first 10 digits one by one
for d in digits:
    print(d)    

#%% PERFORMANCE STARTS

session = Session()

my_piano = session.new_part("Piano")
my_scale = Scale.major(60)  # 0 = Do, 1 = Re, 3 = Mi, ... -1 = Si, -2 = La, ...

for digit in digits:
    if digit <= 7:
        my_piano.play_note(my_scale[digit], 1., .5)


