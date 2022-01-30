def run_time():
    total_runtime = 0
    number_of_runs = 0

    while True:
        round_trip_time = input("enter roundtrip time").strip()
        if not round_trip_time:
            break
        total_runtime = total_runtime + float(round_trip_time)
        number_of_runs += 1
    print(f"Total run time {total_runtime / number_of_runs}")


run_time()
