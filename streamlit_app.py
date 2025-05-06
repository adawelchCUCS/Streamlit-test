from streamlit_option_menu import option_menu


# # horizontal menu
options = ["Home", "REA Framework",
           "Project Management", "Report Hub", "Dashboards", "Online Resources"]

icons = ["house", "flag", "calendar3", "pencil-square",
         "check-square", "lightbulb"]

selected = option_menu(menu_title=None, options=options,
                       icons=icons, orientation="horizontal")

if selected == 'Home':
    pass  # Or handle the 'Home' page content here
else:
    for option in options:
        if selected == option:
            page = f'{selected}.py'
            with open(page) as f:
                exec(f.read())


