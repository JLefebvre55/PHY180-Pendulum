# Pendulum Lab Outline

## Intro

The purpose of this lab is to investigate the factors that contribute to a pendulum's period. This lab report will focus on initial amplitude, string length, and bob mass, and will also investigate Q factor.

## Background

Pendulums operate on the principle of simple harmonic motion.

## Method

### Materials

DO NOT INCLUDE

- PETG paracord (ref), ~10 feet or other light, strong, knottable string
- Crosman Copperhead Copper BB Pellets, 6000-count (ref) or other bob with removable mass-material and secure mounting point
- Kitchen scale (brand? ref) or other mass measurement device
- Tupperware or other sturdy container, can hold the pendulum's mass-material volume
- Fixed mounting location with mounting screw/nail/peg
- Tarp or other solid-color sturdy backdrop
- Clamps, tape, or other tarp mounting mechanism
- Folding table or other level reference
- Standard 25ft Imperial measuring tape (ref)
- iPhone 10 or other video capture device capable of at least 10 minutes uninterrupted video capture at 1080p60fps
- Roll of painter's tape or other functional camera mount/tripod/prop-up mechanism
- Ladder or other sturdy camera stand surface that, when phone is propped on it, the camera viewport is elevated enough to capture the pendulum's full swing 
- MacBook Pro or other computer with requisite software installed (see README) and >8GB of RAM

### Setup

Apparatus setup:

1. Mounting screw installed at fixed mounting location
2. Bob set up (see below) and attached to string via self-tightening slipknot (ref, fig)
3. Bowline knots (ref) made in string at fixed distances from the bob COM (44.75", 39", 34.25", 29", 25.25")
4. Level reference placed in plane with the pendulum oscillation (Fig)
5. Tape marks at center (pendulum equilibrium) and 2 feet (??m) in either direction of the plane x-axis
6. Camera and mount set up in plane with pendulum oscillation, horizontal calibrated to table (Fig)

Pendulum setup (on a per-capture basis):

1. Cap removed from bob
2. Pour a reasonable amount (think 10%) of the pendulum's mass into sturdy container
3. Bob container placed on scale
4. Record bob mass
5. Replace cap
6. Attach bob to string
7. Loop selected bowline around fixed mounting screw

### Video Capture

3 sets of videos were taken:

 1. Full Period - Pendulum (mass 2032g, length 34.25") released at 90°, allowed to decay to <15°;
 2. String Length Trials - Pendulum (mass 2032g) released at a moderate angle (think 30°-50°) with varying string length (44.75", 39", 34.25", 29", 25.25"), allowed to oscillate for 4-6 periods;
 3. Bob Mass Trials - Pendulum (length 34.25") released at a moderate angle (think 30°-50°) with varying bob mass (2032g, 1784g, 1607g, 1366g, 1012g), allowed to oscillate for 4-6 periods;

### Tracker Analysis

 1. Prepare video for Tracker software:
    1. In VLC, select "File > Convert / Stream"
    2. Open the video capture
    3. Select "Custom" profile, customize with no audio (minimize file size) and FLV encapsulation (compatibility)
    4. Save as file with appropriate name

 2. Open video in Tracker software:
    1. In Tracker, select "File > Open File" and open the FLV video capture
    2. Wait for all frames to be loaded

 3. Tracker Calibration
    1. Select "Track > New > Calibration Tools > Calibration Stick" and follow the Tracker's instructions to calibrate the ends of the stick to the center and 2ft marking on the level reference in the video
    2. Toggle "Track > Axes > Visible" **ON**, and drag the origin of the axes to the pendulum axis

 4. Mass Tracking
    1. Select "Track > New > Point Mass"
    2. On the "Track Control" panel, select the new point mass (should be named "mass A") and select "Autotracker"
    3. Ensure the frame advance number in the bottom right of the screen is set to 5
    4. Depending on the speed of the pendulum, you will have to switch between manually tracking the pendulum frame-by-frame (shift-click) or calibrating the autotracker (set keyframe position, template region, search region, and evolution rate) and allowing it to search for you
    5. Track the pendulum across all frames

 5. Data Export
    1. In the table panel (right side, bottom panel), click the table button and ensure x, y, theta r, and v are toggled on
    2. Right click inside the table, select "Numbers > Units..." and ensure that "Angle Units" is set to radians
    3. Left click inside the table, press "CMD+A" on Mac (or "CTRL+A" on Windows) to select the entire table
    4. Press "CMD+C" on Mac (or "CTRL+C" on Windows) to copy the entire table
    5. Paste the data into Google Sheets. You can now perform analysis on the data.

## Uncertainty

### Measurement Uncertainties

- Time - 60fps, assume ±1 frame, ±0.01667s
- Position (Reference Frame) - 2ft markers on table used as reference (Fig), my standard imperial measuring tape has ±1/16in uncertainty, or 0.2% positional uncertainty. This distance is used as the reference length when analyzing the footage in Tracker. Since all positions are measured as distances, all positional data would have this uncertainty.
- Position (Motion Blur) - Speed at apex when 2030g pendulum released from ???rad (~90°) is 4.042 m/s, which produced a motion blur in the video (Fig). The circular cross-section of the bob has a circumference of 10 5/8" = 26.988cm, or an actual diameter of 8.59cm which, due to motion blur, appeared to be 10.4cm on camera, corresponding to (10.4-8.59)/2 = 0.905cm of positional uncertainty. v/v_0 * 0.905 / 100
- Mass Uncertainty - ±1g kitchen scale

The maximum of the two positional uncertainties are used per datum, per the uncertianty propagation conventions outlined in the Pendulum Lab Handout.

### Calculated Uncertainties

Measurement uncertainty propagation, per the uncertianty propagation conventions outlined in the Pendulum Lab Handout:

- Angular - the numerical difference between the maximum and minimum possible angles for generated from positional data and uncertainty. For example, consider the set S of all 4 possible arctan((y±y')/(x±x')). The uncertainty for this datum would be max{S} - min{S}.

## Results and Analysis

### Q Factor

Fitting to decaying sinusoid, bounded over ~20 oscillations, starting at ~1rad (minimize high-amplitude error)

A: 1.2752835134780802 +/- 0.04197794343541771
tau: 242.01415135578878 +/- 18.57621636803587
T: 2.1576574938901647 +/- 0.0002306306118355046
phi: 21.976476323451035 +/- 0.03227086247050787

Q1 = =πτ/T =π*242.01/2.1577 =352.364182185 ±7.675% = ±27.04

e^{-\pi/2}*A_0 = 0.295490303, occurs after 126 oscillations
Q2 = 352

Q2 well within Q1 uncertainty, confident about this number


### Period vs Amplitude

Fitting to power series, bounded across entire dataset

A: 2.047330637452943 +/- 0.014660515480016737
B: 0.005739228732634549 +/- 0.01335741474301673
C: 0.11212300430197297 +/- 0.021363589099149437

B < B', ergo experimentally zero - asymmetry test

TODO: C 'small enough' criteria???

### Period vs Length

Fitting to power law function

k: 1.1216881420592435 +/- 0.09254205262860149
L_naught: -0.18273907292996916 +/- 0.2282666263394796
n: 0.38512684608325454 +/- 0.13419629603805205

L0 < L0', ergo experimentally zero - accurately determined COM

n seems to be closer to 1/3 than 1/2, suggesting perhaps 3rd root?
k seems to not be very close to 2

When k is removed (k=1):
L_naught: 0.06940995886640021 +/- inf
n: 0.5304151670699991 +/- inf

n is much closer to 1/2, and L0 is actually smaller

### Period vs Mass

Trial 1

A: 0.5982976465159843 +/- 0.00696960369813291
tau: 147.99063636436125 +/- 37.822802956396416
T: 1.9385470241633056 +/- 0.001075641314076281
phi: 0.12093531618368836 +/- 0.011831602340159678

Trial 2

A: -0.594856929544812 +/- 0.007275437302987657
tau: 248.8360149593402 +/- 143.0474626181791
T: 1.945202773867279 +/- 0.0013500190720474804
phi: 3.119976331187423 +/- 0.012328489631952972

Trial 3

A: -0.5396958510011767 +/- 0.0028058639089933455
tau: 203.50230188669417 +/- 37.3374382397159
T: 1.9360006296469705 +/- 0.0005573213164335363
phi: 3.076292670499092 +/- 0.005366626240706735

Trial 4

A: -0.6525989087609709 +/- 0.005838489247085363
tau: 308.1924567677906 +/- 135.49275152677282
T: 1.9641071387611098 +/- 0.0009055417811753947
phi: 3.262423723665946 +/- 0.009073613260952483

Trial 5

A: -0.6233912238860799 +/- 0.005449824042286478
tau: 135.32345583763075 +/- 25.27935836869458
T: 1.9624514793417047 +/- 0.0008731539103006749
phi: 3.260151618915689 +/- 0.008857062212160849

Summary

A: 2.0050088496131817 +/- 0.0977788624826268
B: -4.574242606327281e-05 +/- 0.00013358204953325433
C: 6.109204068551541e-09 +/- 4.384699063840564e-08