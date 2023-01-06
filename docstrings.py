def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    f_name = f_name.title()
    l_name = l_name.title()

    return f_name + " " + l_name

f_name = input("Enter first name: ")
l_name = input("Enter last name: ")

full_name = format_name(f_name, l_name)
print(full_name)