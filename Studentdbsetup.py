from cx_Freeze import *

includefiles = ["Student_management.ico"]
excludes=[]
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [

        (
            "DesktopShortcut",  # Shortcut
            "DesktopFolder",   # Dictionary
            "StudentManagementSystem", # name
            "TARGETDIR", # component
            "[TARGETDIR]\Student_Database_management_system.exe" , #Target
            None,  # argument
            None, # Description
            None, # Hotkey
            None, # Icon
            None, # IconIndex
            None, # Showcmd
            "TARGETDIR" , # WkDir
        )

]

msi_data = {"Shortcut": shortcut_table}


bdist_msi_options = {"data": msi_data}

setup(

        version="0.1",
        description = "Student Management System Developed By Ajay Nadar",
        author = "Ajay Nadar",
        name = "Student Management System",
        options = {'build_exe':{'include_files': includefiles},"bdist_msi": bdist_msi_options,},
        executables = [
            Executable(

                    script = "Student_Database_management_system.py",
                    base = base,
                    icon = 'Student_management.ico',
                )


        ]


)
