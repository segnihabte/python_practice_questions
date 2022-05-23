from scipy import signal
import matplotlib as plt
t = np.linspace(0, 5, 100)
x = np.sin(t)
x_resampled = signal.resample(x, 25)
plt.plot(t, x) 
plt.plot(t[::4], x_resampled, 'ko') 
print("we are doing good oh")
# comment test

def hash_fun(num):
	print("fuck hash functions")
