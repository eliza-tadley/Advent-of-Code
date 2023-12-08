from collections import defaultdict
import math
from tqdm import tqdm


def parse_data(data):
    # want: list of seeds, seed-to-soil map lists, soil-to-fertilizer map lists, fertilizer-to-water map lists
    # water-to-light map lists, light-to-temperature map lists, temperature-to-humidity map lists, humidity-to-location map lists
    seed_to_soil_map = False
    seed_to_soil = []
    soil_to_fertilizer_map = False
    soil_to_fertilizer = []
    fertilizer_to_water_map = False
    fertilizer_to_water = []
    water_to_light_map = False
    water_to_light = []
    light_to_temperature_map = False
    light_to_temperature = []
    temp_to_humidity_map = False
    temp_to_humifity = []
    humidity_to_location_map = False
    humidity_to_location = []
    for line in data:
        if line == '':
            continue
        if line.startswith('seeds'):
            seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]
        elif line.startswith('seed-to-soil'):
            seed_to_soil_map = True
            soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temp_to_humidity_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('soil-to-fertilizer'):
            soil_to_fertilizer_map = True
            seed_to_soil_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temp_to_humidity_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('fertilizer-to-water'):
            fertilizer_to_water_map = True
            seed_to_soil_map, soil_to_fertilizer_map, water_to_light_map, light_to_temperature_map, temp_to_humidity_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('water-to-light'):
            water_to_light_map = True
            seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, light_to_temperature_map, temp_to_humidity_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('light-to-temperature'):
            light_to_temperature_map = True
            seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, temp_to_humidity_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('temperature-to-humidity'):
            temp_to_humidity_map = True
            seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, humidity_to_location_map = False, False, False, False, False, False
        elif line.startswith('humidity-to-location'):
            humidity_to_location_map = True
            seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temp_to_humidity_map = False, False, False, False, False, False
        else:
            if seed_to_soil_map:
                seed_to_soil.append([int(x) for x in line.split(' ')])
            if soil_to_fertilizer_map:
                soil_to_fertilizer.append([int(x) for x in line.split(' ')])
            if fertilizer_to_water_map:
                fertilizer_to_water.append([int(x) for x in line.split(' ')])
            if water_to_light_map:
                water_to_light.append([int(x) for x in line.split(' ')])
            if light_to_temperature_map:
                light_to_temperature.append([int(x) for x in line.split(' ')])
            if temp_to_humidity_map:
                temp_to_humifity.append([int(x) for x in line.split(' ')])
            if humidity_to_location_map:
                humidity_to_location.append([int(x) for x in line.split(' ')])
    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humifity, humidity_to_location


def find_value_from_map(map, original_value):
    for m in map:
        destination_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if source_range_start <= original_value < (source_range_start + range_length):
            new_value = destination_range_start + (original_value - source_range_start)
            return new_value
    return original_value


# Part 1
def p1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humidity, humidity_to_location):
    min_location = math.inf
    for seed in seeds:
        soil = find_value_from_map(seed_to_soil, seed)
        fertilizer = find_value_from_map(soil_to_fertilizer, soil)
        water = find_value_from_map(fertilizer_to_water, fertilizer)
        light = find_value_from_map(water_to_light, water)
        temp = find_value_from_map(light_to_temperature, light)
        humidity = find_value_from_map(temp_to_humidity, temp)
        location = find_value_from_map(humidity_to_location, humidity)
        if location < min_location:
            min_location = location
    return min_location


# Part 2
def p2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humidity, humidity_to_location):
    seed_ranges = []
    for i in range(len(seeds)):
        if i%2 == 0:
            seed_ranges.append((seeds[i], seeds[i+1]))

    min_location = math.inf
    for seed_range in seed_ranges:
        for i in tqdm(range(seed_range[1])):
            seed = seed_range[0] + i
            soil = find_value_from_map(seed_to_soil, seed)
            fertilizer = find_value_from_map(soil_to_fertilizer, soil)
            water = find_value_from_map(fertilizer_to_water, fertilizer)
            light = find_value_from_map(water_to_light, water)
            temp = find_value_from_map(light_to_temperature, light)
            humidity = find_value_from_map(temp_to_humidity, temp)
            location = find_value_from_map(humidity_to_location, humidity)
            if location < min_location:
                min_location = location
    return min_location


def main():
    with open('./input.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humidity, humidity_to_location = parse_data(data)

    print("Part 1 Answer: {}".format(p1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humidity, humidity_to_location)))
    print("Part 2 Answer: {}".format(p2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temp_to_humidity, humidity_to_location)))


if __name__ == "__main__":
    main()
