__author__ = 'jeroendevries'
import statistics
def print_statistics(passengers_list):
    hoogste = max(passengers_list)
    laagste=min(passengers_list)
    gemiddelde = sum(passengers_list)/len(passengers_list)
    mediaan = statistics.median(passengers_list)
    print(laagste,hoogste,gemiddelde,mediaan)

