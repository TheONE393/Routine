from pathlib import Path

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

slot_colors = {
    'A': '#FFB347',
    'B': '#5F9EA0',
    'C': '#7FFFD4',
    'D': '#98FB98',
    'E': '#FF6F61',
    'F': '#C0C0C0',
    'G': '#2fcb59',
    'H': '#B12323',
    'J': '#40E0D0',
    'K': '#FFA07A',
    'L': '#FFD1DC',
    'X': '#E0E0E0'
}

rows = [
    {
        'day': 'Monday',
        'cells': ['A', 'B', 'C', 'D', 'L', 'E', 'G', 'J', 'K']
    },
    {
        'day': 'Tuesday',
        'cells': ['F', 'A', 'B', 'C', 'D', 'G', 'K', 'J']
    },
    {
        'day': 'Wednesday',
        'cells': ['E', 'F', 'A', 'B', 'C', 'H', 'J', 'K']
    },
    {
        'day': 'Thursday',
        'cells': ['D', 'E', 'F', 'A', 'B', 'H', 'K', 'J']
    },
    {
        'day': 'Friday',
        'cells': ['C', 'D', 'E', 'F', 'X', 'X', 'X', 'X']
    }
]

slot_codes = ['A', 'B', 'C', 'D', 'E', 'F']

# Build the table rows with stable data attributes for each editable slot.
def subject_cell(day, col_index, code):
    value = subjects.get(code, '-')
    label = value if isinstance(value, str) and value.strip().lower() != 'none' else '-'
    return f'<td class="head {code}" data-slot="{code}" data-default-text="{label}" style="background-color: {slot_colors.get(code, slot_colors["X"])};">{label}</td>'

rows_markup = []
rows_markup.append(f'''<tr class="rows">
    <th class="head">Monday</th>
    {subject_cell('Monday', 0, 'A')}
    {subject_cell('Monday', 1, 'B')}
    {subject_cell('Monday', 2, 'C')}
    {subject_cell('Monday', 3, 'D')}
    <th class="head L" rowspan="5">{subjects['L']}</th>
    {subject_cell('Monday', 5, 'E')}
    {subject_cell('Monday', 6, 'G')}
    {subject_cell('Monday', 7, 'J')}
    {subject_cell('Monday', 8, 'K')}
</tr>''')
rows_markup.append(f'''<tr class="rows">
    <th class="head">Tuesday</th>
    {subject_cell('Tuesday', 0, 'F')}
    {subject_cell('Tuesday', 1, 'A')}
    {subject_cell('Tuesday', 2, 'B')}
    {subject_cell('Tuesday', 3, 'C')}
    {subject_cell('Tuesday', 4, 'D')}
    {subject_cell('Tuesday', 5, 'G')}
    {subject_cell('Tuesday', 6, 'K')}
    {subject_cell('Tuesday', 7, 'J')}
</tr>''')
rows_markup.append(f'''<tr class="rows">
    <th class="head">Wednesday</th>
    {subject_cell('Wednesday', 0, 'E')}
    {subject_cell('Wednesday', 1, 'F')}
    {subject_cell('Wednesday', 2, 'A')}
    {subject_cell('Wednesday', 3, 'B')}
    {subject_cell('Wednesday', 4, 'C')}
    {subject_cell('Wednesday', 5, 'H')}
    {subject_cell('Wednesday', 6, 'J')}
    {subject_cell('Wednesday', 7, 'K')}
</tr>''')
rows_markup.append(f'''<tr class="rows">
    <th class="head">Thursday</th>
    {subject_cell('Thursday', 0, 'D')}
    {subject_cell('Thursday', 1, 'E')}
    {subject_cell('Thursday', 2, 'F')}
    {subject_cell('Thursday', 3, 'A')}
    {subject_cell('Thursday', 4, 'B')}
    {subject_cell('Thursday', 5, 'H')}
    {subject_cell('Thursday', 6, 'K')}
    {subject_cell('Thursday', 7, 'J')}
</tr>''')
rows_markup.append(f'''<tr class="rows">
    <th class="head">Friday</th>
    {subject_cell('Friday', 0, 'C')}
    {subject_cell('Friday', 1, 'D')}
    {subject_cell('Friday', 2, 'E')}
    {subject_cell('Friday', 3, 'F')}
    {subject_cell('Friday', 4, 'X')}
    {subject_cell('Friday', 5, 'X')}
    {subject_cell('Friday', 6, 'X')}
    {subject_cell('Friday', 7, 'X')}
</tr>''')

slot_options_markup = ''.join(f'<option value="{code}">{code}</option>' for code in slot_codes)

html = '''<!DOCTYPE html>
<html>
    <head>
        <title>The ONE's Routine</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="table.css">
        <link rel="icon" type="image/x-icon" href="theone.ico">
    </head>
    <body>
        <div class="form-panel">
            <h2>Customise your routine</h2>
            <form id="slot-form">
                <label for="slot">Choose a slot</label>
                <select id="slot" name="slot">
                    __SLOT_OPTIONS__
                </select>
                <label for="course-name">Course name</label>
                <input id="course-name" name="course-name" type="text" placeholder="Enter course name or type None to clear" required>
                <label for="course-color">Choose a colour</label>
                <input id="course-color" name="course-color" type="color" value="#40E0D0">
                <button type="submit">Submit</button>
            </form>
        </div>
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
                    <th class="head">1:30-2:30 pm</th>
                    <th class="head">2:30-5:30 pm</th>
                    <th class="head">5:30-6:30 pm</th>
                    <th class="head">6:30-7:30 pm</th>
                </tr>
                __TABLE_ROWS__
            </table>
        </div>
        <script>
            const form = document.getElementById('slot-form');
            const slotSelect = document.getElementById('slot');
            const courseNameInput = document.getElementById('course-name');
            const colorInput = document.getElementById('course-color');

            form.addEventListener('submit', function (event) {
                event.preventDefault();
                const slotCode = slotSelect.value;
                const courseNameInputValue = courseNameInput.value.trim();
                const courseName = courseNameInputValue && courseNameInputValue.toLowerCase() !== 'none'
                    ? courseNameInputValue
                    : '-';
                const color = colorInput.value;
                const cells = document.querySelectorAll(`td[data-slot="${slotCode}"]`);

                cells.forEach((cell) => {
                    cell.textContent = courseName;
                    cell.style.backgroundColor = color;
                    cell.style.color = '#111';
                });
            });
        </script>
    </body>
</html>'''

html = html.replace('__SLOT_OPTIONS__', slot_options_markup)
html = html.replace('__TABLE_ROWS__', ''.join(rows_markup))

output_path = Path(__file__).with_name('index.html')
output_path.write_text(html, encoding='utf-8')
