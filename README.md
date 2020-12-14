# PHY180 Pendulum Lab
 
Pendulum labs for UofT EngSci PHY180. See the [Pendulum Lab Handout](./PendulumLabs.pdf) for assignment details.

Video files are in FLV format for Tracker compatibility. Videos are shot in 1080p60fps to balance high pixel-position accuracy and low frame count/file size.

# Development

## Method

 1. Set up pendulum and camera (see the [Final Report](./report/pendulum.pdf)).
 2. Record

## Dependencies

 - [VLC](https://www.videolan.org/vlc/)
 - [Tracker Video Analysis and Modeling Tool](https://physlets.org/tracker/)
 - [Python 3](https://www.python.org/) and its dependencies (see [requirements](./requirements.txt))
   - [SciPy](https://www.scipy.org/)
   - [MatPlotLib](https://matplotlib.org/3.3.3/index.html)
 - Excel or Google Sheets
 - LaTeX

## Video File Descriptions

The purposes of the [video analysis source files](./src/):

 1. `pendulum_fullPeriod` - Pendulum released at 90°, allowed to decay to <15°; **NOT INCLUDED IN REPO, FIND [HERE](https://drive.google.com/file/d/1M0BHg32SPd2ZmKkyaPqAKxjmWZvkTjqi/view?usp=sharing)**
 2. `pendulum_string{`N`}` - Pendulum released at a reasonable angle with varying lengths (44.75", 39", 34.25", 29", 25.25"), allowed to oscillate for ~4 periods;
 3. `pendulum_mass{`N`}` - Pendulum released at a reasonable angle with varying bob mass (2032g, 1784g, 1607g, 1366g, 1012g), allowed to oscillate for ~4 periods at string length 3. **Note:** `pendulum_mass1` is replaced by `pendulum_string3`.