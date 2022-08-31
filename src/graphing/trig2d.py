import math
import matplotlib.pyplot as plt

# displays in radians unless this is set to True
IS_DEGREES = True

plt.rcParams['figure.dpi'] = 300

resolution = 500

if IS_DEGREES:
    scale = 360 / (2 * math.pi)
else:
    scale = 1

x = [i * 2 * math.pi * scale / resolution for i in range(0, resolution + 1)]
y1 = [math.sin(i / scale) for i in x]
y2 = [math.cos(i / scale) for i in x]
y3 = [math.tan(i / scale) for i in x]

y3 = [i if i >= -1 and i <= 1 else None for i in y3]

ax = plt.axes()
ax.grid(True)
ax.yaxis.set_major_locator(plt.MaxNLocator(21))
ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
plt.ylim(-1, 1)
if IS_DEGREES:
    plt.xlim(0, 360)
else:
    plt.xlim(0, 2 * math.pi)
plt.axhline('0', color='black')
plt.plot(x, y1, label="y = sin(x)")
plt.plot(x, y2, label="y = cos(x)")
plt.plot(x, y3, label="y = tan(x)")
if IS_DEGREES:
    plt.xlabel('x (degrees)')
else:
    plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend()
plt.title("Trig Functions")
plt.show()
