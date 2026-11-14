% The style-study scene, shared by a_distant, b_silhouette and c_flat:
% the night the magistrate follows the thread to the rock behind the town.
% Before running it, define /moonx /moony /moonr.
/cb-st-ko (원님은 붉은 명주실을 손에 감고 캄캄한 뒷산을 올랐습니다. 바람이 불고 부엉이가 울었습니다. 실은 바위 앞에서 끊긴 듯 바위틈으로 사라졌습니다.) def
/cb-st-en (The magistrate wound the red silk thread round his hand and climbed the dark mountain behind the town. The wind blew. An owl called. At a great rock the thread vanished into a crack.) def

/cb-st-back {
  cb-gp-px0 cb-gp-py0 cb-gp-px1 cb-gp-py1 cb-gp-nightsky
  moonx moony moonr cb-gp-moon
  % far crags
  110 300 210 190 [0.42 0.52 0.72] [0.26 0.32 0.56] 5 cb-mh-crag
  300 300 170 150 [0.42 0.52 0.72] [0.26 0.32 0.56] 4 cb-mh-crag
  % a sangseo-un drifting across the far crags, clear of the moon
  360 405 150 cb-mh-cloud
  % near crags
  160 222 160 130 [0.44 0.64 0.62] [0.22 0.40 0.46] 3 cb-mh-crag
  % pines on the near ridge
  110 250 64 8 cb-mh-pine
  250 235 50 -6 cb-mh-pine
  % the big crag with the crack
  490 150 190 330 [0.62 0.56 0.66] [0.38 0.32 0.46] 3 cb-mh-crag
  492 224 92 cb-gp-crack
  % the hillside path, rising to the right
  newpath cb-gp-px0 132 moveto cb-gp-px0 200 lineto 140 214 260 196 cb-gp-px1 236 curveto cb-gp-px1 132 lineto closepath
  [0.40 0.48 0.40] 0.9 cb-bigwash
  newpath cb-gp-px0 200 moveto 140 214 260 196 cb-gp-px1 236 curveto 1.2 cb-line
  % grass strokes on the hill
  0 1 30 { /k exch def
    /gx cb-gp-px0 k 18 mul add def /gy 150 rand 40 mod add def
    newpath gx gy moveto gx 3 add gy 9 add lineto 0.7 cb-line } for
  % the town's sunflowers by the gate, closed for the night
  60 132 70 6 -8 cb-mh-sunflowerplant
  90 132 52 -6 4 cb-mh-sunflowerplant
}
def

% (a night glaze over the finished scene greyed the moon; the night colours
% carry the dark by themselves)
/cb-st-night { } def
