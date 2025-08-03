subjects = {
    'A': 'Plant Physiology (LH-01)',
    'B': 'Ecology (LH-02)',
    'C': 'Animal Physiology (LH-01)',
    'D': 'Inorganic Chemistry (LH-02)',
    'E': 'None',
    'F': 'None',
    'G': 'Plant Lab',
    'H': 'Animal Lab',
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
                    <td class="head X">{subjects['X']}</td>
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
        <div class="footer"><p>*For better view, turn to landscape mode.</p></div>
        <br>
        <br>
        <div class="books">
            Available PDFs of the books are:
            <br>
            <h3>Plant Physiology:</h3>
            <p>
                <a href="Books/Unit 6 - Taiz - Plant Physiology - 3rd.pdf">Taiz - Plant Physiology (better OCR)</a>
            </p>
            <p>
                <a href="Books/Plant physiology -- [by] Frank B_ Salisbury [and] Cleon Ross -- The Wadsworth botany series, Belmont, Calif, California, -- Belmont, Calif_, Wadsworth -- 1036840449 -- 961bd3181a2f624181c096b0243fda9c.pdf">Plant physiology - by Frank Salisbury and Cleon Ross</a>
            </p>
            <p>
                <a href="Books\Fundamentals of Plant Physiology - Taiz.pdf">Fundamentals of Plant Physiology - Lincoln Taiz, Eduardo Zeiger, Ian Max Møller, Angus Murphy</a>
            </p>
            <h3>
                Ecology:
            </h3>
            <p>
                <a href="Books/Ecology _ principles and applications -- J_ L_ Chapman, M J Reiss, M_ J_ Reiss -- 2nd ed, Cambridge, 1999 -- Cambridge University Press (Virtual -- 9780521005753 -- d396013086dd72dd695a938f70d8c7f4 -- Anna’s Archive.pdf">Ecology _ principles and applications (2nd ed) - J L Chapman, M J Reiss, M J Reiss</a>
            </p>
            <p>
                <a href="Books/Essentials of Ecology -- Townsend, Colin R_, Begon, Michael, Harper, John L_ -- 2nd ed_, Malden, Mass, Oxford, England, 2003 -- Blackwell Publishers -- 9781405103282 -- a33d85ac3dc8cf67f11d0fb9bd47fed.pdf">Essentials of Ecology (2nd ed) - Townsend, Colin R, Begon, Michael, Harper, John L</a>
            </p>
            <p>
                <a href="Books/Fundamentals Of Ecology 3Rd Edition -- Madhab Chandra Dash -- 2011 -- MC GRAW HILL INDIA -- 9780070083660 -- c062607e2f4574c0d1dc4ea2488de9ac -- Anna’s Archive.pdf">Fundamentals Of Ecology 3Rd Edition - Madhab Chandra Dash</a>
            </p>
            <p>
                <a href="Books/Unit 10- Smith - Elements of Ecology 8th.pdf">Elements of Ecology, (Unit 10) - Smith</a>
            </p>
            <h3>Animal Physiology:</h3>
            <p>
                <a href="Books/Animal Physiology, 3rd Ed -- Richard W_ Hill, Gordon A_ Wyse, Margaret Anderson -- 3rd ed_, Sunderland, Mass, Massachusetts, 2012 -- Sinauer -- 9780878935598 -- a3af2ce7602f60658114fe5c854901f2 -- Anna’s Archive.pdf">Animal Physiology (3rd Ed) - Richard W Hill, Gordon A Wyse, Margaret Anderson</a>
            </p>
            <p>
                <a href="Books\ISE Integrated Principles of Zoology -- Cleveland Hickman & Susan Keen & David Eisenhour & Allan-compressed.pdf">ISE Integrated Principles of Zoology - Cleveland Hickman & Susan Keen & David Eisenhour & Allan</a>
            </p>
            <p>
                <a href="Books/Principles Of Anatomy And Physiology, 14th Edition -- Gerard J_ Tortora, Bryan H_ Derrickson, Brendan Burkett, -- 14, 2013 -- Wiley & Sons, -- 9781118345009 -- 51b1fb3c2e47538e51cc7e964fde3f2c -- Anna.pdf">Principles Of Anatomy And Physiology (14th ed) - Gerard J Tortora, Bryan H Derrickson</a>
            </p>
            <h3>Inorganic Chemistry:</h3>
            <p>
            </p>
        </div>
        <br><br><br><br><br><br><br><br><br><br><br><br>
    </body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
