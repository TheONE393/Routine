subjects = {
    'A': 'Bio-techniques',
    'B': 'Developmental Biology',
    'C': 'Adv. Mol. Bio.',
    'D': 'None',
    'E': 'Biophysics',
    'F': 'None',
    'G': 'None',
    'H': 'None',
    'J': 'None',
    'K': 'None',
    'X': '-',
    'L': 'LUNCH'
}

def subject_cell(code):
    value = subjects[code]
    if isinstance(value, str) and value.strip().lower() == 'none':
        return f'<td class="head X">{subjects["X"]}</td>'
    else:
        return f'<td class="head {code}">{value}</td>'

html = f'''<!DOCTYPE html>
<html>
    <head>
        <title>
            The ONE's Routine
        </title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="table.css">
        <link rel="icon" type="image/x-icon" href="theone.ico">
    </head>
    <body>
        <br>
        <div class="wallpaper">
            <table class="design">
                <tr class="rows">
                    <th class="head diagonal"><p style="float: left;">Day ⬇️</p><p style="float: right;"> Time ➡️</p></th>
                    <th class="head">8:30-9:30 am</th>
                    <th class="head">9:30-10:30 am</th>
                    <th class="head">10:30-11:30 am</th>
                    <th class="head">11:30-12:30 pm</th>
                    <th class="head">12:30-1:30 pm</th>
                    <th class="head"> 1:30-2:30 pm</th>
                    <th class="head">2:30-5:30 pm</th>
                    <th class="head">5:30-6:30 pm</th>
                    <th class="head">6:30-7:30 pm</th>
                </tr>
                <tr class="rows">
                    <th class="head">Monday</th>
                    {subject_cell('A')}
                    {subject_cell('B')}
                    {subject_cell('C')}
                    {subject_cell('D')}
                    <th class="head L" rowspan="5">{subjects['L']}</th>
                    {subject_cell('E')}
                    {subject_cell('G')}
                    {subject_cell('J')}
                    {subject_cell('K')}
                </tr>
                <tr class="rows">
                    <th class="head">Tuesday</th>
                    {subject_cell('F')}
                    {subject_cell('A')}
                    {subject_cell('B')}
                    {subject_cell('C')}
                    {subject_cell('D')}
                    {subject_cell('G')}
                    {subject_cell('K')}
                    {subject_cell('J')}
                </tr>
                <tr class="rows">
                    <th class="head">Wednesday</th>
                    {subject_cell('E')}
                    {subject_cell('F')}
                    {subject_cell('A')}
                    {subject_cell('B')}
                    {subject_cell('C')}
                    {subject_cell('H')}
                    {subject_cell('J')}
                    {subject_cell('K')}
                </tr>
                <tr class="rows">
                    <th class="head">Thursday</th>
                    {subject_cell('D')}
                    {subject_cell('E')}
                    {subject_cell('F')}
                    {subject_cell('A')}
                    {subject_cell('B')}
                    {subject_cell('H')}
                    {subject_cell('K')}
                    {subject_cell('J')}
                </tr>
                <tr class="rows">
                    <th class="head">Friday</th>
                    {subject_cell('C')}
                    {subject_cell('D')}
                    {subject_cell('E')}
                    {subject_cell('F')}
                    <td class="head X">{subjects['X']}</td>
                    <td class="head X">{subjects['X']}</td>
                    <td class="head X">{subjects['X']}</td>
                    <td class="head X">{subjects['X']}</td>
                </tr>
            </table>
        </div>
    </body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
