import time
 
def read_temp_raw():
    f = open("/sys/bus/w1/devices/28-3cfaf648f0b3/w1_slave", "r")
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    # Last 3 characters in first line 'YES' indicates everything is working as expected.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    # Read temperature from second line .
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
 
 
# Test
print(' C=%3.3f  F=%3.3f'% read_temp())
