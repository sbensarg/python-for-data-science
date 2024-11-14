from datetime import datetime
import time

# current date and time
now = datetime.now()
time = time.time()

print(f"Seconds since January 1, 1970: {time:.4f} or {time:.2e} in scientific notation" )

s1 = now.strftime("%b %d %Y")
print(s1)