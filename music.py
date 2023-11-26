from scamp import *
from utils import pi_digits, find_closest_next_note
from scamp_extensions.pitch import Scale

# session = Session()

# piano1 = session.new_part("Piano")
# piano2 = session.new_part("Piano")

# pitches = [64, 66, 71, 73, 74, 66, 64, 73, 71, 66, 74, 73]

# -----play music-------------------------------------------------------------------
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


# -----digits stuff-------------------------------------------------------------------
# # extract every digit from pie and print it, first 100 digits
# digits = [n for n in list(pi_digits(10))]
# # print first 10 digits one by one
# for d in digits:
#     print(d)    

#%% PERFORMANCE STARTS

session = Session()

my_piano = session.new_part("Piano")

start_pitch = 60
my_scale = Scale.major(60)  # 0 = Do, 1 = Re, 3 = Mi, ... -1 = Si, -2 = La, ...
print(my_scale)

# create an array of size 10 with 0-9
# digits = [Scale.major(start_pitch+i*4) for i in range(10)]

# create map that takes digit and returns [my_scale[digit]+i*12 for i in range(-5,5)] for each digit as value in map
digit_map = {digit : [my_scale[digit]+(i)*12-2 for i in range(-5,5)] for digit in range(1,10)}

print(digit_map)
    


# cur_note,last_note = -1,-1
# for digit in digits:
#     # 0, need last note
#     if digit == 0:
#         my_piano.play_note_off(last_note, 1., .5) # Stop playing the last note if it exists
#     # 1-7
#     elif digit <= 7:
#         cur_note = my_scale[digit] # Set current note to the corresponding scale note
#         my_piano.play_note_on(cur_note, 1., .5) # Play the current note
#     elif digit == 8:
#         my_piano.play_note_off(cur_note, 1., .5)
#     elif digit == 9:
#         pass


#     # if last_note != -1:
#     #     my_piano.play_note_off(last_note, 1., .5) # Stop playing the last note if it exists
#     last_note = cur_note # Update the last note to the current note



