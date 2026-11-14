% The style-study scene, shared by a_distant, b_silhouette and c_flat:
% the night the magistrate follows the thread to the rock behind the town.
% Before running it, define /moonx /moony /moonr.
/cb-st-ko (원님은 붉은 실을 따라 캄캄한 뒷산을 올랐습니다. 실은 바위틈으로 사라졌습니다.) def
/cb-st-en (The magistrate followed the red thread up the dark mountain behind the town. It vanished into a crack in the rock.) def

/cb-st-back {
  cb-gp-px0 cb-gp-py0 cb-gp-px1 cb-gp-py1 cb-gp-nightsky
  % far peaks
  60 290 90 190 [0.16 0.26 0.46] cb-mh-peak
  150 300 70 130 [0.18 0.30 0.50] cb-mh-peak
  250 290 80 165 [0.16 0.26 0.46] cb-mh-peak
  355 290 95 195 [0.18 0.30 0.50] cb-mh-peak
  moonx moony moonr cb-gp-moon
  moonx moonr 1.6 mul add moony moonr 0.5 mul sub 110 cb-mh-cloud
  % mid peaks
  110 210 110 160 [0.18 0.38 0.44] cb-mh-peak
  200 215 80 110 [0.20 0.40 0.40] cb-mh-peak
  300 205 100 140 [0.20 0.40 0.40] cb-mh-peak
  % pines on the ridge
  215 268 60 8 cb-mh-pine
  330 262 48 -6 cb-mh-pine
  % the near crag, with the crack
  505 132 170 340 [0.40 0.36 0.44] cb-mh-peak
  492 226 92 cb-gp-crack
  % the hill path, in front
  newpath cb-gp-px0 132 moveto cb-gp-px0 190 lineto 150 200 260 175 400 190 curveto 400 132 lineto closepath
  [0.22 0.30 0.30] 0.9 cb-bigwash
  % the town's sunflowers by the gate, closed for the night
  60 132 70 6 -8 cb-mh-sunflowerplant
  90 132 52 -6 4 cb-mh-sunflowerplant
}
def

% (a night glaze over the finished scene greyed the moon; the night colours
% carry the dark by themselves)
/cb-st-night { } def
