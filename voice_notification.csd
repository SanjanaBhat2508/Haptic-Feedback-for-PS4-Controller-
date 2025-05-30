<CsoundSynthesizer>

<CsOptions>
; Select the audio output device
-odac
</CsOptions>

<CsInstruments>
sr = 44100        ; Sample rate
ksmps = 128       ; Contro rate - define the number of samples per control period
nchnls = 2        ; Stereo output
0dbfs = 2         ; Full scale amplitude for auido output

instr 1
    ; MP3 Playback from the specified file
    iskptim = 0 ; Start playing the MP3 from the beginning
    ibufsize = 64 ; Set the buffer size for audio streaming 
    ar1, ar2 mp3in "/home/sanjana/Downloads/Connected to XTLite.mp3", iskptim, 0, 0, ibufsize ; Load and play the MP3 file
    outs ar1, ar2  ; Send the MP3's left and right audio signals to the speakers
endin

</CsInstruments>

<CsScore>
i1 0 5
e
</CsScore>

</CsoundSynthesizer> 
