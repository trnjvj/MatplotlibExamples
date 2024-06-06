import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(2, 1, 1) # two rows, one column, first plot



fig2 = plt.figure()
ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])



import numpy as np
t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax.plot(t, s, color='blue', lw=2)



ax.lines[0]
Out[101]: <matplotlib.lines.Line2D at 0x19a95710>

line
Out[102]: <matplotlib.lines.Line2D at 0x19a95710>



line = ax.lines[0]
line.remove()



xtext = ax.set_xlabel('my xdata')  # returns a Text instance
ytext = ax.set_ylabel('my ydata')



import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.subplots_adjust(top=0.8)
ax1 = fig.add_subplot(211)
ax1.set_ylabel('Voltage [V]')
ax1.set_title('A sine wave')

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2*np.pi*t)
line, = ax1.plot(t, s, color='blue', lw=2)

# Fixing random state for reproducibility
np.random.seed(19680801)

ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
n, bins, patches = ax2.hist(np.random.randn(1000), 50,
                            facecolor='yellow', edgecolor='yellow')
ax2.set_xlabel('Time [s]')

plt.show()






a = o.get_alpha()
o.set_alpha(0.5*a)




o.set(alpha=0.5, zorder=2)





matplotlib.artist.getp(fig.patch)
  agg_filter = None
  alpha = None
  animated = False
  antialiased or aa = False
  bbox = Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0)
  capstyle = butt
  children = []
  clip_box = None
  clip_on = True
  clip_path = None
  contains = None
  data_transform = BboxTransformTo(     TransformedBbox(         Bbox...
  edgecolor or ec = (1.0, 1.0, 1.0, 1.0)
  extents = Bbox(x0=0.0, y0=0.0, x1=640.0, y1=480.0)
  facecolor or fc = (1.0, 1.0, 1.0, 1.0)
  figure = Figure(640x480)
  fill = True
  gid = None
  hatch = None
  height = 1
  in_layout = False
  joinstyle = miter
  label =
  linestyle or ls = solid
  linewidth or lw = 0.0
  patch_transform = CompositeGenericTransform(     BboxTransformTo(   ...
  path = Path(array([[0., 0.],        [1., 0.],        [1.,...
  path_effects = []
  picker = None
  rasterized = None
  sketch_params = None
  snap = None
  transform = CompositeGenericTransform(     CompositeGenericTra...
  transformed_clip_path_and_affine = (None, None)
  url = None
  verts = [[  0.   0.]  [640.   0.]  [640. 480.]  [  0. 480....
  visible = True
  width = 1
  window_extent = Bbox(x0=0.0, y0=0.0, x1=640.0, y1=480.0)
  x = 0
  xy = (0, 0)
  y = 0
  zorder = 1
  
  
  
  
  
  fig = plt.figure()

ax1 = fig.add_subplot(211)

ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

ax1
Out[159]: <Axes:>

print(fig.axes)
[<Axes:>, <matplotlib.axes._axes.Axes object at 0x7f0768702be0>]




for ax in fig.axes:
    ax.grid(True)
    
    
    
    
    import matplotlib.lines as lines

fig = plt.figure()

l1 = lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
l2 = lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)
fig.lines.extend([l1, l2])

plt.show()






ax = fig.add_subplot()
rect = ax.patch  # a Rectangle instance
rect.set_facecolor('green')





x, y = np.random.rand(2, 100)

line, = ax.plot(x, y, '-', color='blue', linewidth=2)




print(ax.lines)
[<matplotlib.lines.Line2D at 0xd378b0c>]





n, bins, rectangles = ax.hist(np.random.randn(1000), 50)

rectangles
Out[234]: <BarContainer object of 50 artists>

print(len(ax.patches))
Out[235]: 50







fig, ax = plt.subplots()

# create a rectangle instance

rect = matplotlib.patches.Rectangle((1, 1), width=5, height=12)

# by default the Axes instance is None

print(rect.axes)
None

# and the transformation instance is set to the "identity transform"

print(rect.get_data_transform())
IdentityTransform()

# now we add the Rectangle to the Axes

ax.add_patch(rect)

# and notice that the ax.add_patch method has set the Axes
# instance

print(rect.axes)
Axes(0.125,0.1;0.775x0.8)

# and the transformation has been set too

print(rect.get_data_transform())
CompositeGenericTransform(
    TransformWrapper(
        BlendedAffine2D(
            IdentityTransform(),
            IdentityTransform())),
    CompositeGenericTransform(
        BboxTransformFrom(
            TransformedBbox(
                Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0),
                TransformWrapper(
                    BlendedAffine2D(
                        IdentityTransform(),
                        IdentityTransform())))),
        BboxTransformTo(
            TransformedBbox(
                Bbox(x0=0.125, y0=0.10999999999999999, x1=0.9, y1=0.88),
                BboxTransformTo(
                    TransformedBbox(
                        Bbox(x0=0.0, y0=0.0, x1=6.4, y1=4.8),
                        Affine2D(
                            [[100.   0.   0.]
                             [  0. 100.   0.]
                             [  0.   0.   1.]])))))))

# the default Axes transformation is ax.transData

print(ax.transData)
CompositeGenericTransform(
    TransformWrapper(
        BlendedAffine2D(
            IdentityTransform(),
            IdentityTransform())),
    CompositeGenericTransform(
        BboxTransformFrom(
            TransformedBbox(
                Bbox(x0=0.0, y0=0.0, x1=1.0, y1=1.0),
                TransformWrapper(
                    BlendedAffine2D(
                        IdentityTransform(),
                        IdentityTransform())))),
        BboxTransformTo(
            TransformedBbox(
                Bbox(x0=0.125, y0=0.10999999999999999, x1=0.9, y1=0.88),
                BboxTransformTo(
                    TransformedBbox(
                        Bbox(x0=0.0, y0=0.0, x1=6.4, y1=4.8),
                        Affine2D(
                            [[100.   0.   0.]
                             [  0. 100.   0.]
                             [  0.   0.   1.]])))))))

# notice that the xlimits of the Axes have not been changed

print(ax.get_xlim())
(0.0, 1.0)

# but the data limits have been updated to encompass the rectangle

print(ax.dataLim.bounds)
(1.0, 1.0, 5.0, 12.0)

# we can manually invoke the auto-scaling machinery

ax.autoscale_view()

# and now the xlim are updated to encompass the rectangle, plus margins

print(ax.get_xlim())
(0.75, 6.25)

# we have to manually force a figure draw

fig.canvas.draw()






ax.tick_params(axis='x', labelcolor='orange')





fig, ax = plt.subplots()
axis = ax.xaxis
axis.get_ticklocs()





array([0. , 0.2, 0.4, 0.6, 0.8, 1. ])

axis.get_ticklabels()

[Text(0.0, 0, '0.0'), Text(0.2, 0, '0.2'), Text(0.4, 0, '0.4'), Text(0.60
                                                                     
                                                                     
                                                                     
                                                                     axis.get_ticklines()

<a list of 12 Line2D ticklines objects>






axis.get_ticklabels(minor=True)
axis.get_ticklines(minor=True)

<a list of 0 Line2D ticklines objects>





# plt.figure creates a matplotlib.figure.Figure instance
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')

ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')


for label in ax1.xaxis.get_ticklabels():
    # label is a Text instance
    label.set_color('red')
    label.set_rotation(45)
    label.set_fontsize(16)

for line in ax1.yaxis.get_ticklines():
    # line is a Line2D instance
    line.set_color('green')
    line.set_markersize(25)
    line.set_markeredgewidth(3)

plt.show()








import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))

# Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')

ax.yaxis.set_tick_params(which='major', labelcolor='green',
                         labelleft=False, labelright=True)

plt.show()





