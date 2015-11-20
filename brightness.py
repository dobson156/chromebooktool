backlight_dir="/sys/class/backlight/backlight.12/"
brightness_path=backlight_dir + "brightness"
max_brightness_path=backlight_dir + "max_brightness"

def get_amount():
	with open(brightness_path) as f:
		return int(f.read())

def set_amount(val):
	with open(brightness_path, 'w') as f:
		f.write(str(int(val)))

def get_max():
	with open(max_brightness_path) as f:
		return int(f.read())

def get_pcent():
	return get_amount() * 100 / get_max()

def set_pcent(pcent):
	set_amount(get_max()*pcent/100)

def up(interval=5):
	set_pcent(min(get_pcent() + interval, 100))

def down(interval=5):
	set_pcent(max(get_pcent() - interval, 0))

def main():
	import sys
	for arg in sys.argv:
		if arg == "up":	up()
		elif arg == "down": down()
		else:
			import re
			m=re.match("[0-9]+", arg)
			if not m: continue
			pcent=int(m.group())
			if pcent >= 0 and pcent <= 100:
				set_pcent(pcent)

if __name__ == "__main__":
	#set_amount(1000)
	main()
