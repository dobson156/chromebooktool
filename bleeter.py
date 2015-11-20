import datetime
import re


def get_time():
	#return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	return datetime.datetime.now().strftime("%H:%M %d-%m-%y")

bat_dir="/sys/class/power_supply/sbs-104-000b/"
bat_now_path=bat_dir+"charge_now"
bat_max_path=bat_dir+"charge_full"
bat_sta_path=bat_dir+"status"

def get_battery():
	with open(bat_max_path) as f:
		bat_max=int(f.read())
	with open(bat_now_path) as f:
		bat_now=int(f.read())
	with open(bat_sta_path) as f:
		stat='^' if f.read(1).lower() == 'c' else 'v'
	return str(int( bat_now * 100 / bat_max ))+stat

meminfo_path="/proc/meminfo"

def get_mem_usage():
	with open(meminfo_path) as f:
		data = f.read()
		mem_tot=int(re.search("MemTotal:\s+([0-9]*)", data).group(1))
		mem_fre=int(re.search("MemFree:\s+([0-9]*)", data).group(1))
	return 100-int(mem_fre*100/mem_tot)


def get_cpu():
	pass

print("bat:{} mem:{}% {}".format(
	get_battery(),
	get_mem_usage(),
	get_time()))
