import numpy as np
#frequency of notes for the "correct" chime
freqs_cor = [349, 294, 392]

#beats for each note in "correct" chime
beats_cor = [.5, .25, 1]

#song beats per minute
bpm = 168

#convert the times into seconds
times_cor = [ibeat/bpm * 60 for ibeat in beats_cor]

#create the np array
final_cor = np.array([freqs_cor, times_cor], dtype = 'float')

#transpose the array
final_cor = final_cor.transpose()

#save data to file
np.save('correctSong.npy', final_cor)

#frequency of notes for the "incorrect" chime
freqs_inc = [349, 294, 277, 262]

#beats for each note in "incorrect" chime
beats_inc = [.5, .5, .5, .5]

#song beats per minute
bpm = 168

#convert the times into seconds
times_inc = [ibeat/bpm * 60 for ibeat in beats_inc]

#create the np array
final_inc = np.array([freqs_inc, times_inc], dtype = 'float')

#transpose the array
final_inc = final_inc.transpose()

#save data to file
np.save('wrongSong.npy', final_inc)
