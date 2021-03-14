######
#   Project files Structure 
#
#├── CMakeLists.txt
#├── main
#│   ├── CMakeLists.txt
#│   ├── component.mk               Component make file
#│   └── [Projectname].c
#├── Makefile                       Makefile used by legacy GNU Make
#└── [Projectname].code-workspace   Needed by VSCode
######

import os
import tkinter as tk

#####################################
# Generate files when Generate button is clicked
def generate_files():
    project_name = ent_project_name.get()
    project_dir = ent_directory.get() + '/' + project_name
    project_subdir = project_dir + "/main"

    try:
    	os.makedirs(project_dir)
    except OSError:
    	print ("Creation of the directory %s failed" % project_dir)
    else:
    	print ("Successfully created the directory %s " % project_dir)

    #######################
    # Create files on project directory
    file = 'CMakeLists.txt'
    with open(os.path.join(project_dir, file), 'w') as fp: 
    	pass

    file = 'Makefile'
    with open(os.path.join(project_dir, file), 'w') as fp: 
    	pass

    # Needed by VSCODE. The settings inside this file will make command prompt the default terminal
    # and configure the path of ESP-IDF tools.
    file = project_name + '.code-workspace'                 
    with open(os.path.join(project_dir, file), 'w') as fp: 
    	pass

    #######################
    # Create files on the main subdirectory


    try:
    	os.makedirs(project_subdir)
    except OSError:
    	print ("Creation of the directory %s failed" % project_subdir)
    else:
    	print ("Successfully created the directory %s " % project_subdir)


    file = project_name + '.c'
    with open(os.path.join(project_subdir, file), 'w') as fp: 
    	pass

    file = 'component.mk'
    with open(os.path.join(project_subdir, file), 'w') as fp: 
    	pass

    file = 'CMakeLists.txt'
    with open(os.path.join(project_subdir, file), 'w') as fp: 
    	pass

    ########################
    # Write charactes on the project files
    with open(project_dir + '/Makefile', 'w') as writer:
    	writer.write("#\n")
    	writer.write("# This is a project Makefile. It is assumed the directory this Makefile resides in is a\n")
    	writer.write("# project subdirectory.\n")
    	writer.write("#\n\n")
    	writer.write("PROJECT_NAME := " + project_name + "\n")
    	writer.write("\n")
    	writer.write("include $(IDF_PATH)/make/project.mk")
    writer.close()

    with open(project_dir + '/CMakeLists.txt', 'w') as writer:
    	writer.write("# The following lines of boilerplate have to be in your project's\n")
    	writer.write("# CMakeLists in this exact order for cmake to work correctly\n")
    	writer.write("cmake_minimum_required(VERSION 3.5)\n\n")
    	writer.write("include($ENV{IDF_PATH}/tools/cmake/project.cmake)\n")
    	writer.write("project(" + project_name + ")")
    writer.close()

    with open(project_dir + '/main/'+ project_name + '.c', 'w') as writer:
    	writer.write("#include <stdio.h>\n")
    	writer.write("#include \"freertos/FreeRTOS.h\"\n")
    	writer.write("#include \"freertos/task.h\"\n")
    	writer.write("#include \"driver/gpio.h\"\n")
    	writer.write("#include \"sdkconfig.h\"")
    	writer.write("\n\n\n")
    	writer.write("void app_main(void)\n")
    	writer.write("{\n")
    	writer.write("\n\n\n")
    	writer.write("}")
    writer.close()

    with open(project_dir + '/main/CMakeLists.txt', 'w') as writer:
    	writer.write("idf_component_register(SRCS \"" + project_name + ".c\" INCLUDE_DIRS \"\")")
    writer.close()

    with open(project_dir + '/main/component.mk', 'w') as writer:
    	writer.write("#\n")
    	writer.write("# \"main\" pseudo-component makefile.\n")
    	writer.write("#\n")
    	writer.write("# (Uses default behaviour of compiling all source files in directory, adding 'include' to include path.)")
    writer.close()

    with open(project_dir + '/' + project_name + '.code-workspace', 'w') as writer:
    	writer.write("{\n")
    	writer.write("\t\"folders\": [\n")
    	writer.write("\t\t{\n")
    	writer.write("\t\t\t\"path\": \".\"\n")
    	writer.write("\t\t}\n")
    	writer.write("\t],\n")
    	writer.write("\"settings\": {\n\n")
    	writer.write("\t\t\"terminal.integrated.shell.windows\": \"cmd.exe\",\n")
    	writer.write("\t\t\"terminal.integrated.shellArgs.windows\": [\n")
    	writer.write("\t\t\t\"/k\",\n")
    	writer.write("\t\t\t\"${env:IDF_PATH}/export.bat\"\n")
    	writer.write("\t\t],\n")
    	writer.write("\t}\n")
    	writer.write("}")
    writer.close()

#End of  Generate file function
##################################	

    

# Set-up the window
#
window = tk.Tk()
window.title("ESP-IDF Project Generator")
window.resizable(width=True, height=True)

# Create a GUI for the user to enter the Project directory and Project Name
#
frm_entry = tk.Frame(master=window)
lbl_directory = tk.Label(master=frm_entry, text="Project Directory")
lbl_project_name = tk.Label(master=frm_entry, text="Project Name")
ent_directory = tk.Entry(master=frm_entry, width=50)
ent_project_name = tk.Entry(master=frm_entry, width=50)

ent_project_name.grid(row=1, column=1, sticky="e")
ent_directory.grid(row=0, column=1, sticky="e")

btn_generate = tk.Button(
    master=window,
    text="Generate",
    command = generate_files
)

frm_entry.grid(row=0, column=1, padx=10)
lbl_directory.grid(row = 0, column=0, padx=10)
lbl_project_name.grid(row = 1, column=0, padx=10)
btn_generate.grid(row = 2, column=1)

window.mainloop()


