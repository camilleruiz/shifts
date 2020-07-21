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

def get_max_shift(shifts):
	current_max_shift = [-1, -1000000000000000000];

	for shift in shifts:
		if shift[1] >= current_max_shift[1]:
			current_max_shift = shift;

	return current_max_shift;


def get_min_shift(shifts):
	current_min_shift = [-1, 1000000000000000000];

	for shift in shifts:
		if shift[1] <= current_min_shift[1]:
			current_min_shift = shift;

	return current_min_shift;

def get_shifts(values, point_threshold = 0, value_threshold = 0, limit = 0):

	direction = 2;

	i = 1;
	while direction == 2:
		current_sign = check_sign(values[i], values[i+1]);
		if current_sign != 0:
			direction = current_sign;
			break;
		i+=1;

	sign = 2;
	shift_array = [];
	temp_shifts = [];


	for i in range(0, len(values)-1):
		current_sign = check_sign(values[i], values[i+1]);
		current_value = values[i];

		if sign == 2:
			sign = current_sign;
			continue;



		append_later = [];

		if sign != current_sign and current_value > limit:
			
			curr_shift = [i, current_value];

			if len(temp_shifts) == 0:
				temp_shifts.append(curr_shift);

			else:
				point_distance = abs(i - temp_shifts[-1][0]);
				value_distance = abs(current_value - temp_shifts[-1][1]);
				if point_distance < point_threshold or value_distance < value_threshold:
					temp_shifts.append(curr_shift);
				else:
					append_later.append(curr_shift)

		point_distance = 0;
		value_distance = 0;
		if len(temp_shifts) != 0:
			point_distance = abs(i - temp_shifts[-1][0]);
			value_distance = abs(current_value - temp_shifts[-1][1]);

		if point_distance >= point_threshold and value_distance >= value_threshold and current_sign != 0 and len(temp_shifts) != 0:
			if (direction == current_sign and len(shift_array) == 0) or len(temp_shifts) == 1:
				shift_array.append(temp_shifts[0]);
			
			if direction != current_sign:
				if direction == 1:
					shift_array.append(get_max_shift(temp_shifts));
				else:
					shift_array.append(get_min_shift(temp_shifts));

			direction = current_sign;
			temp_shifts = [];

		if len(append_later) > 0:
			shift_array.append(append_later[0]);
			append_later = [];
		sign = current_sign;
	if len(temp_shifts) > 0:
		shift_array.append(temp_shifts[-1])

	return shift_array;


