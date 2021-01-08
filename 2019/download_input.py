import arrow
import requests

today = arrow.now()
# today = arrow.get('2019-12-01')

day = today.day
with open(f'inputs/day{day}', 'w') as input_file:
    content = requests.get(
        f'https://adventofcode.com/2019/day/{day}/input',
        headers={
            'Cookie': 'session=53616c7465645f5f1cbcb55ef1a1046a970afdd78f37f950e75df92cafa2b8f057db5cbdbcf28b8b44371ba26044bc80'
        }
    ).text
    # breakpoint()
    input_file.write(content)


