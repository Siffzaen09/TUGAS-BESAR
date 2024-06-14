import itertools
import math
import time

# Data lokasi pengirim dan penerima sebagai koordinat (x, y) (perkiraan koordinat untuk contoh)
locations = {
    'Bandung': (6.9175, 107.6191),
    'Jakarta': (6.2088, 106.8456),
    'Garut': (7.2021, 107.8876),
    'Bogor': (6.5950, 106.8167),
    'Bekasi': (6.2383, 106.9756)
}

# Fungsi untuk menghitung jarak Euclidean antara dua titik
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Fungsi untuk menghitung total jarak dari jalur
def total_distance(route, locations):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(locations[route[i]], locations[route[i + 1]])
    distance += euclidean_distance(locations[route[-1]], locations[route[0]])  # Kembali ke awal
    return distance

# Algoritma Brute Force
def brute_force_tsp(locations):
    # Buat daftar semua kemungkinan permutasi dari lokasi
    location_names = list(locations.keys())
    permutations = list(itertools.permutations(location_names))

    # Cari jalur dengan jarak total minimum
    min_route = None
    min_distance = float('inf')
    k = 0  # Counter for iterations
    for perm in permutations:
        distance = total_distance(perm, locations)
        k += 1
        if distance < min_distance:
            min_distance = distance
            min_route = perm

    return min_route, min_distance, k

# Algoritma Greedy
def greedy_tsp(locations):
    location_names = list(locations.keys())
    start = location_names[0]
    route = [start]
    location_names.remove(start)
    k = 0  # Counter for iterations

    while location_names:
        last_location = route[-1]
        next_location = min(location_names, key=lambda x: euclidean_distance(locations[last_location], locations[x]))
        route.append(next_location)
        location_names.remove(next_location)
        k += 1

    return route, total_distance(route, locations), k

# Mengukur waktu eksekusi Brute Force
start_time = time.time()
brute_force_result, brute_force_distance, brute_force_k = brute_force_tsp(locations)
brute_force_time = time.time() - start_time

print("Brute Force Result:")
print("Route:", brute_force_result)
print("Distance:", brute_force_distance)
print("Iterations (k):", brute_force_k)
print("Time:", brute_force_time, "seconds")

# Mengukur waktu eksekusi Greedy
start_time = time.time()
greedy_result, greedy_distance, greedy_k = greedy_tsp(locations)
greedy_time = time.time() - start_time

print("\nGreedy Result:")
print("Route:", greedy_result)
print("Distance:", greedy_distance)
print("Iterations (k):", greedy_k)
print("Time:", greedy_time, "seconds")

# Evaluasi dan Perbandingan
print("\nComparison:")
print("Brute Force - Route:", brute_force_result, "Distance:", brute_force_distance, "Iterations (k):", brute_force_k, "Time:", brute_force_time, "seconds")
print("Greedy - Route:", greedy_result, "Distance:", greedy_distance, "Iterations (k):", greedy_k, "Time:", greedy_time, "seconds")