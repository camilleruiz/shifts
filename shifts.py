import pandas as pd;
import numpy as np;


def check_sign(a, b):
	temp = b-a;
	
	if abs(temp) < 1:
		return 0;

	if temp > 0:
		return 1;
	elif temp < 0:
		return -1;
	return 0;
	
def get_shifts(values, point_threshold, value_threshold = 0, limit=0):
	sign = 2;
	shift_array = [];

	direction = 2;

	i = 1;
	while direction == 2:
		current_sign = check_sign(values[i], values[i+1]);
		if current_sign != 0:
			direction = current_sign;
			break;
		i+=1;

	for i in range(0, len(values)-1):
		current_sign = check_sign(values[i], values[i+1]);
		current_value = values[i];

		if sign == 2:
			sign = current_sign;
			continue;

		if sign != current_sign and current_value > limit:

			if len(shift_array) == 0:
				shift_array.append([i, current_value]);
				if current_sign != 0:
					direction = current_sign;
			else:

				prev_shift_index = shift_array[-1][0]; 
				distance = abs(i - prev_shift_index);

				if distance < point_threshold:
					shift_array.pop();
					if direction != current_sign:
						shift_array.append([i, current_value]);
						if current_sign != 0:
							direction = current_sign;
				else:
					shift_array.append([i, current_value]);
					if current_sign != 0:
						direction = current_sign;

		sign = current_sign;

	return shift_array;


