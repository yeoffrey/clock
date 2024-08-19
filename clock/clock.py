from typing import List, Dict


def plot_historical_events(input: List[Dict[str, int]]) -> List[Dict[str, str]]:
    # Define the total number of seconds in 12 hours
    total_seconds_in_half_day = 24 * 60 * 60
    total_milliseconds_in_half_day = total_seconds_in_half_day * 1_000

    # Define the total number of years in the timeline
    total_years = 4_600_000_000  # 4.6 billion years

    def convert_to_clock_time(years_ago: int) -> str:
        # Calculate the ratio of years ago to total years
        year_ratio = years_ago / total_years

        # Calculate the corresponding milliseconds on the 12-hour clock
        milliseconds_on_clock = total_milliseconds_in_half_day * year_ratio

        # Convert milliseconds to HH:MM:SS.sss format
        seconds_total = milliseconds_on_clock // 1_000
        hours = int(seconds_total // 3600)
        minutes = int((seconds_total % 3600) // 60)
        seconds = int(seconds_total % 60)
        milliseconds = int(milliseconds_on_clock % 1_000)

        # Adjust hours to make 4.6 billion years correspond to 00:00:00
        hours = (12 - hours) % 12

        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

    def format_years_ago(years_ago: int) -> str:
        if years_ago >= 1_000_000_000:
            return f"{years_ago / 1_000_000_000:.1f} billion years ago"
        elif years_ago >= 1_000_000:
            return f"{years_ago / 1_000_000:.1f} million years ago"
        elif years_ago >= 1_000:
            return f"{years_ago / 1_000:.1f} thousand years ago"
        else:
            return f"{years_ago} years ago"

    def human_readable_time(milliseconds_on_clock: float) -> str:
        seconds_total = milliseconds_on_clock // 1_000
        milliseconds_total = int(milliseconds_on_clock % 1_000)
        hours = int(seconds_total // 3600)
        minutes = int((seconds_total % 3600) // 60)
        seconds = int(seconds_total % 60)

        time_parts = []
        if hours > 0:
            time_parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
        if minutes > 0:
            time_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
        if seconds > 0:
            time_parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")
        if milliseconds_total > 0:
            time_parts.append(
                f"{milliseconds_total} millisecond{'s' if milliseconds_total > 1 else ''}"
            )

        return (
            " and ".join(time_parts) + " ago" if len(time_parts) > 0 else "Right now!"
        )

    # Create the result list of dictionaries
    result = []
    for event in input:
        milliseconds_on_clock = total_milliseconds_in_half_day * (
            event["years_ago"] / total_years
        )
        clock_time = (
            convert_to_clock_time(event["years_ago"])
            if event["years_ago"] != 4_600_000_000
            else "24:00:00:000"
        )
        years_ago_formatted = format_years_ago(event["years_ago"])
        time_description = human_readable_time(milliseconds_on_clock)

        result.append(
            {
                "name": event["name"],
                "clock_time": clock_time,
                "years_ago": years_ago_formatted,
                "human_readable": time_description,
            }
        )

    return result


inputs = [
    {"name": "Earth's formation", "years_ago": 4_600_000_000},
    {"name": "First life on Earth", "years_ago": 3_700_000_000},
    {"name": "Dinosaurs appear", "years_ago": 230_000_000},
    {"name": "First humans", "years_ago": 300_000},
    {"name": "Modern civilization", "years_ago": 10_000},
    {"name": "Now", "years_ago": 0},
]

# Example usage
events = plot_historical_events(inputs)

for e in events:
    print(
        f"{e['name']} at {e['clock_time']} -> {e['years_ago']} ({e['human_readable']})"
    )
