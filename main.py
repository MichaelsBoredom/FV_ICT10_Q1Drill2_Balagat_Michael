from pyscript import display, document

def generate_message(event=None): 
    #  I included the (event=None) 
    #  to avoid errors beacuse it said 
    #  "TypeError: generate_message() takes 0 positional arguments but 1 was given"
    #  So it's necessary for some reason


    # I assigned the strings to variables in here
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # I used escape characters: \t (tab), \" (quote) right here
    notes = f"\t{name} is currently {age} years old and studies at \"{school}\".\n"
    notes += "\tThis information was gathered through input fields and displayed using\n"
    notes += "\ta multiline string in Python via PyScript."

    # The multiline string for the profile info
    profile = f"""
<div class="card p-3 bg-light mt-3">
    <b>🧑‍🎓 Student Profile</b><br>
    Name   : {name}<br>
    Age    : {age}<br>
    School : {school}<br>
    <br>
    <span>📝 <b>Notes:</b></span><br>
    <pre>{notes}</pre>
</div>
"""

    document.getElementById("output").innerHTML = profile

    # hooray im done