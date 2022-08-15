<!DOCTYPE html>
<html>
    <head>
        <title>Your Machine Learning App</title>
    </head>

    <body>
        <form name="form", method="POST", style="text-align: center;">
            <br>
            temperature: <input type="number" name="temperature", placeholder="Enter temperature in C" required/>
            <br><br>
            humidity: <input type="number" name="humidity", placeholder="Enter humidity in %" required/>
            <br><br>
            pressure: <input type="number" name="pressure", placeholder="Enter pressure in hPa" required/>
            <br><br>
            precipitation: <input type="number" name="precipitation", placeholder="Enter precipitation in mm/h" required/>
            <br><br>
            cloudCover: <input type="number" name="cloudCover", placeholder="Enter cloudCover in %" required/>
            <br><br>
            elevation: <input type="number" name="elevation", placeholder="Enter elevation in m above sea level" required/>
            <br><br>
            <button value="Submit">Run</button>
        </form>
        <p style="text-align: center;">{{ output }}</p>
    </body>
</html>
