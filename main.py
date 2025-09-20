from pyscript import display, document

def generate_message(e): 

    # Values in input fields
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Escape characters for \t (tab), \" (quote)
    notes = f"\t{name} is currently {age} years old and studies at \"{school}\".\n"
    notes += "\tThis information was gathered through input fields and displayed using\n"
    notes += "\ta multiline string in Python via PyScript."

    # The multiline strings for the profile info
    profile = f"""
<div class="card p-3 bg-light mt-3">
    <b>🧑‍🎓 Student Profile</b><br>
    \nName   : {name}<br>
    \nAge    : {age}<br>
    \nSchool : {school}<br>
    <br>
    <span>📝 \nNotes:</span><br>
    <pre>{notes}</pre>
</div>
"""

    document.getElementById("output").innerHTML = profile

    # hooray im done
