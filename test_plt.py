import matplotlib.pyplot as plt
import collections

fig, ax = plt.subplots()
window_size = 50
data_buffer = collections.deque(maxlen=window_size)

bars = ax.bar(range(window_size), [0]*window_size, animated=True)
ax.set_ylim(0, 100)

def update(frame):
    # Simulate incoming data point
    new_value = np.random.randn() * 20 + 50
    data_buffer.append(new_value)
    
    # Update visible bars
    for i, (bar, val) in enumerate(zip(bars, data_buffer)):
        bar.set_height(val)
        bar.set_color(plt.cm.RdYlGn(val / 100))  # Color by value
    
    return bars

ani = FuncAnimation(fig, update, interval=50, blit=True)
plt.show()
